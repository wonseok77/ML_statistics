from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.view_Test),  
    path('dbtesrt/', views.view_DB_Test),
    path('createTable/', views.createTable),
]
