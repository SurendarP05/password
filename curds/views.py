from django.forms import ValidationError
from rest_framework import status
from django.http import HttpResponse
from rest_framework.views import exception_handler
from rest_framework.response import Response
from django.db import IntegrityError
from django.db import OperationalError
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework import generics,mixins
from rest_framework import viewsets
from.serializer import CurdSerializer
from.models import Curd


def custom_exception_handler(exc, context):
   
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code

    return response


class CurdListView(generics.GenericAPIView, 
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin,):
                        #   mixins.RetrieveModelMixin,
                        #   mixins.DestroyModelMixin,
                        #   mixins.UpdateModelMixin,
                        #   ):
    
    serializer_class = CurdSerializer
    queryset=Curd.objects.all()
    lookup_field = 'id'

    def get(self,request, id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
#     def perform_create(self, serializer ):
#      queryset = Curd.objects.filter(name=self.request.user)
#      if queryset.exists():
#         raise ValidationError('You have already signed up')
#      serializer.save(name=self.request.user)
    
#     def put(self,request,id=None):
#         return self.update(request,id)
    
#     def delete(self,request,id=None):
#         return self.destroy(request,id)
    
    
    
# class CreationDetail(APIView):
#     def post(self, request):
#      createdata = CurdSerializer(data=request.data)
#      if createdata.is_valid(): 
#           createdata.save()
#           return Response({'message':'data created'},status=status.HTTP_201_CREATED)
#      return Response({'message':'error'},status=status.HTTP_400_BAD_REQUEST)
    
# class DetailInfo(APIView):
#    def get(self,request):
#       user = Curd.objects.all()
#       getinfo= CurdSerializer(user, many=True)
#       return Response({'data':getinfo.data,'message': 'data recived'})
   
# class UpdateDetail(APIView):
#     def put(self,request,id):
#       try:
#         user = Curd.objects.get(id=id)
#       except Curd.DoesNotExist:
#           msg ={"msg":"not found Error"}
#           return Response( msg,status=status.HTTP_404_NOT_FOUND)
#       putdata = CurdSerializer(user,data=request.data)
#       if putdata.is_valid():
#          putdata.save()
#          return Response({'message':'Requried Data is Update  '},status=status.HTTP_205_RESET_CONTENT)
#       return Response({'message':'error'},status=status.HTTP_400_BAD_REQUEST)

# class DeleteDetail(APIView):
#     def delete(self,request,id):
#       try:
#             user = Curd.objects.get(id=id)
#       except Curd.DoesNotExist:
#          return Response({'message':'error'},status=status.HTTP_400_BAD_REQUEST)
#       user.delete()
#       return Response( {'message':'Data was deleted'},status=status.HTTP_204_NO_CONTENT,)
    
# class RetriveData(RetrieveAPIView):
#        queryset = Curd.objects.all()
#        serializer_class = CurdSerializer
    

# class curdViwset(viewsets.ModelViewSet):
#     serializer_class = CurdSerializer
#     queryset=Curd.objects.all()
#     lookup_field = 'id'
class CurdDestroyListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curd.objects.all()
    serializer_class = CurdSerializer
    lookup_field = 'id'
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({'message': 'Object deleted successfully', 'status':status.HTTP_204_NO_CONTENT})
        except Curd.DoesNotExist:
           return Response({'message':'user not found', 'ststus':status.HTTP_404_NOT_FOUND})
        except IntegrityError :
            return Response({'error': 'Cannot delete this object because it is referenced by other objects', 'status':status.HTTP_409_CONFLICT})
        # except :           
        