# Generated by Django 3.1.2 on 2021-03-15 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysisapp', '0002_data_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='data',
            name='created',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='data',
            name='inprogress',
            field=models.BooleanField(default=False),
        ),
    ]
