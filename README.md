# Meu Bolso - API de Finanças Pessoais

API REST para controle de finanças pessoais, permitindo gerenciar usuários, categorias e transações financeiras.

## Tecnologias

- **Python 3.14**
- **FastAPI** - Framework web
- **SQLAlchemy** - ORM
- **Alembic** - Migrações de banco de dados
- **PostgreSQL** - Banco de dados
- **Pydantic** - Validação de dados

## Pré-requisitos

- Python 3.10+
- PostgreSQL instalado e rodando

## Instalação

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd meu-bolso-python
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Copie o arquivo de exemplo e preencha com suas credenciais:

```bash
cp .env.example .env
```

Edite o `.env`:

```env
DATABASE_URL=postgresql://seu_usuario:sua_senha@localhost:5432/meu_bolso
```

### 5. Crie o banco de dados no PostgreSQL

```bash
psql -U postgres -c "CREATE DATABASE meu_bolso;"
```

### 6. Execute as migrações

```bash
alembic upgrade head
```

### 7. Inicie o servidor

```bash
uvicorn app.main:app --reload
```

A API estará disponível em `http://localhost:8000`.

## Documentação interativa

Com o servidor rodando, acesse:

- **Swagger UI**: `http://localhost:8000/docs`
