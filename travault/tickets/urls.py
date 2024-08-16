from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),
    path('<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('create/', views.ticket_create, name='ticket_create'),
    path('<int:ticket_id>/update/', views.ticket_update, name='ticket_update'),
    path('<int:ticket_id>/close/', views.ticket_close, name='ticket_close'),
]