from django.conf.urls import url
from . import views
from django.views.generic import ListView
from .models import Click



urlpatterns = [
        url(r'^stats/(?P<click_short>\w+)$', views.stats_detail, name='stats_detail'),
        url(r'^list$', ListView.as_view(model=Click, paginate_by=25), name='click_list'),
        url(r'^(?P<click_short>\w+)$', views.short, name='redirect_shorts'),
        url(r'^clicks.png/(?P<click_pk>\d*)?$', views.stats_chart, name="stats_chart"),
        url(r'^user/(?P<username>\w+)$', views.user_table, name='user_table'),
        url(r'^$', views.index, name='index')

]
