from django.contrib import admin
from django.urls import path, include
from devices.urls import urlpatterns as devices

urlpatterns = [
    path("admin/", admin.site.urls),
    path('devices/', include(devices))
]