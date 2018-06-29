from django.db import models



# Create your models here.
class Document(models.Model):
    info = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents')

    @property
    def get_name(self):
        directory, name = self.document.name.split('/')
        return name
