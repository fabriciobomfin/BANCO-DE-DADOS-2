from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# URL de conexão para BD(Banco de Dados) MySQL.
DARABASE_URL = f"mysql+pymysql://usuario:senha@host:porta/nome_bd"