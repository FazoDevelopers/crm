# Generated by Django 4.2.4 on 2023-10-15 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='description',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='experience_desc',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='salary',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='salary_type',
        ),
    ]
