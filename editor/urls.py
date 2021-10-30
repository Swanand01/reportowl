from django.urls import path
from . import views

urlpatterns = [
    path('<str:file_id>/', views.editor_view, name='editor_view'),
    path('<str:file_id>/section/<slug:slug>',
         views.section_view, name='section_view'),
    path('<str:file_id>/chapter/<slug:slug>',
         views.chapter_view, name='chapter_view'),
    path('', views.index, name='index'),
]
