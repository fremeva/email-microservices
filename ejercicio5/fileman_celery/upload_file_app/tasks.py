from django.contrib.auth.models import User

from fileman_celery import celery_app as app
from upload_file_app.models import Document
import pandas as pd
import os
from django.conf import settings


@app.task()
def save_user_upload(document_id):
    doc = Document.objects.get(pk=document_id)
    user = pd.read_excel(os.path.join(settings.MEDIA_ROOT, doc.document.name))
    for idx, row in user.iterrows():
        User.objects.create(**dict(row))

    print('Ok! Finished')
