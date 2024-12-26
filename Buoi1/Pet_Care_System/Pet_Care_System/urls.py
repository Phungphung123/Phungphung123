from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('Pet_Care_System_Mng.urls')),
    path('admin/', admin.site.urls),
]