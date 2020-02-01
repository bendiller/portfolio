from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tag/<str:tag>', views.index, name='tag'),
    path('<str:name>', views.detail, name='detail'),
]
