from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import Maintenance, Chapter, Ata, Type_Maintenance


# Create your views here.
class MaintenanceViewSet(viewsets.ModelViewSet):

    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
    permission_classes = [permissions.IsAuthenticated]
    
  
class AtaViewSet(viewsets.ModelViewSet):

    queryset = Ata.objects.all()
    serializer_class = AtaSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class ChapterViewSet(viewsets.ModelViewSet):

    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [permissions.IsAuthenticated]
    
 
 
class Type_MaintenanceViewSet(viewsets.ModelViewSet):

    queryset = Type_Maintenance.objects.all()
    serializer_class = Type_MaintenanceSerializer
    permission_classes = [permissions.IsAuthenticated]
    
  