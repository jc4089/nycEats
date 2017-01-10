from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /inspection/
    url(r'^$', views.index, name = 'index'),
    # url(r'^$', views.IndexView.as_view(), name = 'index'),
    # ex: /inspection/1/
    # url(r'^(?P<inspection_id>[0-9]+)/$', views.detail, name = 'detail'),
]