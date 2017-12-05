from sqlalchemy import Column, ForeignKey, String, Integer, create_engine
from sqlalchemy import UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    picture = Column(String(250), nullable=False)
    email = Column(String(250))


class Game(Base):
    __tablename__ = "game"
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    __table_args__ = (UniqueConstraint('name'),
                      )

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
                }


class GameItem(Base):
    """docstring for GameItem"""
    __tablename__ = "gameitem"
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    game_id = Column(Integer, ForeignKey('game.id'))
    game = relationship(Game)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    __table_args__ = (UniqueConstraint('name', 'game_id',
                      name='_game_item_uc'),
                      )

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'description': self.description,
                }


engine = create_engine('sqlite:///gamecatalogwithusers.db')
Base.metadata.create_all(engine)
