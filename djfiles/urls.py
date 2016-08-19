from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<filename>\w+)/$', views.get_file),
]
