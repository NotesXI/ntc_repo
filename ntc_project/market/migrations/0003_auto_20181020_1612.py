# Generated by Django 2.1.2 on 2018-10-20 16:12

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('market', '0002_auto_20181020_0155'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notes',
            new_name='Note',
        ),
    ]