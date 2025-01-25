# API EM PYTHON com DJANGO 
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

## Descrição
Essa é uma API desenvolvida em Python utilizando o framework Django. A API permite a criação de usuários, autenticação via token JWT, e oferece funcionalidades para gerenciamento de carteiras (wallets). Os usuários podem verificar o saldo, realizar transferências e consultar o histórico de transferências realizadas.

## Como Rodar a API

- Primeiro é preciso instalar as dependências do projeto rodando:

          pip install -r requirements.txt

- A API estará disponível em `http://localhost:8000`.

### Migrando os models no banco

- Logo após vai ser necessário rodar o seguinte comando para migrar os models no banco:

        py manage.py makemigrations
        py manage.py migrate

### Comando para popular banco

- Logo em seguida rode um comando para popular o banco com informações ficticias:

        py manage.py populate

- E por ultimo é só rodar o docker do projeto com os seguintes comandos:

          docker-compose build
          docker-compose up

### Arquivo Postman 

- No projeto há o arquivo postman para realizar as requisições
