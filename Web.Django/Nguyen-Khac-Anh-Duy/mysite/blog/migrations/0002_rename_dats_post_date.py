# Generated by Django 4.1.7 on 2023-05-20 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='dats',
            new_name='date',
        ),
    ]