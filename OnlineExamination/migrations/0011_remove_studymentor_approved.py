# Generated by Django 2.2.19 on 2021-03-06 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineExamination', '0010_studymentor_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studymentor',
            name='Approved',
        ),
    ]