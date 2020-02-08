from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>', views.detail, name='detail'),
    path('projects/<str:proj_type>', views.projects, name='projects'),
    path('tag/<str:tag>', views.projects, name='tag'),
]
