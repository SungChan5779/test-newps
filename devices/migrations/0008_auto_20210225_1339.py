# Generated by Django 3.1.6 on 2021-02-25 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0007_auto_20210225_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone_number',
            name='user',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='devices.device'),
        ),
    ]
