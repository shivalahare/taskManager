from django.urls import path
from . import views

urlpatterns = [
    # Other URLs for tasks
    path('', views.taskList, name='taskList'),
    path('create/', views.createTask, name='createTask'),
    path('update/<int:pk>/', views.updateTask, name='updateTask'),
    path('delete/<int:pk>/', views.deleteTask, name='deleteTask'),
    
    # Auth URLs
    path('signup/', views.signup, name='signup'),
]
