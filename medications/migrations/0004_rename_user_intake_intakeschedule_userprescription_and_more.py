# Generated by Django 5.0.6 on 2024-06-13 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0003_doselog_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intakeschedule',
            old_name='user_intake',
            new_name='userprescription',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='intake_time',
        ),
        migrations.AddField(
            model_name='notification',
            name='intake_schedule',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='medications.intakeschedule'),
            preserve_default=False,
        ),
    ]
