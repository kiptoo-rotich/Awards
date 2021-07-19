from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('accounts/profile/',views.profile,name='profile'),
    path('logout/', views.logout, name='logout'), 
    path('new_project',views.newProject,name='new_project'),
    path('search/',views.search_results,name='search'),
    path('reviews/<id>/',views.reviews,name = 'reviews'),
    path('update/',views.updateprofile,name = 'updateprofile'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('api/projects',views.ProjectsList.as_view()),
    path('api-token-auth/', obtain_auth_token)

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
