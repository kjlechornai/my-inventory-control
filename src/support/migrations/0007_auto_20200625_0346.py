# Generated by Django 3.0.6 on 2020-06-25 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0006_auto_20200625_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
