# Generated by Django 3.2.9 on 2021-12-14 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=200)),
                ('Email_name', models.CharField(max_length=200)),
                ('Phone_number', models.CharField(max_length=100)),
                ('Password', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
