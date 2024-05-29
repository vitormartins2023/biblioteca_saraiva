from rest_framework import serializers
from .models import *

class UsuarioCustomizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCustomizado
        fields = ['id','email','telefone','endereco','cpf']
        many = True

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categoria
        fields = '__all__'
        many = True

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Autor
        fields = '__all__'
        many = True

class BibliotecarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Bibliotecario
        fields = '__all__'
        many = True



class LivrosSerializer(serializers.ModelSerializer):
    categoria_FK= CategoriaSerializer(read_only=True)
    autor_FK= AutorSerializer(read_only=True)
    class Meta:
        model= Livros
        fields = '__all__'
        many = True

class EmprestimoSerializer(serializers.ModelSerializer):
    customUserFK= UsuarioCustomizadoSerializer(read_only=True)
    livro= LivrosSerializer(read_only= True)
    class Meta:
        model= Emprestimo
        fields = '__all__'
        many = True