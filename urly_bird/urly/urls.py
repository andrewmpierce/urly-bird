from django.conf.urls import url
from . import views
from django.views.generic import ListView
from .models import Click



urlpatterns = [
        url(r'^login', views.user_login, name='login'),
        url(r'^logout', views.user_logout, name='logout'),
        url(r'^profile/(?P<username>\w+)', views.user_profile, name='profile'),
        url(r'^register', views.user_register, name='register'),
        url(r'^stats/(?P<click_short>\w+)$', views.stats_detail, name='stats_detail'),
        #url(r'^list$', ListView.as_view(model=Click, paginate_by=25), name='click_list'),
        url(r'^list$', views.list_clicks, name='click_list'),
        url(r'^(?P<click_short>\w+)$', views.short, name='redirect_shorts'),
        url(r'^delete/(?P<click_pk>\d+)$', views.click_delete, name='click_delete'),
        url(r'^edit/(?P<click_pk>\d+)$', views.click_edit, name='click_edit'),
        url(r'^clicks.png/(?P<click_pk>\d*)?$', views.stats_chart, name="stats_chart"),
        url(r'^user/stats/(?P<username>\w+)$', views.user_table, name='user_table'),
        #url(r'^list/(?P<username>\w+)$'), views.
        url(r'^$', views.index, name='index')

]
