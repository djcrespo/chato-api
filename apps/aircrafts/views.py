from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import Plane, Plane_Model, Time, Service


# Create your views here.
class PlaneViewSet(viewsets.ModelViewSet):

    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer
    permission_classes = [permissions.IsAuthenticated]
    
   
class Plane_ModelViewSet(viewsets.ModelViewSet):

    queryset = Plane_Model.objects.all()
    serializer_class = Plane_ModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class TimeViewSet(viewsets.ModelViewSet):

    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class ServiceViewSet(viewsets.ModelViewSet):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]