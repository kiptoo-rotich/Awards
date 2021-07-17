from django.conf import settings
from django.urls import path
from django.contrib.auth import views


from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('accounts/profile/',views.profile,name='profile'),
    path('logout/', views.logout, name='logout'), 
    path('awards/projects/',views.newProject,name='projects')
]