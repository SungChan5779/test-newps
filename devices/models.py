from django.db import models
from core import models as core_models
from users import models as uesrs_models
# Create your models here.


class Ups(core_models.TimeStampedModel):
    device = models.ForeignKeyde, on_delete=models.CASCADE)
    input_voltage_r = models.IntegerField()
    input_voltage_s = models.IntegerField()
    input_voltage_t = models.IntegerField()

    input_ampare_r = models.IntegerField()
    input_ampare_s = models.IntegerField()
    input_ampare_t = models.IntegerField()

    input_hz_r = models.IntegerField()
    input_hz_s = models.IntegerField()
    input_hz_t = models.IntegerField()

    output_voltage_r = models.IntegerField()
    output_voltage_s = models.IntegerField()
    output_voltage_t = models.IntegerField()

    output_ampare_r = models.IntegerField()
    output_ampare_s = models.IntegerField()
    output_ampare_t = models.IntegerField()

    output_load_r = models.IntegerField()
    output_load_s = models.IntegerField()
    output_load_t = models.IntegerField()

    output_hz_r = models.IntegerField()
    output_hz_s = models.IntegerField()
    output_hz_t = models.IntegerField()

    bypass_voltage_r = models.IntegerField()
    bypass_voltage_s = models.IntegerField()
    bypass_voltage_t = models.IntegerField()

    bypass_ampare_r = models.IntegerField()
    bypass_ampare_s = models.IntegerField()
    bypass_ampare_t = models.IntegerField()

    bypass_hz_r = models.IntegerField()
    bypass_hz_s = models.IntegerField()
    bypass_hz_t = models.IntegerField()

    ups_temp = models.IntegerField()
    


class Temp_Humi(core_models.TimeStampedModel):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)


class Contact(core_models.TimeStampedModel):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)


class Device(core_models.TimeStampedModel):

    DEVICE_CHOICE = [
        ("ups", "UPS"), ("th", "온습도"), ("con", "접점")
    ]
    name = models.CharField(max_length=50, default="")
    ip = models.GenericIPAddressField(protocol="IPv4", unpack_ipv4=False)
    port_num = models.IntegerField()
    administrator = models.CharField(max_length=20, default="")
    device_select = models.CharField(max_length=3, choices=DEVICE_CHOICE)
    host = models.ForeignKey("users_models.User", on_delete=models.CASCADE)