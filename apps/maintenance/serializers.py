from django.contrib.auth.models import Group
from .models import *
from rest_framework import serializers


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'
       
       
class AtaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ata
        fields = '__all__'
        
         
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'
        
              
class Type_MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_Maintenance
        fields = '__all__'

       