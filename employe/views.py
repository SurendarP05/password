from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from . models import *
from .serializer import *


class EmployeeApiView(generics.ListAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
class DeleteEmployee(generics.RetrieveDestroyAPIView):
     queryset = EmployeeModel.objects.all()
     serializer_class = EmployeeSerializer
     lookup_field = "id"
     def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({'message': 'Object deleted successfully', 'status':status.HTTP_204_NO_CONTENT})
        except IntegrityError :
            return Response({'error': 'Cannot delete this object because it is referenced by other objects', 'status':status.HTTP_409_CONFLICT})
    

class SalaryApiview(generics.ListAPIView):
    queryset = SalaryModel.objects.all()
    serializer_class =SalarySerializer

class DeleteSalary(generics.RetrieveDestroyAPIView):
    queryset = SalaryModel.objects.all()
    serializer_class =SalarySerializer
    lookup_field = "id"

