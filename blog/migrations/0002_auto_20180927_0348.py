# Generated by Django 2.0.8 on 2018-09-27 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='creted_date',
            new_name='created_date',
        ),
    ]
