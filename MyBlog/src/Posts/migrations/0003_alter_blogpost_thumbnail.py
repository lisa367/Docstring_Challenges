# Generated by Django 3.2 on 2022-10-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_blogpost_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='MyBlog'),
        ),
    ]