from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('plot/<str:plotId>', views.plot, name='plot'),
]
