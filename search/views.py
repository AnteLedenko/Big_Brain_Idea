# the search_results function handles search functionality for posts and users. 
# retrieves search results from the Post and User models based on a query string 'q'.
# logged in users  search queries are logged in the SearchQuery model.

from django.shortcuts import render
from django.contrib.auth.models import User
from blog.models import Post
from .models import SearchQuery

def search_results(request):
    query = request.GET.get('q')
    post_results = []
    user_results = []

    if query:
        post_results = Post.objects.filter(title__icontains=query)
        user_results = User.objects.filter(username__icontains=query)
        if request.user.is_authenticated:
            SearchQuery.objects.create(user=request.user, query=query)

    return render(request, 'search/search_results.html', {
        'query': query,
        'post_results': post_results,
        'user_results': user_results
    })
