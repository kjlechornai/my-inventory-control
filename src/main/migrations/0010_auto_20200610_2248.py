# Generated by Django 3.0.6 on 2020-06-10 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200610_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_slug',
            field=models.CharField(max_length=100, default=1),
        ),
    ]
