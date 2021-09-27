from django.urls import path
from . import views

app_name    =   'account'
urlpatterns = [
    path('login/', views.loginPage, name="login_page"),
    path('signup/', views.signupPage, name="signup_page"),
    path('merchant_signup/', views.merchantSignupPage, name="merchant_signup_page"),
    path('logout/', views.logoutpage, name="logout_page"),

    path('password_reset/', view = views.PasswordResetView.as_view(), name = "password_reset"),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/done/', view = views.PasswordResetDoneView.as_view(), name = "password_reset_done"),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]