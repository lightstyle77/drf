# Generated by Django 3.2.8 on 2021-11-25 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20210914_0957'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['pk']},
        ),
    ]
