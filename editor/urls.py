from django.urls import path
from . import views

urlpatterns = [
    path('<str:file_id>/', views.editor_view, name='editor_view'),
    path('<str:file_id>/<slug:chapter_slug>/section/<slug:section_slug>',
         views.section_view, name='section_view'),
    path('<str:file_id>/chapter/<slug:slug>',
         views.chapter_view, name='chapter_view'),
    path('', views.index, name='index'),
    path('<str:file_id>/<slug:chapter_slug>/section',
         views.new_section_view, name='new_section_view'),
]
