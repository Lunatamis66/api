# API de Usuarios com FastAPI e PostgreSQL (TimescaleDB)

API simples para listar usuarios, conectada ao PostgreSQL com TimescaleDB.

## Tecnologias

- FastAPI
- SQLAlchemy (async)
- PostgreSQL + TimescaleDB
- Docker e Docker Compose

## Endpoints

- `GET /health` - status da API
- `GET /db/ping` - teste de conexao com o banco
- `GET /users` - lista todos os usuarios

## Rodando com Docker (recomendado)

### 1) Subir API + banco

```bash
docker compose up --build -d
```

### 2) Verificar se os containers estao ativos

```bash
docker compose ps
```

### 3) Abrir documentacao Swagger

- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Inserindo dados de teste

Com o ambiente rodando, execute:

```bash
docker exec -it timescaledb psql -U postgres -d postgres -c "INSERT INTO users (name, email) VALUES ('Ana', 'ana@email.com'), ('Carlos', 'carlos@email.com');"
```

Depois teste:

- [http://127.0.0.1:8000/users](http://127.0.0.1:8000/users)

## Rodando localmente (sem Docker para a API)

### Requisitos

- Python 3.13+
- PostgreSQL/TimescaleDB rodando

### 1) Criar e ativar ambiente virtual

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Instalar dependencias

```powershell
pip install -r requirements.txt
```

### 3) Configurar variaveis de ambiente

Copie o arquivo de exemplo:

```powershell
Copy-Item .env.example .env
```

Ajuste a `DATABASE_URL` no `.env`, por exemplo:

```env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5433/postgres
```

### 4) Executar a API

```powershell
uvicorn app.main:app --reload
```

## Estrutura do projeto

```text
app/
  config.py
  database.py
  main.py
  models.py
  schemas.py
requirements.txt
docker-compose.yml
Dockerfile
```

## Publicando no GitHub

### 1) Inicializar repositorio local

```bash
git init
git add .
git commit -m "Initial commit: FastAPI users API with PostgreSQL/TimescaleDB"
```

### 2) Criar repositorio no GitHub e conectar

```bash
git branch -M main
git remote add origin <URL_DO_REPOSITORIO>
git push -u origin main
```
