# Generated by Django 3.1.5 on 2022-02-12 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220212_0339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yorummodel',
            old_name='guncellenme_tarihi',
            new_name='duzenleme_tarihi',
        ),
    ]