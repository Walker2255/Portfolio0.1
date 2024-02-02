from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Work(models.Model):
    title = RichTextField()
    time = RichTextField()
    dashboard = RichTextField()
    description = RichTextField()
    myImage = models.FileField(upload_to="works/", max_length=250, null=True, default=None)

    def __str__(self):
        return self.title