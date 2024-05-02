# Generated by Django 5.0.4 on 2024-05-01 15:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Faqs',
            },
        ),
        migrations.AlterField(
            model_name='legal',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
