from django.urls import path

from . import views

urlpatterns = [
    path('GetPropertyData', views.getPropertyData, name='getPropertyData'),
    path('rentEstimate/<str:location>', views.getRentEstimate, name='getRentEstimate'),
]