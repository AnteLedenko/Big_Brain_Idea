# Here im using djangos generic view classes to implement CRUD operations for Post model, also importing 
# Comment model and CommentForm to display it in PostDetailView.
# PostListView displays a paginated list of posts 9 per page in descending order of date.
# PostDetailView shows post details, comments, and a comment form using 'blog/post_details.html'.
# PostCreateView alows logged-in users to create posts with title and content
# PostUpdateView author can edit title and content. 
# PostDeleteView author can delete their posts after comfirmation.
# like_post function lets the logged in user to add and remove likes.

from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from comments.forms import CommentForm
from comments.models import Comment
from .models import Post


def about(request):
    return render(request, 'blog/about.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 9

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comments.filter().order_by('-date_posted')
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('home')  

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post-detail', pk=post.id)




