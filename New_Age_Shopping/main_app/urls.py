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
    path('merchant_shop_now/<str:slug>/<int:pk>/', views.category_shopping, name="merchant_shop_now"),
    path('checkout/', views.checkout, name="checkout"),
    path('wishlist/<int:pk>/', views.wishlist, name="wishlist"),
    path('wishlist/', views.nav_wishlist, name="nav_wishlist"),
    path('remove_cart/', views.remove_cart, name="remove_cart"),
    path('update_item/', views.update_item, name="update_item"),
    path('payment_view/', views.esewa_gateway, name="payment_view"),
    path('paypal_gateway/', views.paypal_gateway, name="paypal_gateway"),
    path('add_comment/<int:pk>/', views.addComment, name="add_comment"),
    path('merchant_list/', views.totalMerchant, name="merchant_list"),
    path("post_payment/", views.postPayment, name="post_payment"),
    path("remove_wishlist/<int:pk>/", views.remove_wishlist, name="remove_wishlist"),
    path("esewa_successful/", views.esewaSuccessful, name="esewa_successful")
    # path('merchant_shopping_page/<int:pk>', views.merchantShopPage, name="merchant_shopping_page")
]

