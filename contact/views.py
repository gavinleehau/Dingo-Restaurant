from django.shortcuts import render, redirect
from .models import ContactInfo, Reservations

# Create your views here.

def contact(request):
    contactInfo = ContactInfo.objects.get(pk=1)
    data = Reservations()
    if request.method == 'POST':
        data.email = request.POST['email']
        data.customerName = request.POST['customerName']
        data.phoneNumber = request.POST['phoneNumber']
        data.date = request.POST['date']
        data.time = request.POST['time']
        data.amount = request.POST['amount']
        data.note = request.POST['note']
        data.save()
        return redirect('success_page')
		
    return render(
		request=request,
		template_name = "contact.html",
		context={
			'contactInfo': contactInfo
		}
	)

def success_page(request):

    return render(
        request=request,
        template_name="success_page.html",
        context={}
    )

	
 
	
