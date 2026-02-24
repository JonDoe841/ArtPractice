from django.urls import path
from categories import views

app_name = 'categories'

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('add/', views.add_category, name='add_category'),
    path('<int:pk>/', views.category_detail, name='detail'),
    path('<int:pk>/edit/', views.category_edit, name='edit'),
    path('<int:pk>/delete/', views.category_delete, name='delete'),
]