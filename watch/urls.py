from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name= 'home'),
    url(r'^create/profile$',views.create_profile, name='create-profile'),
    url(r'^post',views.post, name='post'),
    url(r'^businesses',views.businesses, name='businesses'),
   
 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)