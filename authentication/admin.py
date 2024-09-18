from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import *

class CustomUserAdmin(UserAdmin):
    model = User
    ordering = ('-date_joined',)
    list_display = ('last_name', 'role', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'role')
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ('first_name' ,'last_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'role', 'password1', 'password2'),
        }),
    )
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(User, CustomUserAdmin)
