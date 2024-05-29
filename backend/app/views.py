from django.shortcuts import render
from .models import *
from .serializers import * 

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class CategoriaView(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = (IsAuthenticated,)

class AutorView(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class BibliotecarioView(ModelViewSet):
    queryset = Bibliotecario.objects.all()
    serializer_class = BibliotecarioSerializer

class LivrosView(ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer

class EmprestimoView(ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

