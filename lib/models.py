
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    players = relationship("Player", back_populates="team")
    coaches = relationship("Coach", back_populates="team")

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    team_id = Column(Integer, ForeignKey("teams.id"))
    team = relationship("Team", back_populates="players")

class Coach(Base):
    __tablename__ = "coaches"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    team_id = Column(Integer, ForeignKey("teams.id"))
    team = relationship("Team", back_populates="coaches")
