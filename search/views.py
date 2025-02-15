from django.shortcuts import render
from blog.models import Post
from django.contrib.auth.models import User
from .models import SearchQuery
from django.contrib.auth.decorators import login_required

@login_required
def search_results(request):
    query = request.GET.get('q')
    post_results = []
    user_results = []

    if query:
        post_results = Post.objects.filter(title__icontains=query)
        user_results = User.objects.filter(username__icontains=query)
        SearchQuery.objects.create(user=request.user, query=query)

    return render(request, 'search/search_results.html', {
        'query': query,
        'post_results': post_results,
        'user_results': user_results
    })