# Generated by Django 4.0.4 on 2022-06-04 11:39

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesApp', '0013_alter_review_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.CharField(max_length=40, verbose_name=django.contrib.auth.models.User),
        ),
    ]
