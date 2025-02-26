# API Handler Application

## requirements
### install requirements
```bash
pip install -r req.txt
```

### run the dependencies applications
```bash
docker-compose up --build -d
```

### initialize the Database(psql)
```bash
alembic init app/db/migrations
alembic revision --autogenerate -m "Initial migration"
```

### run the application
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## templates
### .env file template
```text
POSTGRES_DB=app
POSTGRES_PORT=5332
POSTGRES_HOST=0.0.0.0
POSTGRES_USER=postgres
POSTGRES_PASSWORD=mypassword
SECRET_KEY=sraGbRmjYQXmYdYl8Pk!OFE35UP6n/QqqpOD=iu/bUXBFSSPwnsuprP6T45Q5Ymywu2khUka!6II3Ql
DATABASE_URL=postgresql+psycopg2://postgres:mypassword@0.0.0.0:5332/app
```