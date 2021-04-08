from django.db import models
from django.conf import settings
from django.conf.urls.static import static


class files(models.Model):
    id = models.AutoField(primary_key=True)
    attachment = models.FileField(upload_to="pdf/", blank=True)

    
    def __str__(self):
        return f"{self.attachment}"