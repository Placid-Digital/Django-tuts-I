# Generated by Django 3.2.9 on 2021-12-16 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grapi', '0002_rename_users_person'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='first_name',
            new_name='name',
        ),
    ]