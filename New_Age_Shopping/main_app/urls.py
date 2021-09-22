from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home_page"),
    path('detail/<int:pk>', views.detail, name="detail_page"),
    path('cart/', views.cart, name="cart_page"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('about_us/', views.about_us, name="about_us"),
    path('shop_now/', views.shop_now, name="shop_now"),
    path('shop_now/<str:slug>/', views.category_shopping, name="shop_now"),
    path('checkout/', views.checkout, name="checkout"),
    path('whishlist/', views.whishlist, name="whishlist"),
    path('remove_cart/', views.remove_cart, name="remove_cart"),
    path('update_item/', views.update_item, name="update_item"),
    path('payment_view/', views.payment_view, name="payment_view"),
    

]