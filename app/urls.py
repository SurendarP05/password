from django.urls import path
# from .views import UserRegistrationAPIView, LoginApi
from .views import *

urlpatterns = [
    # path('register/', UserRegistrationAPIView.as_view()),
    path('login/', LoginApi.as_view()),
    path('user/', UserView.as_view()),
    # path('login/', LoginView.as_view()),
    path('resetpassword/', PasswordResetview.as_view())
    
]
