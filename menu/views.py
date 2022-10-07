from django.shortcuts import render

# Create your views here.

def menu(request):

	return render(
		request=request,
		template_name = "menu.html",
		context={}
	)