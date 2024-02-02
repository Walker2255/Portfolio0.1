from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title = RichTextField()
    time = RichTextField()
    where = RichTextField()
    description = RichTextField()

    def __str__(self):
        return self.title