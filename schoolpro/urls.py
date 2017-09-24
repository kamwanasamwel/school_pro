
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^student/', include('studentbasic.urls',
                           namespace='studentbasic',
                           app_name='studentbasic')),
    url(r'^signup/', include('core.urls', namespace='core', app_name='core')),
]
