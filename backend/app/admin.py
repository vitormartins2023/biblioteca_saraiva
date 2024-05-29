from django.contrib import admin
from .models import *  
from django.contrib.auth.admin import UserAdmin

class AdminUsuarioCustomizado(UserAdmin):
    model=UsuarioCustomizado
    list_display = ['id', 'email', 'cpf']
    list_display_links = ('id', 'email', 'cpf',)

    fieldsets = (
        (None,{'fields': ('email','password')}),
        ('Permissions', {'fields': ('is_staff','is_active','groups','user_permissions',)}),
        ('Management', {'fields': ('last_login',)}),
        ('Custom fields', {'fields': ('cpf','telefone','endereco',)}),
    )
    filter_horizontal = ('groups','user_permissions',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','password1','password2', 'is_staff','is_active','groups','user_permissions',)
        }),
    )    
    search_fields = ['email',]
    ordering = ['email']

admin.site.register(UsuarioCustomizado,AdminUsuarioCustomizado)

class AdminCategoria(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Categoria,AdminCategoria)


class AdminAutor(admin.ModelAdmin):
    list_display = ['id', 'nome','biografia','foto','customUserFK','Nascimento']
    list_display_links = ('id', 'nome','biografia','foto','customUserFK','Nascimento',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Autor,AdminAutor)

class AdminBibliotecario(admin.ModelAdmin):
    list_display = ['id', 'nome','customUserFK']
    list_display_links = ('id', 'nome','customUserFK',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Bibliotecario,AdminBibliotecario)


class AdminLivros(admin.ModelAdmin):
    list_display = ['id', 'titulo','descricao','n_paginas','formato','status','n_edicao','autor_FK','categoria_FK','dataPub','valor_livro','capa','estrela','estoque']
    list_display_links = ('id', 'titulo','autor_FK','n_paginas','valor_livro',)
    search_fields = ('descricao','id',)
    list_per_page = 10

admin.site.register(Livros,AdminLivros)

class AdminEmprestimo(admin.ModelAdmin):
    list_display = ['id','customUserFK','valor_total','data_pegou','data_prevista','data_entrega'] #Quando subi o campo livro que possui manyToManyfield deu erro "The value of 'list_display[1]' must not be a many-to-many field or a reverse foreign key"
    list_display_links = ('id','customUserFK','valor_total',)
    search_fields = ('customUserFK','id',)
    list_per_page = 10

admin.site.register(Emprestimo,AdminEmprestimo)


    