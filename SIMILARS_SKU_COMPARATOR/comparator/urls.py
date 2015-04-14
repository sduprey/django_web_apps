
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details$', views.details, name='details'),
    url(r'^(?P<sku_id>\w+)/results$', views.results, name='results'),
]