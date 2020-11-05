from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from apps.users.models import User
from apps.users.forms import UserChangeForm, UserCreationForm


class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at')}),
    )
    limited_fieldsets = (
        (None, {'fields': ()}), ('Important dates', {'fields': ('last_login', 'created_at')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('username', 'password1', 'password2',)}),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = auth_admin.AdminPasswordChangeForm
    list_display = ('username', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username',)
    ordering = ('username',)
    readonly_fields = ('last_login', 'created_at',)



admin.site.register(User, UserAdmin)

