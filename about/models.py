from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class About(models.Model):
    title = RichTextField()

    def __str__(self):
        return self.title