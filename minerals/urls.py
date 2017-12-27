from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.mineral_first_search, name='home_page'),
    url(r'detail/(?P<pk>\d+)/$', views.mineral_detail, name='mineral_detail'),
    url(r'search/name$', views.mineral_name_search, name='mineral_name_search'),
    url(r'search/letter/(?P<letter>[a-zA-Z])/$', views.mineral_first_search, name='mineral_first_search'),
    url(r'search/group/(?P<group>[a-zA-Z\s]+)/$', views.mineral_group_search, name='mineral_group_search'),
]
