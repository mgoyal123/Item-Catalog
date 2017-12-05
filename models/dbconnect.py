from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from database_setup import Game, Base, GameItem, User

# Connect to Database and create database session
engine = create_engine('sqlite:///gamecatalogwithusers.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
