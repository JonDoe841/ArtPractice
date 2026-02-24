from django.urls import path, include
from tutorials import views
app_name = 'tutorials'
urlpatterns = [
    path('', views.tutorial_list, name= 'tutorial_list'),
    path('create/', views.create_tutorial, name='create_tutorial'),
    path('category/<int:category_id>/', views.tutorials_by_category, name='by_category'),
    path('<int:pk>/', include([
        path('', views.tutorial_details, name= 'details'),
        path('edit/', views.tutorial_edit, name= 'edit'),
        path('delete/', views.tutorial_delete, name= 'delete'),
    ]))

]
