# Generated by Django 3.1.2 on 2021-02-07 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_auto_20210207_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='snmp',
            field=models.CharField(blank=None, choices=[('megatec', 'MEGATEC'), ('eaton', 'EATON'), ('world_wise', 'WORLD_WISE')], default=None, max_length=20),
        ),
    ]