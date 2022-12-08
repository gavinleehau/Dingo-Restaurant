from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import InstagramFeeds, author, blog, author, InstagramFeeds

# Create your views here.

def showPosts(request):
    if 'q' in request.GET:
        q = request.GET['q']
        Posts = blog.objects.filter(title__contains=q)
    else:
        Posts = blog.objects.all()
        
    new_paginator = Paginator(Posts, per_page = 5) #number of blogs per page
    page_number = request.GET.get('page')
    page = new_paginator.get_page(page_number)

    recentPosts = blog.objects.all().order_by('-id')[0:4]
    igFeeds 	= InstagramFeeds.objects.all()

    return render(
        request=request,
        template_name = "blog.html",
        context={
            'page': page,
            'recentPosts': recentPosts,
            'igFeeds': igFeeds,
        }
    )


def postDetail(request, post_id):
    post_detail = blog.objects.get(id=post_id)
    # authorOfPost= get_object_or_404(author, id=post_id)
    recentPosts = blog.objects.all().order_by('-id')[0:4]

    nextpost = blog.objects.filter(id__gt=post_detail.id).order_by ('id').first()
    prevpost = blog.objects.filter(id__lt=post_detail.id).order_by('id').last()
    

    return render(
        request=request,
        template_name = "single-blog.html",
        context={
            'post_detail': post_detail,
            'recentPosts': recentPosts,
            'nextpost': nextpost,
            'prevpost': prevpost,
            # 'authorOfPost': authorOfPost,
        }
    )


# def searchBar(request) :
#     if request.method == 'GET':
#         query=request.GET.get('query')
#         if query:
#             Post = blog.objects.filter(title__contains=query)
#             print('dung')
#             return render(request, 'searchbar.html', {'Post' : Post})
#         else:
#             print("No information to show")
#             return render(request, 'searchbar. html', {})