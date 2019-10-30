from django.urls import path

# bring in the views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]
