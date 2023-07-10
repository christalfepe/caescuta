# CAEscuta
Trabalho feito em dupla para disciplina de Desenvolvimento de Sistemas WEB.
O projeto consiste em uma plataforma de gestão contínua de pessoas 
voltado para alunos da universidade, onde estes podem dar feedbacks 
quanto a espaços e/ou disciplinas. Além disso, administradores podem criar, 
ativar, desativar ou deletar pesquisas para que alunos possam responder.

## Instalações
É recomendado o uso da IDE PyCharm.

Instalações necessárias:

Python

Django:

        pip install django==3.1.4

Opcional:

        -m pip --upgrade pip

## Inserção de superuser via terminal
Executar o comando:

        python manage.py createsuperuser 

## Atualização do banco de dados
Caso haja inserção de usuários via terminal, após executar os comandos:

        python manage.py migrate 
        python manage.py makemigrations

## Execução do projeto
Para execução do projeto é necessário o comando

        python manage.py runserver
