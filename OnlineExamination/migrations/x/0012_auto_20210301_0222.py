# Generated by Django 2.2.19 on 2021-03-01 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineExamination', '0011_auto_20210301_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studymentor',
            name='user',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
