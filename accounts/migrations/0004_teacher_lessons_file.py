# Generated by Django 4.2.4 on 2023-10-13 07:08

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_student_amount_remove_student_amount_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='lessons_file',
            field=models.FileField(blank=True, null=True, upload_to=accounts.models.Teacher.lessons_file_path, verbose_name='dars jadvali:'),
        ),
    ]
