# Generated by Django 4.2.4 on 2023-08-27 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useralert',
            old_name='device_id',
            new_name='user_id',
        ),
    ]
