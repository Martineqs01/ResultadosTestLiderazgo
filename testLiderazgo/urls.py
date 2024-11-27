from django.urls import path
from .views import home, reporte, estadGen

urlpatterns = [
    path('', home, name='home'),
    path('reporte/', reporte, name='reporte'),
    path('estadGen/', estadGen, name='estadGen'),

]
