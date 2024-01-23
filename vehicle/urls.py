from rest_framework.routers import DefaultRouter
from vehicle.views import (CarViewSet, MotoCreateAPIView, MotoListAPIView, MotoRetrieveAPIView, MotoUpdateAPIView,
                           MotoDestroyAPIView, MilageCreateAPIView, MilageDestroyAPIView, MotoMilageListAPIView,
                           MilageListAPIView)
from django.urls import path

app_name = 'vehicle'
router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')
urlpatterns = [
    path('moto/create/', MotoCreateAPIView.as_view(), name='moto_create'),
    path('moto/', MotoListAPIView.as_view(), name='moto_list'),
    path('moto/detail/<int:pk>/', MotoRetrieveAPIView.as_view(), name='moto_detail'),
    path('moto/update/<int:pk>/', MotoUpdateAPIView.as_view(), name='moto_update'),
    path('moto/delete/<int:pk>/', MotoDestroyAPIView.as_view(), name='moto_delete'),

    path('milage/', MilageListAPIView.as_view(), name='milage'),
    path('milage/create/', MilageCreateAPIView.as_view(), name='milage_create'),
    path('milage/delete/<int:pk>/', MilageDestroyAPIView.as_view(), name='milage_delete'),
    path('moto/milage/', MotoMilageListAPIView.as_view(), name='moto_milage'),
] + router.urls
