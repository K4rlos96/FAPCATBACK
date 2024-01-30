from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

usuario = "postgres"
contraseña = "Pafcat2024"
servidor = "pafcat-1.cty8aw0eanev.us-east-1.rds.amazonaws.com"
puerto = "5432"
base_de_datos = "postgres"

SQLALCHEMY_DATABASE_URL = f"postgresql://{usuario}:{contraseña}@{servidor}:{puerto}/{base_de_datos}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
