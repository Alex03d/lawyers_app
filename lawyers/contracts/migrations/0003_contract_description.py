# Generated by Django 2.2.19 on 2022-09-13 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_remove_contract_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='description',
            field=models.TextField(default='пусто'),
        ),
    ]
