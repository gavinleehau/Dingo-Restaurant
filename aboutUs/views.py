from unittest import mock
from django.shortcuts import render
from .models import History, Feedback
from chefs.models import Chefs

# Create your views here.

def about(request):
	ourHistory = History.objects.all()
	chefs      = Chefs.objects.all().order_by('-id')[0:3]
	feedback   = Feedback.objects.all().order_by('-id')[0:5]

	return render(
		request=request,
		template_name = "about.html",
		context={
			'ourHistory': ourHistory,
			'chefs': chefs,
			'feedback': feedback,
		}
	)