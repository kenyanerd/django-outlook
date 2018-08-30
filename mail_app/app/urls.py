from django.conf.urls import url
from app import views

app_name = 'app'
urlpatterns = [
    # The home view ('/app/')
    url(r'^$', views.home, name='home'),
    # Explicit home ('/app/home/')
    url(r'^home/$', views.home, name='home'),
    # Redirect to get token ('/app/gettoken/')
    url(r'^gettoken/$', views.gettoken, name='gettoken'),
]
