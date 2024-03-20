from django.db import models
from django.contrib.auth.hashers import make_password, check_password


# class CustomUserManager(BaseUserManager):
#     def create_user(self, nome, email, password, **outros):
#         email = self.normalize_email(email)
#         user = self.model(email=email, nome=nome, **outros)

#         if not nome:
#             raise ValueError('Nome não pode ser vazio')
        
#         hash_senha = make_password(password)
#         print('senha:' + hash_senha)
#         user.set_password(hash_senha)
#         user.save()
#         return user
    
#     def create_superuser(self, nome, email, password, **outros):
#         outros.setdefault('is_staff', True)
#         outros.setdefault('is_superuser', True)
#         outros.setdefault('is_active', True)

#         if outros.get('is_staff') is not True:
#             raise ValueError('Super Usuario precisa ter is_staff=True')

#         if outros.get('is_superuser') is not True:
#             raise ValueError('Super Usuario precisa ter is_superuser=True')

#         return self.create_user(nome, email, password, **outros)
    

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     nome = models.CharField(max_length=254, unique=True, blank=False)
#     email = models.EmailField(max_length=254, blank=False)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'nome'
#     REQUIRED_FIELDS = ['email']

#     def __str__(self):
#         return self.nome
    
