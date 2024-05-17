# rest/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Paragraph

# Register the Paragraph model to the admin site
admin.site.register(Paragraph)

# CustomUserAdmin class to define the admin interface for the CustomUser model
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'name', 'dob', 'is_staff']  # Fields to display in the user list
    fieldsets = (
        (None, {'fields': ('email', 'name', 'dob', 'password')}),  # Fields to display in the user detail form
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),  # Fields related to permissions
        ('Important dates', {'fields': ('last_login',)}),  # Fields related to important dates
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'dob', 'password1', 'password2', 'is_staff', 'is_superuser')}  # Fields to display in the user creation form
        ),
    )
    search_fields = ('email',)  # Fields to include in the search
    ordering = ('email',)  # Default ordering of the user list

# Register the CustomUser model with the CustomUserAdmin class to the admin site
admin.site.register(CustomUser, CustomUserAdmin)
