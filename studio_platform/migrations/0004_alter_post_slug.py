# Generated by Django 3.2.15 on 2022-10-11 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio_platform', '0003_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]