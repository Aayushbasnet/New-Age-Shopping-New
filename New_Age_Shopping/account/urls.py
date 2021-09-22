from django.urls import path
from . import views

app_name    =   'account'
urlpatterns = [
    path('login/', views.loginPage, name="login_page"),
    path('signup/', views.signupPage, name="signup_page"),
]