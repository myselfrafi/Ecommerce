from django.urls import path

from Cart import views


urlpatterns = [
    path('viewcart',views.view_cart,name='view-cart'),
    path('add2cart/<int:pk>',views.add_2_cart,name='add-2-cart'),
    path('reducequantity/<int:cart_id>',views.reduce_cart_item_quantity,name='reduce-cart-item'),
    path('remove/<int:cart_id>',views.remove_cart_item,name='remove-cart-item'),
]
