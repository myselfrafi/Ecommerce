from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ProductForm
from  products.models import Product


def show_products(request):
    product = Product.objects.all()

    context = {
        'all_products':product
    }
    return render(request,'showProduct.html',context)


def show_one_product(request,pk):
    try:
        one_product = Product.objects.get(id=pk)
        

        context = {
            'one_product':one_product
        }
        return render(request,'showProductDetail.html',context)
    except:
        return HttpResponse("<h3>Product Item not found...X X X</h3>")




def add_product(request):
    form = ProductForm()

    if(request.method=='POST'):
        form = ProductForm(request.POST,request.FILES)

        if(form.is_valid()):
            form.save()
            return redirect('show-products')

    context = {
        'form':form
    }
    return render(request,'addProduct.html',context)




def about_product(request):
    return render(request,'About.html')

def Courosal(request):
    featured_products = Product.objects.all()[:3]
    all_products = Product.objects.all()

    context = {
        'featured_products': featured_products,
        'all_products': all_products
    }
    return render(request,'courosal.html')






"""def update_product(request,pk):
    try:
        one_product = Product.objects.get(id=pk)

        product = ProductForm(instance=one_food)

        if(request.method=='POST'):
            form = ProductForm(request.POST,request.FILES,instance=one_product)

            if(product.is_valid()):
                form.save()
                return redirect('show-products')
            
        context = {
            'form':form
        }

        return render(request,'updateProduct.html',context)
    except:
        return HttpResponse("<h3>Product Item not found...X X X</h3>")"""



"""def delete_product(request,pk):
    try:
        one_product = Product.objects.get(id=pk)
        one_product.delete()

        return redirect('show-products')
    except:
        return HttpResponse("<h3>Product Item not found...X X X</h3>")"""
        
        
