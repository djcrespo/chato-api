# Generated by Django 5.0.6 on 2024-10-24 04:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plane_Model',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('senior_service', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('time', models.IntegerField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('tuition', models.CharField(max_length=60)),
                ('type_tuition', models.CharField(max_length=60)),
                ('series', models.CharField(max_length=60)),
                ('model', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='aircrafts.plane_model')),
                ('senior_service', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='aircrafts.service')),
                ('time', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='aircrafts.time')),
            ],
        ),
    ]
