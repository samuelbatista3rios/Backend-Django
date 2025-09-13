# 🐍 Backend Django – Prova GTHPI

Este projeto é um backend desenvolvido em **Django + Django REST Framework**, com foco em cadastro e gerenciamento de pessoas.  
Foram implementadas APIs RESTful documentadas via **Swagger**, com persistência de dados utilizando **PostgreSQL**.

---

## 🚀 Funcionalidades
- CRUD de Pessoas (Incluir, Pesquisar, Alterar e Excluir)
- Cálculo de **peso ideal** baseado em sexo e altura
- Documentação automática da API (Swagger UI / ReDoc)
- Persistência de dados utilizando ORM (Django Models)
- API REST seguindo boas práticas (status codes, serialização, validações)

---

## 🛠️ Tecnologias utilizadas
- **Python 3.11+**
- **Django 5+**
- **Django REST Framework (DRF)**
- **drf-yasg** (Swagger / OpenAPI Docs)
- **PostgreSQL 14+**
- **Psycopg2** (driver PostgreSQL)

---

## 📂 Estrutura do Projeto
Backend-Django/
│── pessoas/ # App principal (models, views, serializers, urls)
│── prova_gthpi/ # Configuração principal do projeto Django
│── manage.py # Gerenciador do Django
│── requirements.txt # Dependências do projeto


---

## ⚙️ Configuração e Instalação

### 1. Clone o repositório

git clone https://github.com/seu-usuario/Backend-Django.git
cd Backend-Django
2. Crie e ative o ambiente virtual

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Instale as dependências

pip install -r requirements.txt
4. Configure o banco PostgreSQL
Crie um banco no PostgreSQL:

sql

CREATE DATABASE backend_django;
CREATE USER meu_usuario WITH PASSWORD 'minha_senha';
ALTER ROLE meu_usuario SET client_encoding TO 'utf8';
ALTER ROLE meu_usuario SET default_transaction_isolation TO 'read committed';
ALTER ROLE meu_usuario SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE backend_django TO meu_usuario;
No arquivo prova_gthpi/settings.py, configure:


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'backend_django',
        'USER': 'meu_usuario',
        'PASSWORD': 'minha_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
5. Execute as migrações

python manage.py migrate
6. Crie um superusuário (opcional, para acessar o admin)

python manage.py createsuperuser

7. Inicie o servidor
python manage.py runserver
📌 Endpoints principais
Swagger UI → http://127.0.0.1:8000/swagger/

ReDoc → http://127.0.0.1:8000/redoc/

Listar pessoas → GET /pessoas/

Incluir pessoa → POST /pessoas/

Pesquisar pessoa por ID → GET /pessoas/{id}/

Alterar pessoa → PUT /pessoas/{id}/

Excluir pessoa → DELETE /pessoas/{id}/

Calcular peso ideal → POST /pessoas/peso-ideal/

📖 Exemplo de payload (POST Pessoa)
json

{
  "nome": "Samuel",
  "data_nascimento": "1999-05-10",
  "cpf": "123.456.789-00",
  "sexo": "M",
  "altura": 1.80,
  "peso": 80.0
}
🗄️ Exemplo de DTO / ORM
O modelo Pessoa (em pessoas/models.py) é mapeado via ORM do Django:


from django.db import models

class Pessoa(models.Model):
       SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    cpf = models.CharField(max_length=14, unique=True)
    altura = models.FloatField()
    peso = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.nome
        
👉 O Django ORM converte automaticamente:

Objeto Python ↔ Registro no PostgreSQL

🧑‍💻 Autor
Samuel Batista Fonseca
Full Stack Developer | Python + Angular


📜 Licença
Este projeto é de uso acadêmico/profissional e pode ser utilizado para estudos e testes.

