# Generated by Django 3.2.9 on 2021-11-25 12:20

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
                ('last_name', models.CharField(max_length=100)),
                ('Email_name', models.CharField(max_length=200)),
                ('Password', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
