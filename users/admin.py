from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin as OldUserAdmin

admin.site.register(Profile)

@admin.register(User)
class UserAdmin(OldUserAdmin):
	list_display = ('username','email','is_staff','is_reporter','is_writer')
	fieldsets = OldUserAdmin.fieldsets + (('User Type', {'fields': ('is_reporter','is_writer','is_member')}),)

