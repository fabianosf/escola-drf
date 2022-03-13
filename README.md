# Escola DRF

 -> Ambiente Linux

* montar o ambiente virtual
* source env/bin/activate 
* python manage.py runserver 
* python 3.7.12

Explicacao Aplicacao Django REST

app = cursos
urls - arquivos de rota
views1 - arquivo de funcao apiview
views - arquivo de funcao porem mais atual, utilizo o viewsets, é mais pratico usar né 
serializers - arquivo de serializar/deserializar objetos python(para uma melhor visualizacao) sem isso seria dificil de ler
models - onde ficam nossos modelos, nossas classes
permissions - arquivo de permissao de url(nesse caso, so pode deletar se for superusuario) eu defini isso em views
admin - arquivo para poder registrar nossos models, para que possam ser vistos no django-admin
settings - arquivo de configuracao do django
requirements - arquivo das bibliotecas utilizadas
env - ambiente virtual
db - arquivo banco de dados, utilizei o postgresql

