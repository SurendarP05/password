from rest_framework import serializers

from .utils import send_normal_email
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import smart_str, smart_bytes
from django.urls import reverse

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['id', 'uname', 'email', 'fname', 'lname', 'gender', 'phone', 'newpassword', 'confirmpassword']

# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()  
#     password = serializers.CharField()
        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LonginModel
        fields = '__all__'

    def validate(self, data):
        if not UserRegistration.objects.filter(uname = data['username'], confirmpassword=data['password'] ).exists():
            raise serializers.ValidationError("Account Not Fount")
        return data
    
    def get_jwt(self, data):
        user = UserRegistration.objects.filter(uname = data['username']).first()
        if not user:
            return Response({'message': 'Invalide Creditials'})
        refresh = RefreshToken().for_user(user)
       
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),

           
        }


class PasswordReSetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get('email')
        if UserRegistration.objects.filter(email =email).exists():  
            user = UserRegistration.objects.get(email=email)
            print(user)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            request = self.context.get('request')
            site_domain = get_current_site(request).domain
            relative_link = reverse('password-reset-confirm',kwargs={'uidb64':uidb64, 'token':token })
            abslink = f"http://{site_domain}{relative_link}"
            email_body = f"HI link below the reset password\n{abslink}" 
            data = {
                'email_body' : email_body,
                'email_subject': "Reset your password",
                'to_email':user.email
            }
            send_normal_email(data)

        return super().validate(attrs) 
    