from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'detail/(?P<pk>\d+)/$', views.mineral_detail, name='mineral_detail'),
]