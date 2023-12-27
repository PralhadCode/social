from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home_view, name='home_view'),
    path('', views.contact_view, name='contact_view')
]
