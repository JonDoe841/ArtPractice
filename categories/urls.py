from django.urls import path, include

app_name = 'categories'
from categories import views
urlpatterns = [
    path('',views.category_list,name= 'category_list'),
    path('add/', views.add_category, name='add_category'),
    path('<int:pk>/', include([
        path('', views.category_detail, name='detail'),
        path('edit/', views.category_edit, name='edit'),
        path('delete/', views.category_delete, name='delete'),
    ])),
]
