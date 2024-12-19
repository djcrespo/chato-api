from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import *
from .models import Plane, Plane_Model, Time, Service

# other models
from apps.propellers.models import *
from apps.engines.models import *


# Create your views here.
class PlaneViewSet(viewsets.ModelViewSet):

    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        data = request.data

        enginers_data = data.pop('enginers')
        proppellers_data = data.pop('proppellers')
        plane_model_id = data.pop('model')
        plane_model_instance = Plane_Model.objects.get(id=plane_model_id)
        
        plane_instance = Plane.objects.create(
            model=plane_model_instance,
            **data
        )
        
        """
        for engine in enginers_data:
            model_engine_id = engine.pop('model_engine')
            model_engine_instance = Model_Engine.objects.get(id=model_engine_id)
            engine_instance = Engine.objects.create(
                engine_model=model_engine_instance,
                **engine
            )
            plane_instance.enginers.add(engine_instance)
            plane_instance.save()
        
        for proppeller in proppellers_data:
            model_proppeller_id = proppeller.pop('model_proppeller')
            proppeller_model_instance = Model_Propeller.objects.get(id=model_proppeller_id)
            proppeller_instance = Propeller.objects.create(
                propeller_model=proppeller_model_instance,
                **proppeller
            )
            plane_instance.propellers.add(proppeller_instance)
            plane_instance.save()
        """
            
        return Response(
            PlaneSerializer(plane_instance).data,
            status=status.HTTP_201_CREATED
        )
    
   
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