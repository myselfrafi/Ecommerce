from django.urls import path
from products import views


urlpatterns = [
     path('add', views.add_product,name='add-product'),
     path('show',views.show_products,name='show-products'),
     path('show_product_detail/<int:pk>',views.show_one_product,name='show-one-product'),
     path('about/',views.about_product,name='about-page'),
] 