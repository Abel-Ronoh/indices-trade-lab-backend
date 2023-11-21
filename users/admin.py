from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Affiliate, Portfolio

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'id_number')  # Customize displayed fields

admin.site.register(User, CustomUserAdmin)
admin.site.register(Affiliate)
admin.site.register(Portfolio)
