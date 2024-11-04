from django.contrib.auth.models import Group
from .models import *
from rest_framework import serializers


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = '__all__'
        
        
class Plane_ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane_Model
        fields = '__all__'      

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'     
        
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'    