from django.urls import path
from . import views

urlpatterns = [
    path('', views.company_list, name='company_list'),
    path('<int:company_id>/', views.company_detail, name='company_detail'),
    path('add/', views.company_add, name='company_add'),
    path('<int:company_id>/edit/', views.company_edit, name='company_edit'),
    path('<int:company_id>/delete/', views.company_delete, name='company_delete'),
    path('<int:company_id>/activity-log/', views.company_activity_log, name='company_activity_log'),
    path('<int:company_id>/notes/', views.company_notes, name='company_notes'),
    path('<int:company_id>/notes/add/', views.company_notes_add, name='company_notes_add'),
    path('<int:company_id>/notes/<int:note_id>/edit/', views.company_notes_edit, name='company_notes_edit'),
    path('<int:company_id>/notes/<int:note_id>/delete/', views.company_notes_delete, name='company_notes_delete'),
]