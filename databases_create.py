from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Denifinir Modelode dados

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer,primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    email = Column(String)
    # email = Column(String,primary_key=False)

engine = create_engine('sqlite:///user_db.db')

Base.metadata.create_all(engine)


