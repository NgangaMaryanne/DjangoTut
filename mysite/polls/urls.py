from django.conf.urls import url
from . import views
urlpatterns = [
    #urls for the polls app.
    url(r'^$', views.index, name='index'),
]
