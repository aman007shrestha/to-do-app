from django.urls import path
from . import views


app_name = 'task'
urlpatterns = [
	path('update/<int:pk>/', views.update_task, name='update'),
	path('', views.index, name='index'),
	path('delete/<int:pk>/', views.delete_task, name='delete'),
]