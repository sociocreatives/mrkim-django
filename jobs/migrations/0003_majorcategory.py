# Generated by Django 5.0.4 on 2024-04-30 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_delete_majorcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='MajorCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/category/subcats')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.category')),
            ],
            options={
                'verbose_name_plural': 'Major Sub Categories',
            },
        ),
    ]
