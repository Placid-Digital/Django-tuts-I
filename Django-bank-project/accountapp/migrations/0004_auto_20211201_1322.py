# Generated by Django 3.2.9 on 2021-12-01 13:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0003_auto_20211201_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moneytransfer',
            name='closing_balance',
        ),
        migrations.AlterField(
            model_name='userbankaccount',
            name='account_no',
            field=models.PositiveIntegerField(default='9440813056', unique=True),
        ),
        migrations.AlterField(
            model_name='userbankaccount',
            name='contact',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
