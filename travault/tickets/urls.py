from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),
    path('create/', views.ticket_create, name='ticket_create'),
    path('<int:ticket_id>/', views.ticket_view, name='ticket_view'),
    path('<int:ticket_id>/edit/', views.ticket_view_edit, name='ticket_view_edit'),
    path('<int:ticket_id>/update/add/', views.ticket_add_update, name='ticket_add_update'),
    path('<int:ticket_id>/update/<int:update_id>/edit/', views.ticket_update_edit, name='ticket_update_edit'),
    path('<int:ticket_id>/delete/', views.ticket_delete, name='ticket_delete'),
]