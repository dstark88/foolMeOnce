from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^articles/$', views.articles, name='articles'),
    # url(r'^articles/(?P<pk>\d+)$'),
]
