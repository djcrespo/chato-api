from django.contrib.auth.models import Group
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' #retornar los atributos
        

class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'address', 'license', 'role']
        depth = 3  #acceder a subniveles de informacion  
