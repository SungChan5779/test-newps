from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Device)
class Devices(admin.ModelAdmin):
    pass


@admin.register(models.Ups)
class Ups_Item(admin.ModelAdmin):
    fieldsets = (
        ("UPS_IDENT", {
            "fields": ("device_name","ups_model","ups_admin","ups_location","indent_model",
                
            ),
        }),
        ("PHASE&STATUS",{
            "fields": ("input_phase","input_fail_cause","output_phase","output_status","ups_temp",
            ),
        }),
        ("INPUT_DATA",{
            "fields": ("input_voltage","input_voltage_r","input_voltage_s","input_voltage_t","input_current","input_current_r","input_current_s","input_current_t","input_hz","input_hz_r","input_hz_s","input_hz_t",
            ),
        }),
        ("OUTPUT_DATA",{
            "fields": ("output_voltage","output_voltage_r","output_voltage_s","output_voltage_t","output_current","output_current_r","output_current_s","output_current_t","output_load","output_load_r","output_load_s","output_load_t","output_hz","output_hz_r","output_hz_s","output_hz_t",
            ),
        }),
        ("BYPASS_DATA",{
            "fields": ("bypass_voltage","bypass_voltage_r","bypass_voltage_s","bypass_voltage_t","bypass_current","bypass_current_r","bypass_current_s","bypass_current_t","bypass_hz","bypass_hz_r","bypass_hz_s","bypass_hz_t",
                
            ),
        }),
        ("BATTERY_DATA", {
            "fields": ("battery_voltage","battery_status","battery_current",
            ),
        }),
        
    )
    
@admin.register(models.Temp_Humi)
class TH_Item(admin.ModelAdmin):
    pass

@admin.register( models.Contact, models.Phone_Number)
class Device_Items(admin.ModelAdmin):
    pass
