# Generated by Django 2.1.2 on 2018-11-09 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyPurchases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes_id', models.IntegerField(default=0, unique=True)),
            ],
        ),
    ]
