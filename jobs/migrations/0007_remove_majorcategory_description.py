# Generated by Django 5.0.4 on 2024-04-29 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_alter_majorcategory_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='majorcategory',
            name='description',
        ),
    ]
