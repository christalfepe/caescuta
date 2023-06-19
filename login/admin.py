from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .forms import ModelUsuarioCreateForm, ModelUsuarioChangeForm
from .models import ModelUsuario

@admin.register(ModelUsuario)
class ModelUsuarioAdmin(UserAdmin):
    add_form = ModelUsuarioCreateForm
    form = ModelUsuarioChangeForm
    model = ModelUsuario
    list_display = ('first_name', 'last_name', 'email', 'fone', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('first_name', 'last_name', 'fone')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login','date_joined')}),
    )