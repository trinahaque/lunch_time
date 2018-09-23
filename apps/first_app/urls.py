from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^success$', views.success),
    url(r'^successId$', views.successId),
    url(r'^coffee$', views.getCoffee),
    url(r'^lunch$', views.getLunch),
    url(r'^resetUser$', views.resetUser),
]
