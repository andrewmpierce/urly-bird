from django.conf.urls import url


from . import views


urlpatterns = [
    url(r'^$', views.new_url, name='new_url'),
    url(r'^stats/(?P<click_short>\w+)$', views.stats_detail, name='stats_detail'),
    url(r'^(?P<click_short>\w+)$', views.short, name='redirect_shorts'),
]
