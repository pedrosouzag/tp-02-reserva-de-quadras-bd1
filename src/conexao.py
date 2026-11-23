import psycopg2

DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "alocacao_quadras"
DB_USER = "postgres"


def conectar():
    senha = input("Senha do PostgreSQL: ")
    return psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=senha)

