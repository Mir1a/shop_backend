# Generated by Django 5.0.1 on 2024-01-15 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users/avatar'),
        ),
    ]