# Generated by Django 4.1 on 2022-12-31 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('lastName', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=20)),
                ('p_email', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('Pass', models.CharField(max_length=15)),
            ],
        ),
    ]