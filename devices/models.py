from django.db import models
from core import models as core_models
from users import models as users_models
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class Abstract(core_models.TimeStampedModel):   #아직 사용x 필요하면 사용예정

    name = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Device(core_models.TimeStampedModel):

    DEVICE_CHOICE = [
        ("ups", "UPS"), ("th", "온습도"), ("con", "접점")
    ]
    SNMP_CHOICE = [
        ("megatec", "MEGATEC"), ("eaton", "EATON"), ("world_wise", "WORLD_WISE")
    ]
    snmp = models.CharField(max_length=20, choices=SNMP_CHOICE, blank=None, default=None)
    name = models.CharField(max_length=50, default="")
    ip = models.GenericIPAddressField(protocol="IPv4", unpack_ipv4=False)
    port_num = models.IntegerField(default=0)
    administrator = models.CharField(max_length=20, default="")
    device_select = models.CharField(max_length=3, choices=DEVICE_CHOICE)
    host = models.ForeignKey(users_models.User, on_delete=models.CASCADE,related_name="devices")

    def __str__(self):
        return f"{self.name}_{self.device_select}"
        

@receiver(post_save, sender=Device)
def device_postsave(sender, instance, created, **kwargs):
    print(instance.device_select)
    print(created)
    device_select = instance.device_select
    if created:
        if device_select == "ups":
            Ups.objects.create(device_name=instance)
        elif device_select == "th":
            Temp_Humi.objects.create(device_name=instance)
        else:
            Contact.objects.create(device_name=instance)
        Phone_Number.objects.create(user=instance)



class Ups(core_models.TimeStampedModel):
    device_name = models.ForeignKey("Device", related_name="upss", on_delete=models.CASCADE)

    ups_model = models.CharField(max_length=50, default="")
    ups_admin = models.CharField(max_length=50, default="(주)뉴피에스")
    ups_location = models.CharField(max_length=50, default="UPS실")

    indent_model = models.CharField(max_length=50, default="")
    input_phase = models.IntegerField(default=0)
    input_fail_cause = models.IntegerField(default=0)
    output_phase = models.IntegerField(default=0)
    output_status = models.IntegerField(default=0)

    input_voltage = models.FloatField(default=0)
    input_voltage_r = models.FloatField(default=0)
    input_voltage_s = models.FloatField(default=0)
    input_voltage_t = models.FloatField(default=0)

    input_current = models.FloatField(default=0)
    input_current_r = models.FloatField(default=0)
    input_current_s = models.FloatField(default=0)
    input_current_t = models.FloatField(default=0)

    input_hz = models.FloatField(default=0)
    input_hz_r = models.FloatField(default=0)
    input_hz_s = models.FloatField(default=0)
    input_hz_t = models.FloatField(default=0)

    output_voltage = models.FloatField(default=0)
    output_voltage_r = models.FloatField(default=0)
    output_voltage_s = models.FloatField(default=0)
    output_voltage_t = models.FloatField(default=0)

    output_current = models.FloatField(default=0)
    output_current_r = models.FloatField(default=0)
    output_current_s = models.FloatField(default=0)
    output_current_t = models.FloatField(default=0)

    output_load = models.IntegerField(default=0)
    output_load_r = models.IntegerField(default=0)
    output_load_s = models.IntegerField(default=0)
    output_load_t = models.IntegerField(default=0)

    output_hz = models.FloatField(default=0)
    output_hz_r = models.FloatField(default=0)
    output_hz_s = models.FloatField(default=0)
    output_hz_t = models.FloatField(default=0)

    bypass_voltage = models.FloatField(default=0)
    bypass_voltage_r = models.FloatField(default=0)
    bypass_voltage_s = models.FloatField(default=0)
    bypass_voltage_t = models.FloatField(default=0)

    bypass_current = models.FloatField(default=0)
    bypass_current_r = models.FloatField(default=0)
    bypass_current_s = models.FloatField(default=0)
    bypass_current_t = models.FloatField(default=0)

    bypass_hz = models.FloatField(default=0)
    bypass_hz_r = models.FloatField(default=0)
    bypass_hz_s = models.FloatField(default=0)
    bypass_hz_t = models.FloatField(default=0)

    ups_temp = models.FloatField(default=0)
    
    battery_voltage = models.FloatField(default=0)
    battery_status = models.IntegerField(default=0)
    battery_current = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = "UPS"

    def __str__(self):
        return f"{self.device_name} -{self.ups_location}({self.ups_model})"
        

class Temp_Humi(core_models.TimeStampedModel):

    device_name = models.ForeignKey("Device", related_name="temps", on_delete=models.CASCADE)
    th_location = models.CharField(max_length=50, default="전산실")
    temp_1 = models.FloatField(default=0)
    temp_2 = models.FloatField(default=0)
    humi_1 = models.FloatField(default=0)
    humi_2 = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = "TEMP_HUMI"

    def __str__(self):
        return f"{self.device_name} - {self.th_location}"
    


class Contact(core_models.TimeStampedModel):

    device_name = models.ForeignKey("Device", related_name="contacts", on_delete=models.CASCADE)
    con_location = models.CharField(max_length=50, default="전산실")
    con_1 = models.IntegerField(default=0)
    con_2 = models.IntegerField(default=0)
    con_3 = models.IntegerField(default=0)
    con_4 = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Contact"

    def __str__(self):
        return f'{self.device_name} - {self.con_location}'
    


class Phone_Number(core_models.TimeStampedModel):
    
    user = models.OneToOneField("Device", on_delete=models.CASCADE, default=None, blank=True, related_name="phones")
    name_1 = models.CharField(max_length=20, blank=True)
    name_2 = models.CharField(max_length=20, blank=True)
    name_3 = models.CharField(max_length=20, blank=True)
    name_4 = models.CharField(max_length=20, blank=True)
    name_5 = models.CharField(max_length=20, blank=True)
    name_6 = models.CharField(max_length=20, blank=True)
    name_7 = models.CharField(max_length=20, blank=True)
    name_8 = models.CharField(max_length=20, blank=True)
    name_9 = models.CharField(max_length=20, blank=True)
    name_10 = models.CharField(max_length=20, blank=True)

    phone_1 = models.CharField(max_length=11, blank=True)
    phone_2 = models.CharField(max_length=11, blank=True)
    phone_3 = models.CharField(max_length=11, blank=True)
    phone_4 = models.CharField(max_length=11, blank=True)
    phone_5 = models.CharField(max_length=11, blank=True)
    phone_6 = models.CharField(max_length=11, blank=True)
    phone_7 = models.CharField(max_length=11, blank=True)
    phone_8 = models.CharField(max_length=11, blank=True)
    phone_9 = models.CharField(max_length=11, blank=True)
    phone_10 = models.CharField(max_length=11, blank=True)

    class Meta:
        verbose_name_plural = "Phone_Number"
    
    def __str__(self):
        return f'{self.user.name} - {self.user.device_select}'
    