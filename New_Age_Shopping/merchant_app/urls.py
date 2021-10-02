from django.urls import path
from . import views

app_name    =   'merchant_app'

urlpatterns = [
    path('', views.merchantDashboard, name="merchantDashboard"),
    path('delete_product/<int:id>/', views.delete_product, name="delete_product"),
    path('update_product/<int:id>/', views.update_product, name="update_product"),
    path('mlogout/', views.mlogout, name="mlogout"),
    path('mprofile_update/', views.mProfileUpdate, name="mprofile_update"),
]