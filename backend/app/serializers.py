from rest_framework import serializers
from .models import *

class UsuarioCustomizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCustomizado
        fields = '__all__'
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


class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Livros
        fields = '__all__'
        many = True

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Emprestimo
        fields = '__all__'
        many = True