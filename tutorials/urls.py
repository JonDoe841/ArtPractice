from django.urls import path, include
from tutorials import views
app_name = 'tutorial'
urlpatterns = [
    path('', views.tutorial_list, name= 'tutorial_list'),
    path('add/', views.tutorial_add, name= 'add'),
    path('<int:pk>/', include([
        path('', views.tutorial_details, name= 'details'),
        path('edit/', views.tutorial_edit, name= 'edit'),
        path('delete/', views.tutorial_delete, name= 'delete'),
    ]))

]
