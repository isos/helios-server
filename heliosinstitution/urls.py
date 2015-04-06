"""
Institution related urls
Shirlei Chaves (shirlei@gmail.com)

"""

from django.conf.urls import *


from views import *


urlpatterns = patterns('',
    (r'^dashboard$', dashboard),
    (r'^stats$', stats),
    (r'^manage_users$', manage_users),
    (r'^users$', users),
    (r'^admin-actions$', admin_actions),
    (r'^(?P<role>[\w\ ]+)/delegate_user$', delegate_user),
    (r'^(?P<user_pk>\d+)/revoke_user$', revoke_user),
)
