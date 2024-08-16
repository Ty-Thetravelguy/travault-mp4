from django.urls import path
from . import views

urlpatterns = [
    path('', views.company_list, name='company_list'),
    path('<int:company_id>/', views.company_detail, name='company_detail'),
    path('create/', views.company_create, name='company_create'),
    path('<int:company_id>/update/', views.company_update, name='company_update'),
    path('<int:company_id>/delete/', views.company_delete, name='company_delete'),
]