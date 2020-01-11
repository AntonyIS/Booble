from django.contrib import admin
from django.contrib.auth.admin import  UserAdmin
from .models import CustomUser, Blog


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email','date_joined','location', 'bio','followers', 'following', 'company','linkedin', 'github']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Blog)