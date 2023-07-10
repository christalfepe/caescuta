from django.contrib import admin
# imports necessários para administração do nosso usuário
from django.contrib.auth.admin import UserAdmin

from .forms import ModelUsuarioCreateForm, ModelUsuarioChangeForm
from .models import ModelUsuario


@admin.register(ModelUsuario)
class ModelUsuarioAdmin(UserAdmin):
    add_form = ModelUsuarioCreateForm # O CreateForm passará a ser o formulário para adicionar novos usuários
    form = ModelUsuarioChangeForm # O ChangeForm servirá para alteração dos usuários
    model = ModelUsuario
    list_display = ('first_name', 'last_name', 'email', 'matricula', 'is_staff')

    # quais dados apresentar ao acessar a área administrativa? veja:
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('first_name', 'last_name', 'matricula')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login','date_joined')}),
    )

