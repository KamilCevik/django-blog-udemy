# Generated by Django 3.1.5 on 2022-02-12 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_iletisimmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iletisimmodel',
            options={'verbose_name': 'İletişim', 'verbose_name_plural': 'İletişim'},
        ),
        migrations.AlterModelTable(
            name='iletisimmodel',
            table='iletisim',
        ),
    ]