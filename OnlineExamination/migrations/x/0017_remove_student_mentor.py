# Generated by Django 2.2.19 on 2021-03-01 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineExamination', '0016_auto_20210301_0233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='mentor',
        ),
    ]
