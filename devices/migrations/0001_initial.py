# Generated by Django 3.1.2 on 2021-02-07 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('con_1', models.IntegerField(default=0)),
                ('con_2', models.IntegerField(default=0)),
                ('con_3', models.IntegerField(default=0)),
                ('con_4', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Contact',
            },
            bases=('core.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('snmp', models.CharField(choices=[('megatec', 'MEGATEC'), ('eaton', 'EATON'), ('world_wise', 'WORLD_WISE')], max_length=20)),
                ('name', models.CharField(default='', max_length=50)),
                ('ip', models.GenericIPAddressField(protocol='IPv4')),
                ('port_num', models.IntegerField(default=0)),
                ('administrator', models.CharField(default='', max_length=20)),
                ('device_select', models.CharField(choices=[('ups', 'UPS'), ('th', '온습도'), ('con', '접점')], max_length=3)),
            ],
            bases=('core.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Ups',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('ups_model', models.CharField(default='', max_length=50)),
                ('ups_admin', models.CharField(default='(주)뉴피에스', max_length=50)),
                ('ups_location', models.CharField(default='UPS실', max_length=50)),
                ('indent_model', models.CharField(default='', max_length=50)),
                ('input_phase', models.IntegerField(default=0)),
                ('input_fail_cause', models.IntegerField(default=0)),
                ('output_phase', models.IntegerField(default=0)),
                ('output_status', models.IntegerField(default=0)),
                ('input_voltage', models.IntegerField(default=0)),
                ('input_voltage_r', models.IntegerField(default=0)),
                ('input_voltage_s', models.IntegerField(default=0)),
                ('input_voltage_t', models.IntegerField(default=0)),
                ('input_current', models.IntegerField(default=0)),
                ('input_current_r', models.IntegerField(default=0)),
                ('input_current_s', models.IntegerField(default=0)),
                ('input_current_t', models.IntegerField(default=0)),
                ('input_hz', models.IntegerField(default=0)),
                ('input_hz_r', models.IntegerField(default=0)),
                ('input_hz_s', models.IntegerField(default=0)),
                ('input_hz_t', models.IntegerField(default=0)),
                ('output_voltage', models.IntegerField(default=0)),
                ('output_voltage_r', models.IntegerField(default=0)),
                ('output_voltage_s', models.IntegerField(default=0)),
                ('output_voltage_t', models.IntegerField(default=0)),
                ('output_current', models.IntegerField(default=0)),
                ('output_current_r', models.IntegerField(default=0)),
                ('output_current_s', models.IntegerField(default=0)),
                ('output_current_t', models.IntegerField(default=0)),
                ('output_load', models.IntegerField(default=0)),
                ('output_load_r', models.IntegerField(default=0)),
                ('output_load_s', models.IntegerField(default=0)),
                ('output_load_t', models.IntegerField(default=0)),
                ('output_hz', models.IntegerField(default=0)),
                ('output_hz_r', models.IntegerField(default=0)),
                ('output_hz_s', models.IntegerField(default=0)),
                ('output_hz_t', models.IntegerField(default=0)),
                ('bypass_voltage', models.IntegerField(default=0)),
                ('bypass_voltage_r', models.IntegerField(default=0)),
                ('bypass_voltage_s', models.IntegerField(default=0)),
                ('bypass_voltage_t', models.IntegerField(default=0)),
                ('bypass_current', models.IntegerField(default=0)),
                ('bypass_current_r', models.IntegerField(default=0)),
                ('bypass_current_s', models.IntegerField(default=0)),
                ('bypass_current_t', models.IntegerField(default=0)),
                ('bypass_hz', models.IntegerField(default=0)),
                ('bypass_hz_r', models.IntegerField(default=0)),
                ('bypass_hz_s', models.IntegerField(default=0)),
                ('bypass_hz_t', models.IntegerField(default=0)),
                ('ups_temp', models.IntegerField(default=0)),
                ('battery_voltage', models.IntegerField(default=0)),
                ('battery_status', models.IntegerField(default=0)),
                ('battery_current', models.IntegerField(default=0)),
                ('device_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.device')),
            ],
            options={
                'verbose_name_plural': 'UPS',
            },
            bases=('core.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Temp_Humi',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('temp_1', models.IntegerField(default=0)),
                ('temp_2', models.IntegerField(default=0)),
                ('humi_1', models.IntegerField(default=0)),
                ('humi_2', models.IntegerField(default=0)),
                ('device_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.device')),
            ],
            options={
                'verbose_name_plural': 'TEMP_HUMI',
            },
            bases=('core.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Phone_Number',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('name_1', models.CharField(default=None, max_length=20)),
                ('name_2', models.CharField(default=None, max_length=20)),
                ('name_3', models.CharField(default=None, max_length=20)),
                ('name_4', models.CharField(default=None, max_length=20)),
                ('name_5', models.CharField(default=None, max_length=20)),
                ('name_6', models.CharField(default=None, max_length=20)),
                ('name_7', models.CharField(default=None, max_length=20)),
                ('name_8', models.CharField(default=None, max_length=20)),
                ('name_9', models.CharField(default=None, max_length=20)),
                ('name_10', models.CharField(default=None, max_length=20)),
                ('phone_1', models.CharField(default=None, max_length=11)),
                ('phone_2', models.CharField(default=None, max_length=11)),
                ('phone_3', models.CharField(default=None, max_length=11)),
                ('phone_4', models.CharField(default=None, max_length=11)),
                ('phone_5', models.CharField(default=None, max_length=11)),
                ('phone_6', models.CharField(default=None, max_length=11)),
                ('phone_7', models.CharField(default=None, max_length=11)),
                ('phone_8', models.CharField(default=None, max_length=11)),
                ('phone_9', models.CharField(default=None, max_length=11)),
                ('phone_10', models.CharField(default=None, max_length=11)),
                ('user', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='devices.device')),
            ],
            options={
                'verbose_name_plural': 'Phone_Number',
            },
            bases=('core.timestampedmodel',),
        ),
    ]
