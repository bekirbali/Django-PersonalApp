from django.urls import path

from .views import *

urlpatterns = [
    path('departments/', DepartmentListCreateView.as_view()),
    path('departments/<str:pk>/', DepartmentRUDView.as_view()),
    path('personnel/', PersonnelListCreateView.as_view()),
    path('personnel/<str:pk>/', PersonnelRUDView.as_view()),
    
]
