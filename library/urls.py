from django.urls import path
from . import views

urlpatterns = [
    path('', views.research_list, name='research_list'),
    path('add/', views.add_research, name='add_research'),
]
