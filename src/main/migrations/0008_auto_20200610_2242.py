# Generated by Django 3.0.6 on 2020-06-10 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200610_2123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('catname',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='category_summary',
        ),
        migrations.RemoveField(
            model_name='category',
            name='is_main',
        ),
        migrations.RemoveField(
            model_name='category',
            name='item',
        ),
        migrations.RemoveField(
            model_name='category',
            name='sub_category',
        ),
        migrations.AddField(
            model_name='category',
            name='category_slug',
            field=models.SlugField(default=1),
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Category'),
        ),
    ]
