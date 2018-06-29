from django import forms

from upload_file_app.models import Document
from upload_file_app.tasks import save_user_upload


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'

    def save(self, commit=True):
        doc = super(DocumentForm, self).save(commit=commit)
        save_user_upload.delay(doc.pk)
        return doc
