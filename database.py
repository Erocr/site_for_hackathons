from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData


metadata = MetaData()


def get_metadata():
    return metadata


def new_engine():
    with open("database_key.txt") as file:
        SQLALCHEMY_DATABASE_URL = file.read()

    return create_engine(SQLALCHEMY_DATABASE_URL)


Base = declarative_base()

Soumission = Table("Soumission", metadata,
                   Column("id", Integer, primary_key=True),
                   Column("heure", DateTime),
                   Column("code", String),
                   Column("score", Float)
                   )

Personne = Table("Personne", metadata,
                 Column("id", Integer, primary_key=True),  # Maybe put mail, or n°etudiant instead
                 Column("nom", String)
                 )

Exercice = Table("Exercice", metadata,
                 Column("id", Integer, primary_key=True),
                 Column("nom", String))

Hackathon = Table("Hackathon", metadata,
                  Column("id", Integer, primary_key=True),
                  Column("date_deb", DateTime),
                  Column("date_fin", DateTime),
                  )
