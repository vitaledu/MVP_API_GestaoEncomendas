from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Encomenda(Base):
    __tablename__ = 'encomendas'

    id = Column(Integer, primary_key=True)
    codigo_rastreamento = Column(String, unique=True, nullable=False)
    descricao = Column(String, nullable=False)
    endereco_origem = Column(String, nullable=False)
    endereco_destino = Column(String, nullable=False)
    status = Column(String, default="Em trânsito")

DATABASE_URL = "sqlite:///./encomendas.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
