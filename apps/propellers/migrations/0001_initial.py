# Generated by Django 5.0.6 on 2024-11-11 01:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model_Propeller',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('propeller_model', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Propeller',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('series', models.CharField(max_length=60)),
                ('time', models.IntegerField(max_length=60)),
                ('senior_service', models.IntegerField(max_length=60)),
                ('propeller_model', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='propellers.model_propeller')),
            ],
        ),
    ]
