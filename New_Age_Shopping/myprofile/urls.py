from django.urls import path
from . import views

app_name = "myprofile"

urlpatterns = [
    path("", view=views.myProfile, name="myprofile"),
    path("shippingaddress/", view=views.shippingAddress1, name="shippingaddress"),
    path("addshippingaddress/", view=views.addShippingAddress, name="add-shipping-address"),
    path("my_order/", view=views.myOrder, name="my_order"),
    path("my_review/", view=views.myReview, name="my_review"),
    path("update_user_profile/", view=views.updateProfile, name="update_user_profile"),
    path('review_seller/', view=views.reviewSeller, name="review_seller"),
    path('review_seller/<int:pk>/', view=views.reviewSellerSuccess, name="review_seller_success"),


]