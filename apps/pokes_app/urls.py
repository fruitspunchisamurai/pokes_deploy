from django.conf.urls import url
from . import views

urlpatterns = [
    #Landing Routes
    url(r'^$', views.index, name="landing"),
    url(r'^success$', views.success, name="success"),
    #Login/Register
    url(r'^create$', views.create, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
    #Friend
    url(r'^friend/(?P<id>\d+)$', views.add_friend, name="add_friend"),
    url(r'^confirm_remove/(?P<id>\d+)$', views.confirm_remove, name="confirm_remove"),
    url(r'^remove_friend/(?P<id>\d+)$', views.remove_friend, name="remove_friend"),
    #Poke
     url(r'^poke/(?P<id>\d+)$', views.poke, name="poke"),
     url(r'^reset_pokes$', views.reset_pokes, name="reset_pokes"),
]