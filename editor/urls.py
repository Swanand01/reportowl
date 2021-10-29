from django.urls import path
from . import views

urlpatterns = [
    path('<str:file_id>/', views.editor_view, name='editor_view'),
    path('', views.index, name='index'),
]
