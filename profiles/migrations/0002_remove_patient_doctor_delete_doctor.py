# Generated by Django 5.0.6 on 2024-06-14 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='doctor',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]