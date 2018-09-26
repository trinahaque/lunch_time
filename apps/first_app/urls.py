from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^success$', views.success),
    url(r'^successId$', views.successId),
    url(r'^getCoffee$', views.getCoffee),
    # url(r'^getCoffee/(?P<pid>\d+)$', views.getCoffee),
    url(r'^lunch$', views.getLunch),
    url(r'^resetUser$', views.resetUser),
]
