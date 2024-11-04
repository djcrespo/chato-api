from django.contrib.auth.models import Group
from .models import *
from rest_framework import serializers


class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = '__all__'
        
        
class Model_EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model_Engine
        fields = '__all__'      


        
        
        