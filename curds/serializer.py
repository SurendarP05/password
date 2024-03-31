from rest_framework import serializers
from .models import Curd

class CurdSerializer(serializers.ModelSerializer):
    class Meta :
        model = Curd
        fields= '__all__'