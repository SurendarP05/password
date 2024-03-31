from django.urls import path
from .views import *


urlpatterns = [

    path('myregister/',RegistrationAPIView.as_view(),name= 'password- register'),
    path('mylogin/', LoginView.as_view(),name= 'password-login'),
    path('myresetpassword/',  PasswordResetMail.as_view()),
    path('reset-confirm/<str:uid>/<str:token>/', PasswordResetConfirmAPIView.as_view(), name='password-reset-confirm'),
]