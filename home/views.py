from django.shortcuts import render
from blog.models import blog
from chefs.models import Chefs
from aboutUs.models import History, Feedback

# Create your views here.

def home(request):
	latestPosts = blog.objects.all().order_by('-id')[0:4]
	chefs 		= Chefs.objects.all().order_by('-id')[0:3]
	ourHistory  = History.objects.all()
	feedback    = Feedback.objects.all().order_by('-id')[0:5]

	return render(
		request=request,
		template_name = "home.html",
		context={
			'latestPosts': latestPosts,
			'chefs': chefs,
			'ourHistory': ourHistory,
			'feedback': feedback,
		}
	)