from django.urls import path
from . import views

urlpatterns = [
    path('Pet_Care_System_Mng/', views.index, name='Customer'),
]