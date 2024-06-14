# Generated by Django 5.0.6 on 2024-06-14 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doselog',
            name='status',
            field=models.CharField(blank=True, choices=[('taken', 'Taken'), ('missed', 'Missed'), ('skipped', 'Skipped')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='doselog',
            name='taken_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]