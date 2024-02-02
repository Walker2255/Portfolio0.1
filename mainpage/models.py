from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Main(models.Model):
    title = RichTextField()
    description = RichTextField()
    myImage = models.FileField(upload_to="mainpage/", max_length=250, null=True, default=None)

    def __str__(self):
        return self.title
