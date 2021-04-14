from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('first_name', 'last_name' ,'email', 'mobile_number', 'gender' ,'date_of_birth', 'address1', 'address2', 'city', 'state', 'pincode', 'is_staff', 'is_active', 'date_joined', 'last_login', 'profile_picture', 'email_confirmed', 'reset_password', )
    list_filter = ('is_staff', 'is_active', 'gender' ,'city', 'state', 'date_joined', 'email_confirmed', 'reset_password', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Activation', {'fields': ('email_confirmed', 'reset_password')}),
        ('User Profile', {'fields': ('mobile_number', 'gender', 'date_of_birth', 'address1', 'address2', 'city', 'state', 'pincode', 'profile_picture')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'mobile_number', 'gender', 'date_of_birth', 'address1', 'address2', 'city', 'state', 'pincode', 'profile_picture', 'email_confirmed', 'reset_password', )}
        ),
    )
    search_fields = ('email',)
    ordering = ('date_joined',)

admin.site.register(CustomUser, CustomUserAdmin)