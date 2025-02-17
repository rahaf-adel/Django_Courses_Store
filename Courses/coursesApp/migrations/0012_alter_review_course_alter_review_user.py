# Generated by Django 4.0.4 on 2022-06-04 11:16

import coursesApp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coursesApp', '0011_alter_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='course',
            field=models.IntegerField(verbose_name=coursesApp.models.Course),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
