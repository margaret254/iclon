from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.new_post,name='newpost'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^post/(\d+)',views.post,name ='post')

]