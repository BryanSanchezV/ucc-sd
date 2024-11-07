from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@db/postgres"

engine = create_engine(DATABASE_URL)
metadata = MetaData()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

@app.get("/data")
def read_data():
    with engine.connect() as connection:
        result = connection.execute("SELECT * FROM mytable")
        data = [dict(row) for row in result]
    return data
