
from django.conf.urls import url
from lists import views

# in this project, by convention we are using urls without trailing slashes to indicate that this endpoint will modify the database in some way.

urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/$', views.view_list, name='view_list'),    
]
