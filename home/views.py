from django.shortcuts import render

# Create your views here.

def home(request):

	return render(
		request=request,
		template_name = "home.html",
		context={}
	)
	
def chefs(request):

	return render(
		request=request,
		template_name = "chefs.html",
		context={}
	)
