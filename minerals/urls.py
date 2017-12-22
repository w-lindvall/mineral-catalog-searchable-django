from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'detail/(?P<pk>\d+)/$', views.mineral_detail, name='mineral_detail'),
    url(r'search/name$', views.mineral_name_search, name='mineral_name_search'),
    url(r'search/first$', views.mineral_first_search, name='mineral_first_search'),
    url(r'search/group/$', views.mineral_group_search, name='mineral_group_search'),
]
