# Generated by Django 2.2.19 on 2022-09-15 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0004_auto_20220915_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attorney',
            old_name='test',
            new_name='test1',
        ),
    ]
