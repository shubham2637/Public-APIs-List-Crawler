# Generated by Django 3.0.6 on 2020-05-23 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='api_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('API', models.TextField()),
                ('link', models.URLField()),
                ('Description', models.TextField()),
                ('HTTPs', models.CharField(max_length=3)),
                ('CORS', models.CharField(max_length=3)),
                ('Category', models.CharField(max_length=100)),
            ],
        ),
    ]
