from django.urls import path

from .import views

app_name = 'salon'

urlpatterns = [
    path('', views.salon_listes, name='list'),
    path('<int:num_salon>', views.salon_detail, name='detail'),
    path('filter/<str:name>/', views.salon_filter, name='filter'),
    path('filterses/<str:names>/', views.salon_filter, name='filter'),
] 
