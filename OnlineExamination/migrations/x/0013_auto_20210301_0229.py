# Generated by Django 2.2.19 on 2021-03-01 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineExamination', '0012_auto_20210301_0222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studymentor',
            old_name='user',
            new_name='userm',
        ),
        migrations.AlterField(
            model_name='student',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineExamination.StudyMentor', to_field='user'),
        ),
    ]
