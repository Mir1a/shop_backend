# Generated by Django 3.2.7 on 2024-01-21 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name': 'Транзакция', 'verbose_name_plural': 'Транзакции'},
        ),
    ]
