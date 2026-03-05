from django.shortcuts import render,redirect,get_object_or_404


from .models import Cart
 
from products.models import Product


def add_2_cart(request, pk):
    product = get_object_or_404(Product, id=pk)

    cart_item, created = Cart.objects.get_or_create(product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view-cart')




def reduce_cart_item_quantity(request,cart_id):
    one_cart_item = get_object_or_404(Cart,id=cart_id)

    if(one_cart_item.quantity>1):
        one_cart_item.quantity-=1
        one_cart_item.save()
    else:
        one_cart_item.delete()

    return redirect('view-cart')


def remove_cart_item(request,cart_id):
    one_cart_item = get_object_or_404(Cart,id=cart_id)

    one_cart_item.delete()

    return redirect('view-cart')


def view_cart(request):
    cart_items = Cart.objects.all()
    total_cart_items_price = sum(i.total_price for i in cart_items)

    context = {
        'cart_items':cart_items,
        'total_cart_items_price':total_cart_items_price
    }

    return render(request,'Cart/cart.html',context)

