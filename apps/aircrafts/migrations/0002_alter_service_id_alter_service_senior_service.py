# Generated by Django 5.0.6 on 2024-11-11 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aircrafts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='service',
            name='senior_service',
            field=models.IntegerField(max_length=60),
        ),
    ]
