from django.contrib.auth.models import BaseUserManager

class Gerenciador(BaseUserManager):

    def create_user(self, email, password=None, cpf=None, **extra_fields):
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            cpf=cpf,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None, cpf='08453757259', **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        return self.create_user(email, password, cpf, **extra_fields)