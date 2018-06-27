import sys
from django.conf import settings
from django.core.mail import EmailMessage

settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    EMAIL_HOST='smtp.gmail.com',
    EMAIL_USE_TLS=True,
    EMAIL_PORT=587,
    EMAIL_HOST_USER='fredylsvprueba@gmail.com',
    EMAIL_HOST_PASSWORD='prueba123456789'

)
from django.conf.urls import url
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World')


urlpatterns = (
    url(r'^$', index),
)


def send_email(subject='test', body='', to=''):
    e = EmailMessage(subject, body, to=to)
    e.send()
    return 'Ok, Enviado!'
