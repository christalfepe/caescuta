from django.db import models

# Create your models here.
from django.db import models

# AbstractBaseUser x AbstractUser: ambos tratam de um usuário abstrato,
# porém, o BaseUser vem sem algumas funcionalidades prontas do Django.

#from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser , BaseUserManager

class UsuarioManager(BaseUserManager): #gerenciado do usuario
    use_in_migrations = True
    # informamos que esse vai ser o model de User que vamos usar no BD para autenticação

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório!')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # nos campos que vierem no **extra_fields, podemos garantir que o campo 'is_superuser' seja falso.
        extra_fields.setdefault('is_superuser', False)
        # nos campos que vierem no **extra_fields, podemos garantir que o campo 'is_staff' seja verdadeiro.
        # extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super usuário precisa ter is_superuser=True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super usuário precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)

class ModelUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True) # pois vamos usar o e-mail como login
    matricula = models.CharField('Matricula', max_length=8)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email' # poderíamos definir qualquer outro campo como username
    REQUIRED_FIELDS = ['first_name', 'last_name', 'matricula']
    # campos email e senha não precisa informar, pois o Django sabe que eles são obrigatórios para a autenticação.

    def __str__(self):
        return self.email

    objects = UsuarioManager() # com isso especificamos para o Django usar o nosso Manager e não o padrão.

