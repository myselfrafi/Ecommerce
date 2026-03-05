from django.shortcuts import render,redirect

from .forms import RegisterForm,LoginForm

from django.contrib.auth.views import LogoutView

from .models import Register

from products.models import Product

from django.contrib import messages

from django.contrib.auth import logout

from django.db.models import Q  




def register(request):
    form = RegisterForm()

    if(request.method=='POST'):
        form = RegisterForm(request.POST)

        if(form.is_valid()):
            data = form.save(commit=False)

            pwd = form.cleaned_data.get('password')

            data.set_password(pwd)
            form.save()
            
            return redirect('login-form')  #--------------
        
    context = {
        'form':form
    }

    return render(request,'Registration.html',context)




def login(request):
    form = LoginForm()
    if(request.method=='POST'):

        form = LoginForm(request.POST)

        if(form.is_valid()):
            try:
                EMAIL = form.cleaned_data['email']
                PASSWORD = form.cleaned_data['password']

                one_user = Register.objects.get(email=EMAIL)

                print(one_user.password)
                print(PASSWORD)

                if(one_user.check_password(PASSWORD)):
                    messages.success(request,'Login Successfully...')
                    return redirect('Home-Page')#----------------------
                else:
                    messages.error(request,'Password Does not Matched with Registered Details..X X X')

            except:
                messages.error(request,'User Does not Existed with this Details...X X X')


    context = {
        'form':form
    }
    return render(request,'Login.html',context)




def LogoutView(request):
    if request.method == "POST":
        logout(request)
        return redirect('login-form')  





def homepage(request):
    query = request.GET.get('q')

    if query:
        all_products = Product.objects.filter(Q(name__icontains=query))
    else:
        all_products = Product.objects.all()

    context = {
        'all_products': all_products
    }

    return render(request, 'homepage.html', context)


