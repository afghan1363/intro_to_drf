from rest_framework import viewsets, generics
from vehicle.serializers import (CarSerializer, MotoSerializer, MilageSerializer, MotoMilageSerializer,
                                 MotoCreateSerializer)
from vehicle.models import Car, Moto, Milage
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from vehicle.permissions import IsOwnerOrStaff
from vehicle.paginators import VehiclePaginator
from vehicle.tasks import check_milage


# Create your views here.
class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = (AllowAny,)


class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        new_moto = serializer.save()
        new_moto.owner = self.request.user
        new_moto.save()


class MotoListAPIView(generics.ListAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()
    pagination_class = VehiclePaginator


class MotoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()
    permission_classes = (IsOwnerOrStaff,)


class MotoDestroyAPIView(generics.DestroyAPIView):
    queryset = Moto.objects.all()


class MilageCreateAPIView(generics.CreateAPIView):
    serializer_class = MilageSerializer

    def perform_create(self, serializer):
        new_milage = serializer.save()
        if new_milage.car:
            check_milage.delay(pk=new_milage.car_id, model='Car')
        else:
            check_milage.delay(pk=new_milage.moto_id, model='Moto')


class MilageListAPIView(generics.ListAPIView):
    serializer_class = MilageSerializer
    queryset = Milage.objects.all()
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('car', 'moto')
    ordering_fields = ('year',)


class MilageDestroyAPIView(generics.DestroyAPIView):
    queryset = Milage.objects.all()


class MotoMilageListAPIView(generics.ListAPIView):
    queryset = Milage.objects.filter(moto__isnull=False)
    serializer_class = MotoMilageSerializer
