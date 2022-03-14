from django.urls import path
from rest_framework .routers import SimpleRouter

from .views import (
CursoAPIView, 
CursosAPIView, 
AvaliacaoAPIView, 
AvaliacoesAPIView,
CursoViewSet,
AvaliacaoViewSet)



# V2(rotas, porem agora na versao 2 da api..outra forma de fazer..menos codigo :)
# Aqui ele so gera um CRUD
router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

# endpoints(rotas) V1
urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),  
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'), 
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='curso_avaliacao'), 
    
    
    path('avaliacoes/', AvaliacoesAPIView.as_view(),name='avaliacoes'),      
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(),name='avaliacao'), 
]

'''
V1(comentario de funcionamento)
# api/v1/cursos - lista e cria curso(lista todos e cria um curso)
# /api/v1/cursos/pk - pega um curso(get,update, delete)
# /api/v1/cursos/pk/avaliacoes - pega todas as avaliacoes daquele curso com pk X
# /api/v1/cursos/pk/avaliacoes/avaliacoes_pk - pega uma avaliacao que vou fazer acesso
# api/v1/avaliacoes - lista e cria avaliacao
# /api/v1/avaliacoes/pk - pega uma avaliacao
'''