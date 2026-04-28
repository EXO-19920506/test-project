from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.add_item, name='add_item'),
    path('update/<int:product_id>/', views.update_item, name='update_item'),
    path('delete/<int:product_id>/', views.delete_item, name='delete_item'),
]
