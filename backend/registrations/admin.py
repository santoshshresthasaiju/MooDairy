from django.contrib import admin
from .models import CustomUser

from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    # Define the fields you want to display in the admin panel
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_active', 'role')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'role')
    ordering = ('username',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )

    def save_model(self, request, obj, form, change):
        # Automatically mark user as active when created from the admin panel
        if not obj.pk:  # This means the user is being created
            obj.is_active = True  # Automatically set the user as active
        super().save_model(request, obj, form, change)

admin.site.register(CustomUser, CustomUserAdmin)