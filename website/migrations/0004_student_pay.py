# Generated by Django 4.2.3 on 2023-08-24 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_teacher_language_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PAID', "to'lagan"), ('NO_PAID', "to'lamagan")], max_length=255)),
                ('summa', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pays', to='website.student')),
            ],
        ),
    ]
