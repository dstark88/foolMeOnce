from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'materials'

urlpatterns = [
    # ex: /materials/
    # path('', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.about),
    url(r'^article/$', views.article),
    url(r'^$', views.homepage),

]