# Generated by Django 3.0.7 on 2020-07-04 07:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('geometry', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('temperature', models.FloatField(default=10.1)),
            ],
            options={
                'verbose_name_plural': 'cities',
                'ordering': ('name',),
            },
        ),
    ]
