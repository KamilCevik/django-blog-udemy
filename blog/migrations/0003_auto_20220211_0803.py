# Generated by Django 3.1.5 on 2022-02-11 08:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_yazilarmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yazilarmodel',
            name='icerik',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
