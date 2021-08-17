# Generated by Django 3.2.6 on 2021-08-15 10:13

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('doctorconsult', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='timingSlots',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('09:00-10:00', '09:00-10:00'), ('10:00-11:00', '10:00-11:00'), ('11:00-12:00', '11:00-12:00'), ('12:00-01:00', '12:00-01:00')], default='', max_length=47),
        ),
    ]
