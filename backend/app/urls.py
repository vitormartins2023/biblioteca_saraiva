from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register (r'categoria', CategoriaView)
router.register (r'autor', AutorView)
router.register (r'livros', LivrosView)
router.register (r'Emprestimo', EmprestimoView)

urlpatterns = router.urls