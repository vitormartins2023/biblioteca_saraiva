#o models está igual ao do vitor pq na aula de segunda eu fiz junto com ele
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .gerenciador import Gerenciador
from django.utils import timezone


class UsuarioCustomizado(AbstractBaseUser,PermissionsMixin):
     email = models.EmailField("endereço de email", unique=True)
     is_staff = models.BooleanField(default=False)
     is_active = models.BooleanField(default=True)
     telefone = models.CharField(max_length=15, null=True, blank=True)
     endereco = models.CharField(max_length=200)
     cpf = models.CharField(max_length=20)
     
     objects = Gerenciador()

     USERNAME_FIELD = "email"
     REQUIRED_FIELDS = []

     def __str__(self):
          return self.email

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
    
class Autor(models.Model):
    nome = models.CharField(max_length=100)
    biografia =  models.CharField(max_length=500)
    foto = models.CharField(max_length=20000)
    customUserFK =  models.ForeignKey(UsuarioCustomizado, related_name='usuarioAutor', on_delete=models.CASCADE)
    Nascimento = models.DateField()

    def __str__(self):
        return self.nome
    

class Bibliotecario(models.Model):
    nome = models.CharField(max_length=100)
    customUserFK =  models.ForeignKey(UsuarioCustomizado, related_name='usuarioBibliotecario', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

TYPE = [
    ('E','Ebook'),
    ('F', 'Fisico')
]
STATUS = [
    ('A','Aprovado'),
    ('C', 'Cancelado'),
    ('P', 'Pendente')
]


class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=400)
    N_paginas = models.IntegerField()
    formato = models.CharField(max_length=1, choices=TYPE)
    status = models.CharField(max_length=10, choices= STATUS, default = 'P')
    n_edicao = models.IntegerField()
    autor_FK = models.ForeignKey(Autor, related_name='LivroAutor', on_delete=models.CASCADE)
    categoria_FK = models.ForeignKey(Categoria, related_name='CategoriaLivro', on_delete=models.CASCADE)
    dataPub = models.DateField()
    valor_livro =  models.DecimalField(max_digits=5, decimal_places=2,null=True, blank= True)
    capa = models.CharField(max_length=1000)
    estrela = models.IntegerField()
    estoque = models.IntegerField()

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    livro = models.ManyToManyField(Livros, related_name="LivrosEmprestimo")
    customUserFK =  models.ForeignKey(UsuarioCustomizado, related_name='usuarioEmprestimo', on_delete=models.CASCADE)
    valor_total = models.DecimalField(max_digits=5, decimal_places=2)
    data_pegou = models.DateTimeField(auto_now_add=True)
    data_prevista = models.DateField(null=True, blank= True)
    data_entrega = models.DateField(null=True, blank= True)

    def __str__(self):
         return self.CustomUserFK.email
