from django.conf.urls import patterns, url
from admin_utils import make_admin_class

make_admin_class("Status", patterns('uwsgi_admin.views',
    url(r'^$', 'index', name='uwsgi_status_changelist'),
    url(r'^reload/$', 'reload', name='uwsgi_reload')
), "uwsgi")
