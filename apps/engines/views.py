from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import Engine, Model_Engine


# Create your views here.
class EngineViewSet(viewsets.ModelViewSet):

    queryset = Engine.objects.all()
    serializer_class = EngineSerializer
    permission_classes = [permissions.IsAuthenticated]
    
   
class Model_Engine_OneViewSet(viewsets.ModelViewSet):

    queryset = Model_Engine.objects.all()
    serializer_class = Model_EngineSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    



   