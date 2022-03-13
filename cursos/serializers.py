from rest_framework import serializers
from django.db.models import Avg
from .models import Curso, Avaliacao



class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )


    # customizando notas de avalicao
    def validate_avaliacao(self, valor): 
        if valor in range(1,6):
            return valor
        raise serializers.ValidationError('A avaliacao precisa ser um inteiro entre 1 e 5')



class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True) # apenas leitura...vai aparecer avaliacoes la

    # HyperLinked Related Field
    # ele te da um link daquela avalicao
    # avaliacoes = serializers.HyperlinkedRelatedField(
    #    many=True,
    #   ready_only=True,
    #   view_name='avaliacao-detail'
    # )

    # Primary key Related Field
    # retorna apenas o id de avaliacoes nesse caso.. de relacionamento.
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
            'media_avaliacoes'
        )
    
    # media de avaliacoes    
    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')
        
        if media is None:
            return 0
        return round(media * 2) / 2
