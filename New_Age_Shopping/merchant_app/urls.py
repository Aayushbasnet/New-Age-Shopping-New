from django.urls import path
from . import views

app_name    =   'merchant_app'

urlpatterns = [
    path('', views.merchantDashboard, name="merchantDashboard"),
    path('delete_product/', views.delete_product, name="delete_product"),
    path('edit_product/', views.edit_product, name="edit_product"),


]