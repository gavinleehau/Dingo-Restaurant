from django.http import HttpResponse
from django.urls import path, re_path, include
from . import views

urlpatterns = [
	path('', views.showPosts, name='showPosts'),
	re_path(r"^postDetail/(?P<post_id>[0-9]+)$", views.postDetail, name="postDetail"),
 	path('comment/<int:post_id>', views.addComment, name='comment')
	# path('postDetail/<int:post_id>', views.postDetail, name='postDetail'),
]