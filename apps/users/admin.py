from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from apps.users.models import User, Profile, UserMedia
from apps.users.forms import UserChangeForm, UserCreationForm


class ProfileAdminInline(admin.StackedInline):
    model = Profile
    fk_name = 'user'


class UserMediaAdminInline(admin.StackedInline):
    model = UserMedia
    fk_name = 'user'


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Info', {'fields': ('use_type', 'legal_type', 'state')}),
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
    inlines = (ProfileAdminInline, UserMediaAdminInline,)
