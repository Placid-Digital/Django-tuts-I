# Generated by Django 3.2.5 on 2021-12-07 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0009_alter_userbankaccount_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbankaccount',
            name='account_no',
            field=models.PositiveIntegerField(default='9130509138', unique=True),
        ),
    ]