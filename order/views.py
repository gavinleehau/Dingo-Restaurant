from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required

from order.models import ShopCart, OrderForm, Order, ShopCartForm, OrderProduct
from menu.models import Food
from contact.models import ContactInfo

# Create your views here.

@login_required(login_url='/login')
def shopcart(request):
    shopcart = ShopCart.objects.all()
    shopcart_count = ShopCart.objects.all().count()
    contactInfo = ContactInfo.objects.get(pk=1)

    total=0
    for rs in shopcart:
        total += rs.product.price * rs.quantity

    return render(
        request=request,
        template_name= "cart.html",
        context={
            'shopcart': shopcart,
            'total': total,
            'shopcart_count': shopcart_count,
            'contactInfo': contactInfo,
        }
    )


@login_required(login_url='/login')
def addtoshopcart(request,id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    product = Food.objects.get(pk=id)
    checkinproduct = ShopCart.objects.filter(product_id=id, user_id=current_user.id) # Check product in shopcart

    if checkinproduct:
        control = 1 # The product is in the cart
    else:
        control = 0 # The product is not in the cart"""

    if request.method == 'POST':  # if there is a post
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control==1: # Update  shopcart
                data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
                data.quantity += form.cleaned_data['quantity']
                data.save()  # save data
            else : # Inser to Shopcart
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id =id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "Đã thêm sản phẩm vào giỏ hàng ")
        return redirect(shopcart)

    else: # if there is no post
        if control == 1:  # Update  shopcart
            data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
            data.quantity += 1
            data.save()  #
        else:  #  Inser to Shopcart
            data = ShopCart()  # model ile bağlantı kur
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.variant_id =None
            data.save()  #
        messages.success(request, "Đã thêm sản phẩm vào giỏ hàng")
        return redirect(shopcart)


@login_required(login_url='/login')
def deletefromcart(request,id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Sản phẩm đã xóa khỏi giỏ hàng.")
    return redirect(shopcart)


@login_required(login_url='/login')
def deletefromcart(request,id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Sản phẩm đã xóa khỏi giỏ hàng.")
    return redirect(shopcart)


@login_required(login_url='/login')
def orderproduct(request):
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    shopcart_count = ShopCart.objects.all().count()

    total = 0
    for rs in shopcart:
        total += rs.product.price * rs.quantity

    if request.method == 'POST':  # if there is a post
        form = OrderForm(request.POST)
        if form.is_valid():
            # Send Credit card to bank,  If the bank responds ok, continue, if not, show the error
            data = Order()
            data.full_name = form.cleaned_data['full_name'] #get product quantity from form 
            data.address = form.cleaned_data['address']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper() # random cod
            data.code =  ordercode
            data.save() 

            for rs in shopcart:
                detail = OrderProduct()
                detail.order_id = data.id # Order Id
                detail.product_id = rs.product_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity
                detail.price = rs.price
                detail.save()

            ShopCart.objects.filter(user_id=current_user.id).delete() # Clear & Delete shopcart after checkout
            request.session['cart_items']=0
            messages.success(request, "Đơn hàng của bạn đã đặt thành công. Xin cảm ơn đã ủng hộ ! ")
            return render(
                request=request, 
                template_name='success_page.html',
                context={
                    'ordercode':ordercode,
                })
        else:
            messages.warning(request, form.errors)
            print('sai')
            return HttpResponseRedirect("/order/orderproduct")

    form= OrderForm()

    return render(
        request=request,
        template_name = "checkout.html",
        context={
            'shopcart': shopcart,
            'total': total,
            'shopcart_count': shopcart_count,
        }
    )