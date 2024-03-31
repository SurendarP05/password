from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListCreateAPIView
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status


class RegistrationAPIView(ListCreateAPIView):
    queryset = RegistrationModel.objects.all()
    serializer_class = RegistrationSerializer
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(ListCreateAPIView):
   queryset = MyLonginModel.objects.all()
   serializer_class = MyLoginSerializer
   def post(self, request):
      try:
         serializer = MyLoginSerializer(data = request.data)
         if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({ "message": serializer.errors} )
         return Response( {'data': serializer.get_jwt(request.data),'status_code':status.HTTP_200_OK})
      except Exception as e:
         return Response({'error': "internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
class PasswordResetMail(GenericAPIView):
    serializer_class = PasswordReSetMailSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if  serializer.is_valid():
            return Response({'mesaage':"A link has been sent your email to reset your password" ,'status_code':status.HTTP_200_OK})
        return Response({'error':serializer.errors,'status_code':status.HTTP_400_BAD_REQUEST})
    
# class PasswordResetConfirmAPIView(GenericAPIView):
#     queryset = RegistrationModel.objects.all()
#     serializer_class = PasswordResetSerializer
#     def post(self, request, uid, token, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'uid': uid, 'token': token})
#         if serializer.is_valid():
#             print(serializer, "------------------------------------------------------------------------------")
#             serializer.save()
#             return Response({'message': 'Password reset successfully'}, status=200)
#         return Response(serializer.errors, status=400)

class PasswordResetConfirmAPIView(GenericAPIView):
    queryset = RegistrationModel.objects.all()
    serializer_class = PasswordResetSerializer

    def post(self, request, uid, token, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'uid': uid, 'token': token})
        serializer.is_valid(raise_exception=True)  # Use raise_exception=True to raise a validation error
        uid = urlsafe_base64_decode(uid).decode()
        try:
            instance = RegistrationModel.objects.get(pk=uid)
        except RegistrationModel.DoesNotExist:
            return Response({'error': 'Invalid reset link'}, status=400)

        # Pass the instance to the serializer for updating
        serializer.update(instance, serializer.validated_data)

        return Response({'message': 'Password reset successfully'}, status=200)