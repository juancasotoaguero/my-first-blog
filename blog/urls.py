from django.conf.urls import  url
from . import views


urlpatterns = [
               
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name="post_new"),
    url(r'^about/$',views.about_us, name="about_us"),
    url(r'^contact/$', views.contact_form, name="contact_form"),

]
