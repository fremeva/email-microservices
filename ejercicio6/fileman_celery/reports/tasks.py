import xlsxwriter
from celery import current_app as app
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
import os

HEADERS = ['id',
           'last_login',
           'is_superuser',
           'username',
           'first_name',
           'last_name',
           'email',
           'is_staff',
           'is_active',
           'date_joined',
           ]


@app.task
def generate_report():
    dir_file = 'temps/report_user.xlsx'
    workbook = xlsxwriter.Workbook(dir_file, {'remove_timezone': True, 'default_date_format': 'dd/mm/yy'})
    worksheet = workbook.add_worksheet()

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': 1})

    # Write some data headers.
    for col in range(len(HEADERS)):
        worksheet.write(0, col, HEADERS[col], bold)

    users = User.objects.filter(is_active=1)
    for row, user in enumerate(users, start=1):
        for col in range(len(HEADERS)):
            worksheet.write(row, col, user.__dict__[HEADERS[col]])

    workbook.close()
    return dir_file


@app.task
def send_email(filepath):
    e = EmailMessage('Reportes', 'Cuerpo del mensaje {}'.format(filepath),
                     to=['fredylsvprueba@gmail.com', 'fredymv03@gmail.com'])
    e.attach_file(filepath)  # Adjuntamos el archivo a enviar.
    e.send()

    return filepath


@app.task
def removefile(route):
    os.remove(route)
    return 'Archivo borrado!!'
