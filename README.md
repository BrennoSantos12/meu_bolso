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
- **Redoc**: `http://localhost:8000/redoc`

## Endpoints

### Usuários

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/users/` | Criar usuário |
| `GET` | `/users/` | Listar todos os usuários |
| `GET` | `/users/{user_id}` | Buscar categorias do usuário |
| `PUT` | `/users/{user_id}` | Atualizar usuário |

### Categorias

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/categories/` | Criar categoria |
| `GET` | `/categories/` | Listar todas as categorias |
| `GET` | `/categories/{category_id}` | Buscar categoria por ID |
| `GET` | `/categories/transactions/{category_id}` | Listar transações da categoria |
| `PUT` | `/categories/{category_id}` | Atualizar categoria |

### Transações

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/transactions/` | Criar transação |
| `GET` | `/transactions/` | Listar todas as transações |
| `PUT` | `/transactions/{transaction_id}` | Atualizar transação |

## Exemplos de uso

### Criar um usuário

```bash
curl -X POST http://localhost:8000/users/ \
  -H "Content-Type: application/json" \
  -d '{"nome": "João Silva", "email": "joao@email.com", "senha": "minhasenha"}'
```

### Criar uma categoria

```bash
curl -X POST http://localhost:8000/categories/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Alimentação", "user_id": 1}'
```

### Criar uma transação

```bash
curl -X POST http://localhost:8000/transactions/ \
  -H "Content-Type: application/json" \
  -d '{"description": "Supermercado", "amount": 150.00, "type": "despesa", "user_id": 1, "category_id": 1}'
```

## Estrutura do projeto

```
meu-bolso-python/
├── app/
│   ├── main.py              # Inicialização da aplicação
│   ├── database.py          # Configuração do banco de dados
│   ├── models/              # Modelos ORM (SQLAlchemy)
│   │   ├── user.py
│   │   ├── category.py
│   │   └── transaction.py
│   ├── routers/             # Rotas da API
│   │   ├── users.py
│   │   ├── categories.py
│   │   └── transactions.py
│   └── schemas/             # Schemas de validação (Pydantic)
│       ├── user.py
│       ├── category.py
│       └── transaction.py
├── alembic/                 # Migrações do banco de dados
│   ├── env.py
│   └── versions/
├── alembic.ini
├── requirements.txt
├── .env.example
└── .gitignore
```
