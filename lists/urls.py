
from django.conf.urls import url
from lists import views

# in this project, by convention we are using urls without trailing slashes to indicate that this endpoint will modify the database in some way.

urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/$', views.view_list, name='view_list'), 
    url(r'^users/(.+)/$', views.my_lists, name='my_lists'),
    url(r'^(\d+)/share$', views.share_list, name='share_list'),    
]
