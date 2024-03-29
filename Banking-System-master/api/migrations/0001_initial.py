# Generated by Django 2.2.13 on 2021-12-22 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('community', models.CharField(default=None, max_length=15)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('time', models.TimeField(default=None)),
                ('category', models.CharField(max_length=25)),
                ('mode', models.CharField(choices=[('phy', 'Physical'), ('on', 'Online')], max_length=3)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'events',
            },
        ),
    ]
