# Generated by Django 3.2.6 on 2021-08-15 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctorconsult', '0003_auto_20210815_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='timeslots',
        ),
        migrations.DeleteModel(
            name='timeSlot',
        ),
    ]