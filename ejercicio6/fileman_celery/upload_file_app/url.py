from django.conf.urls import url
from .views import model_form_upload

app_name = 'uloploadapp'
urlpatterns = [
    url(r'^$', model_form_upload, name='upload'),
]
