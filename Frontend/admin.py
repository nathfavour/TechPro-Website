from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your CustomUser model with the admin site
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'first_name', 'last_name', 'email', 'aim', 'is_staff', 'is_active',)

# Replace 'CustomUser' with the actual name of your User model if different

# Register the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)
