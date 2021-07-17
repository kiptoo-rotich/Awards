from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('accounts/profile/',views.profile,name='profile'),
    path('logout/', views.logout, name='logout'), 
    path('new_project',views.newProject,name='new_project')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
