from .db import session
from .models import Team, Player, Coach


def create_team(name):
    team = Team(name=name)
    session.add(team)
    session.commit()
    return team

def create_player(name, team):
    player = Player(name=name, team=team)
    session.add(player)
    session.commit()
    return player

def create_coach(name, team):
    coach = Coach(name=name, team=team)
    session.add(coach)
    session.commit()
    return coach


def get_all_teams():
    return session.query(Team).all()

def get_all_players():
    return session.query(Player).all()

def get_all_coaches():
    return session.query(Coach).all()


def update_team(team, new_name):
    team.name = new_name
    session.commit()

def update_player(player, new_name):
    player.name = new_name
    session.commit()

def update_coach(coach, new_name):
    coach.name = new_name
    session.commit()


def delete_team(team):
    session.delete(team)
    session.commit()

def delete_player(player):
    session.delete(player)
    session.commit()

def delete_coach(coach):
    session.delete(coach)
    session.commit()
