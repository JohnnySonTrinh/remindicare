# Generated by Django 5.0.6 on 2024-06-14 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0002_remove_patient_doctor_delete_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(choices=[('medication', 'Medication'), ('supplement', 'Supplement')], max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('dosage_unit', models.CharField(choices=[('mg', 'mg'), ('µg', 'µg'), ('g', 'g'), ('ml', 'ml'), ('l', 'l'), ('IU', 'IU')], max_length=50)),
                ('dosage_type', models.CharField(choices=[('pill', 'Pill'), ('liquid', 'Liquid'), ('injection', 'Injection'), ('capsule', 'Capsule'), ('tablet', 'Tablet'), ('ointment', 'Ointment'), ('powder', 'Powder')], max_length=50)),
                ('dosage_amount', models.CharField(max_length=50)),
                ('dosage_frequency', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='IntakeSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.ManyToManyField(related_name='schedules', to='medications.day')),
            ],
        ),
        migrations.CreateModel(
            name='IntakeTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intake_times', to='medications.intakeschedule')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('sent', 'Sent'), ('snoozed', 'Snoozed'), ('dismissed', 'Dismissed')], max_length=10)),
                ('type', models.CharField(default='reminder', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('intake_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='medications.intaketime')),
            ],
        ),
        migrations.CreateModel(
            name='DoseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taken_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('taken', 'Taken'), ('missed', 'Missed'), ('skipped', 'Skipped')], max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dose_logs', to='profiles.patient')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dose_logs', to='medications.notification')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_on_going', models.BooleanField(default=False)),
                ('valid_until', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('caregiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prescriptions', to='profiles.caregiver')),
                ('medications', models.ManyToManyField(related_name='prescriptions', to='medications.medication')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescriptions', to='profiles.patient')),
            ],
        ),
        migrations.AddField(
            model_name='intakeschedule',
            name='prescription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='medications.prescription'),
        ),
    ]
