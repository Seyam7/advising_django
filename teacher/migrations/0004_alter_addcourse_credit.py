# Generated by Django 4.1 on 2023-01-01 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_addcourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcourse',
            name='credit',
            field=models.FloatField(),
        ),
    ]
