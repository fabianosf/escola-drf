from rest_framework import generics  # v1
from rest_framework.generics import get_object_or_404  # v1
from rest_framework import viewsets  # v2
from rest_framework.decorators import action  # v2
from rest_framework.response import Response  # v2

from rest_framework import mixins  # customizado

from rest_framework import permissions  # permissao token


from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from .permissions import EhSuperUser

'''
API V2
'''


class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # retorna todas as avaliacoes filtradas por esse curso que ta vindo
    # caso contrario retorna pra mim todas as avaliacoes
    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),
                                     curso_id=self.kwargs.get('curso_id'),
                                     pk=self.kwargs.get('avaliacao_pk'))
            return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


'''
API V2
'''

# Apenas Essa View que tem uma permissao propria vindo do djangoModel
class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions, ) # usuario autenticado consegue ler e adicionar curso
    
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    # traga todas as avaliacoes daquele curso
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avaliacoes.all(), many=True)
        return Response(serializer.data)


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
