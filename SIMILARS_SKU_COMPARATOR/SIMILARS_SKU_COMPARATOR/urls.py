from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'SIMILARS_SKU_COMPARATOR.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^comparator/', include('comparator.urls',namespace="comparator")),
    url(r'^admin/', include(admin.site.urls)),
]
