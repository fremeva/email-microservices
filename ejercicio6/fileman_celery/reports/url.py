from django.conf.urls import url
from .views import index

app_name = 'reportsapp'
urlpatterns = [
    url(r'^$', index, name='index')
]
