from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('email_verify/', VerifyEmail.as_view(), name='email_verify'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('logout/<pk>/', LogoutView.as_view(), name="logout"),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
    path('mapp/password-reset-complete/<pk>/', password_change, name='password_change'),
    path('success/', success, name='success'),
    path('user/<pk>/', UserView.as_view(), name='user'),
    path('users/<congregation>/', AllUsers.as_view(), name='users'),
]