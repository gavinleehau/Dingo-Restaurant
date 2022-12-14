from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import InstagramFeeds, author, blog, author, InstagramFeeds, Comment
from contact.models import ContactInfo
from menu.models import Food

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
    contactInfo = ContactInfo.objects.get(pk=1)
    special = Special.objects.all().order_by('-id')[0:3]

    return render(
        request=request,
        template_name = "blog.html",
        context={
            'page': page,
            'recentPosts': recentPosts,
            'igFeeds': igFeeds,
            'contactInfo': contactInfo,
            'special': special,
        }
    )


def postDetail(request, post_id):
    post_detail = blog.objects.get(id=post_id)
    recentPosts = blog.objects.all().order_by('-id')[0:4]
    foods = Food.objects.all().order_by('-id')[0:5]
    comments = Comment.objects.filter(post=post_detail).order_by('-id')
    cmt_count = comments.count()

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
            'foods': foods,
            'comments': comments,
            'cmt_count': cmt_count
        }
    )
    
def addComment(request, post_id):
    url = request.META.get('HTTP_REFERER') # get last url
    user_id = request.user.id # Access User Session information
    commentDetails = ''
    if request.method == 'POST':
        if 'commentDetails' in request.POST:
            commentDetails = request.POST.get('commentDetails')
    commented = Comment.objects.create(
        post_id = post_id,
        user_id = user_id,
        comment = commentDetails,
    )
    commented.save()
    return redirect(url)


    
    
    