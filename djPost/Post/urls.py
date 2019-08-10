from django.urls import path,
from djPost.Post import views

urlpatterns = [
	path('', views.home, name='home'),
	path('posts/', views.home, name='home'),
    path('createform/', views.create_blogform, name='create_blogform'),
    path('createview/', views.createform, name='create_form'),  
]
 
