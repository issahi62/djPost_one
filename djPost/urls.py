from django.contrib import admin
from django.urls import path, re_path, include
from djPost.Post import views

urlpatterns = [
    path('', views.home, name='home'),
	path('posts/', views.home, name='home'),
    path('createform/', views.create_blogform, name='create_blogform'),
    path('createview/', views.createform, name='create_form'), 
    path('admin/', admin.site.urls),
    re_path(r'^(?P<slug>\w+)/update$', views.post_update, name='detail_update'),
    re_path(r'^(?P<slug>\w+)/delete$', views.post_delete, name='post_delete'),
	re_path(r'^(?P<slug>\w+)/$', views.detail_blog, name='detail_blog'),
]
 
