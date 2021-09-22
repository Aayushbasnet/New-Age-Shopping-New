from django.urls import path
from . import views

app_name    =   'account'
urlpatterns = [
    path('login/', views.loginPage, name="login_page"),
    path('signup/', views.signupPage, name="signup_page"),
    path('merchant_signup/', views.merchantSignupPage, name="merchant_signup_page"),
    path('logout/', views.logoutpage, name="logout_page")

]