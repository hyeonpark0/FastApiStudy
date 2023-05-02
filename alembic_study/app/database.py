from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils.functions import database_exists, create_database

dbname = "mydb"
SQLALCHEMY_DB_URL = "mysql+mysqldb://root:admin@localhost:3306/"

if not database_exists(SQLALCHEMY_DB_URL + dbname):
    create_database(SQLALCHEMY_DB_URL + dbname)
    
engine = create_engine(SQLALCHEMY_DB_URL + dbname)

# conn = engine.connect()

# # Create database
# conn.execute("CREATE DATABASE " + dbname)
# conn.close()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()