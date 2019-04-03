from django.conf.urls import url
from . import views
urlpatterns=[
    url('blog',views.list_of_post,name='list_of_post'),
    url(r'^(?p<slug>[\w]+)/$',views.post_detail,name='post_detail')
]