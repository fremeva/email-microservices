from django.shortcuts import render, redirect
from .tasks import generate_report, send_email, removefile


# Create your views here.
def index(request):
    if request.method == 'POST':
        (generate_report.s() | send_email.s() | removefile.s())()
        redirect('/reports/')

    return render(request, 'reports/index.html', {})
