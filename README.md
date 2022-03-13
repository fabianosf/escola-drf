# Escola DRF

 -> Ambiente Linux

* montar o ambiente virtual
* source env/bin/activate 
* python manage.py runserver 
* python 3.7.12

Explicacao Aplicacao Django REST

app = cursos<br><br>
urls - arquivos de rota<br><br>
views1 - arquivo de funcao apiview<br><br>
views - arquivo de funcao porem mais atual, utilizo o viewsets, é mais pratico usar né <br><br>
serializers - arquivo de serializar/deserializar objetos python(para uma melhor visualizacao) sem isso seria dificil de ler<br><br>
models - onde ficam nossos modelos, nossas classes<br><br>
permissions - arquivo de permissao de url(nesse caso, so pode deletar se for superusuario) eu defini isso em views<br><br>
admin - arquivo para poder registrar nossos models, para que possam ser vistos no django-admin<br><br>
settings - arquivo de configuracao do django<br><br>
requirements - arquivo das bibliotecas utilizadas<br><br>
env - ambiente virtual<br><br>
db - arquivo banco de dados, utilizei o postgresql<br><br>

