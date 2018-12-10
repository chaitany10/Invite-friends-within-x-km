from entries.views import *
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('home/',home),
    path('calculate/',calculate),
    path('admin/', admin.site.urls),
    path('entries/', include('entries.urls')),
]
