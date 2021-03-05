# Generated by Django 2.2.19 on 2021-03-01 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineExamination', '0014_auto_20210301_0230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studymentor',
            old_name='userm',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='student',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineExamination.StudyMentor', to_field='userm'),
        ),
    ]