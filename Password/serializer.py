from rest_framework import serializers
from django.core.mail import send_mail
from .models import *
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_str, force_bytes
from  django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator


from django.contrib.auth.hashers import make_password
class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=120, write_only=True)
    def create(self, validate_data):
        print(validate_data)
        validate_data['password'] = make_password(validate_data['password'])
        user =  RegistrationModel.objects.create(**validate_data)
        return user

from django.contrib.auth import authenticate 
class MyLoginSerializer(serializers.ModelSerializer):
   
    class Meta:
       model = MyLonginModel
       fields = '__all__'

    def validate(self, data):
        email = data.get("email")
        password = data.get("passord")
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError("Invalid User")
        else:
            raise serializers.ValidationError("Error")
        data['user'] = user
        # if not RegistrationModel.objects.filter(email = data['email'], password=data['password'] ).exists():
        #     raise serializers.ValidationError("Account Not Fount")
        return data

    def get_jwt(self, data):
        user = RegistrationModel.objects.filter(email = data['email']).first()
        if not user:
            return Response({'message': 'Invalide Creditials'})
        refresh = RefreshToken().for_user(user)
        
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        
        }
    
class PasswordReSetMailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get('email')
        if RegistrationModel.objects.filter(email=email).exists():  
            user = RegistrationModel.objects.get(email=email)
            print(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk)) 
            token = PasswordResetTokenGenerator().make_token(user)
            link = 'http://localhost:8000/reset-confirm/' + str(uid) + '/' + token
            send_mail(
                'Password Reset Link',
                f'Click the following link to reset your password: {link}' ,
                'psurendar@gmail.com',
                [email],
                fail_silently=False,
            )
            return attrs
        else:
            raise serializers.ValidationError("YOU ARE NOT REGISTERED")



class PasswordResetSerializer(serializers.Serializer):
    # class Meta:
        # model = RegistrationModel
        # fields = ['password']
    password = serializers.CharField()

    def validate(self, attrs):
        password = attrs.get('password')
        uid = self.context.get('uid')
        # print(uid)
        token = self.context.get('token')
        try:
            uid = urlsafe_base64_decode(uid).decode()
            user = RegistrationModel.objects.get(pk=uid)
        except RegistrationModel.DoesNotExist:
            raise serializers.ValidationError("Invalid reset link")
        except Exception as e:
            print(e, "hjfciehijhidfhiehiheiheihei")
            raise serializers.ValidationError("Failed to reset password")
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError("Invalid reset link")
        else:
            user.set_password(password)
            print(password, '66666666666666666666666666666666666666666')
            user.save()
        return attrs

    def update(self, instance, validated_data):
        # No need to implement this method as we are updating existing instance
        pass