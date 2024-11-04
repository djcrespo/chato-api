from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import Propeller, Model_Propeller


# Create your views here.
class PropellerViewSet(viewsets.ModelViewSet):

    queryset = Propeller.objects.all()
    serializer_class = PropellerSerializer
    permission_classes = [permissions.IsAuthenticated]
    
   
class Model_PropellerViewSet(viewsets.ModelViewSet):

    queryset = Model_Propeller.objects.all()
    serializer_class = Model_PropellerSerializer
    permission_classes = [permissions.IsAuthenticated]
    