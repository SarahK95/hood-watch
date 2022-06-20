from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name= 'home'),
    url(r'^create/profile$',views.create_profile, name='create-prof'),
    url(r'^post',views.post, name='post'),
    url(r'^businesses',views.businesses, name='businesses'),
    url(r'^health',views.health, name='health'),
    url(r'^police',views.police, name='police'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^update/profile$',views.update_profile, name='update-profile'),
    url(r'^new/business$',views.new_biz, name='new-biz'),
    url(r'^new/post$',views.new_post, name='new-post'),
    url(r'^user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),
    url(r'^my-profile/',views.my_prof, name='my-prof'),
    url(r'^view/blog/(\d+)',views.view_post,name='view_post'),
   
 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)