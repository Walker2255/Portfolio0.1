# Generated by Django 4.2.7 on 2023-11-23 17:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_alter_main_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='title',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
