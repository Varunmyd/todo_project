# Generated by Django 4.1.2 on 2022-10-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2000-07-11'),
            preserve_default=False,
        ),
    ]
