from django.conf.urls import url
from . import views
# . -> current directory/package

urlpatterns = [
    # path("flights", views.index) - for django v2
    url(r'^flights/', views.index, name="index"),
    url(r'^flight/(?P<flight_id>\d+)/$', views.flight, name="flight"),
    url(r'^book/(?P<flight_id>\d+)/$', views.book, name="book"),
    
]