# Generated by Django 4.1 on 2022-12-31 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_rename_student_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='addcourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=40)),
                ('courseCode', models.CharField(max_length=40)),
                ('credit', models.CharField(max_length=40)),
            ],
        ),
    ]