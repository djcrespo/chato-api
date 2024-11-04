from django.contrib.auth.models import Group
from .models import *
from rest_framework import serializers


class PropellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propeller
        fields = '__all__'
        
        
class Model_PropellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model_Propeller
        fields = '__all__'      
