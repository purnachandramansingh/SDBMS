from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.signin, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/$', views.signin, name="signin"),
    url(r'^register/$', views.register, name="signin"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]