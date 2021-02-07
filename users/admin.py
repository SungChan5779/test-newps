from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):        #admin.modelAdmin 대신에 from django.contrib.auth.admin import UserAdmin 사용
    fieldsets = UserAdmin.fieldsets + (     #UserAdmin.fildsets와 CustomFields를 합쳐서 보여주기
        ("CustomFields", {
            'fields': (
                'bio','company',
            ),
        }),
    )

