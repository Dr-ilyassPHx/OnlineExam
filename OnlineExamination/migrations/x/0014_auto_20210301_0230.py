# Generated by Django 2.2.19 on 2021-03-01 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineExamination', '0013_auto_20210301_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineExamination.StudyMentor'),
        ),
    ]