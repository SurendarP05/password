from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from rest_framework import exceptions
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from .serializer import *
from rest_framework.generics import GenericAPIView
from .exception import ServiceUnavailable 
from rest_framework.generics import ListCreateAPIView
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str,DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
# class UserRegistrationAPIView(APIView):
#     def post(self, request):
#         serializer = UserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def get(self, request):
#         users = UserRegistration.objects.all()
#         serializer = UserRegistrationSerializer(users, many=True)
#         return Response(serializer.data)

class LoginApi(APIView):
    def post(self, request):
        try:
            serializer = LoginSerializer(data = request.data)
            if not serializer.is_valid():
               return Response({'error':serializer.errors, "message": "error" ,'status':status.HTTP_400_BAD_REQUEST} )
            return Response( {'data': serializer.get_jwt(request.data)} ,status=status.HTTP_200_OK )
        except Exception as e:
         print(e)
         return Response({'error': "internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
       
      


class UserView(ListCreateAPIView):
    queryset =UserRegistration.objects.all()
    serializer_class = UserRegistrationSerializer
    
    def post(self,request):
      serializer = self.get_serializer(data=request.data)
      if not serializer.is_valid(raise_exception=False):
         return Response({'message':"Sorry, can't create user with these details!" ,"status_code": status.HTTP_406_NOT_ACCEPTABLE, 'errors': serializer.errors})
         

# class LoginView(ListCreateAPIView):
   # queryset = LonginModel.objects.all()
   # serializer_class = LoginSerializer
   # def post(self, request):
   #    try:
   #       serializer = LoginSerializer(data = request.data)
   #       if not serializer.is_valid():
   #          return Response({ "message": serializer.errors} )
   #       return Response( {'data': serializer.get_jwt(request.data),'status_code':status.HTTP_200_OK})
   #    except Exception as e:
   #       print(e)
   #       return Response({'error': "internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class PasswordResetview(GenericAPIView):
    serializer_class = PasswordReSetSerializer
    def post(self,request):
        serializers =  self.serializer_class(data=request.data, context={'request':request})
        if  serializers.is_valid():
            return Response({'mesaage':"A link has been sent your email to reset your password" ,'status_code':status.HTTP_200_OK})
        return Response({'status_code':status.HTTP_400_BAD_REQUEST})


# class PasswordResetConfirm(GenericAPIView):
#     def get(self, request, uidb64,token ):
#         try:
#          user_id = smart_str(urlsafe_base64_decode(uidb64))
#          user =UserRegistration.object.get(id =user_id) 
#          if not PasswordResetTokenGenerator().check_token(user, token):
#                return Response({'message':'Token is invalid','status':status.HTTP_401_UNAUTHORIZED})
#          return Response ({'succes':True,'message':'creditial is valid ', 'uidb64':uidb64 ,'token': token,'status_code':status.HTTP_200_OK}) 

#         except DjangoUnicodeDecodeError:
#             pass   