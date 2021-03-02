# Generated by Django 3.1.6 on 2021-02-14 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('devices', '0003_auto_20210207_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='device_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='devices.device'),
        ),
        migrations.AlterField(
            model_name='device',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='phone_number',
            name='user',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='devices.device'),
        ),
        migrations.AlterField(
            model_name='temp_humi',
            name='device_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temps', to='devices.device'),
        ),
        migrations.AlterField(
            model_name='ups',
            name='device_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upss', to='devices.device'),
        ),
    ]
