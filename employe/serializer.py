from rest_framework import serializers
from curds.serializer import CurdSerializer
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    bio = CurdSerializer()

    class Meta:
        model = EmployeeModel  
        fields = ['bio', 'phoneno', 'job_description', ]

class SalarySerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer() 

    class Meta:
        model = SalaryModel
        fields = [ 'employee', 'basic_sal', 'epf', 'net_sal']
      