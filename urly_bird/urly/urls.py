from django.conf.urls import url
from .models import Click
from django.views.generic import ListView

from . import views


urlpatterns = [

url(r'^$', views.new_short_url, name='homepage'),
url(r'^list$', views.click_detail, name='click_detail'),
URL(r'^', include('django.contrib.auth.urls')),
url(r'^stats/(?P<click_short>\w+)$', views.stats_detail, name='stats_detail'),
url(r'^(?P<click_short>\w+)$', views.short, name='redirect_shorts'),
url(r'^clicks.png/(?P<click_pk>\d*)?$', views.stats_chart, name="stats_chart"),
url(r'^user/(?P<username>\w+)$', views.user_table, name='user_table'),
]
