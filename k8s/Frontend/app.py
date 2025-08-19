import os
import psycopg2

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host="postgres-service",  # ClusterIP service for DB
    port="5432"
)
