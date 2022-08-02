from django.urls import include, path

from . import views

urlpatterns = [
    path('delete/', views.delete),
    path('update/', views.update),
    path('show4/', views.show4),
    path('show3/', views.show3),
    path('show2/', views.show2),
    path('oneshow/', views.oneshow),
    path('show/', views.show),
    path('insert/', views.insert),
    path('index6/', views.index6),
    path('index3/', views.index3),
    path('main/', views.main),
]
