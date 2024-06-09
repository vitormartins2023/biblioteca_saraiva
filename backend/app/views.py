from django.shortcuts import render
from .models import *
from .serializers import * 

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


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

    def list(self, request):
        queryset = Livros.objects.filter(status='A')
        serializer = LivrosSerializer(queryset,many=True)
        print(serializer.data)
        return Response(serializer.data)

class EmprestimoView(ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    
    def create(self, request, *args, **kwargs):
        #coleta os dados que vem do front
        data = request.data
        #consulta no banco para as condições previstas
        vendasDoUsuario = Emprestimo.objects.filter(customUserFK=data['customUserFK'])
        print("quantidade de vendas pendentes: ", vendasDoUsuario.count())
        
        #se o limite de vendas for alçado impede a criação desta venda
        if vendasDoUsuario.count() >= 3:
            print("limite excedido")
            return Response(status=403,data='Usuário com mais de 3 vendas pendentes!')
        else:
            #se o limite ainda não foi alcançado!
            return super().create(request, *args, **kwargs)

