# Generated by Django 4.2.4 on 2023-10-13 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_teacher_lessons_file'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='teacher',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sinflar', to='accounts.teacher'),
        ),
    ]
