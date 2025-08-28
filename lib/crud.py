from .db import session
from .models import Team, Player, Coach, Match, Result

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

def create_match(home_team, away_team, home_score=0, away_score=0):
    match = Match(home_team=home_team, away_team=away_team,
                  home_score=home_score, away_score=away_score)
    session.add(match)
    session.commit()

    
    if home_score > away_score:
        result = Result(match=match, winner=home_team.name, loser=away_team.name, draw="No")
    elif away_score > home_score:
        result = Result(match=match, winner=away_team.name, loser=home_team.name, draw="No")
    else:
        result = Result(match=match, winner="None", loser="None", draw="Yes")

    session.add(result)
    session.commit()
    return match

def get_all_teams():
    return session.query(Team).all()

def get_all_players():
    return session.query(Player).all()

def get_all_coaches():
    return session.query(Coach).all()

def get_all_matches():
    return session.query(Match).all()

def get_all_results():
    return session.query(Result).all()

# -------------------------
# UPDATE
# -------------------------
def update_team(team, new_name):
    team.name = new_name
    session.commit()

def update_player(player, new_name):
    player.name = new_name
    session.commit()

def update_coach(coach, new_name):
    coach.name = new_name
    session.commit()

def update_match(match, home_score, away_score):
    match.home_score = home_score
    match.away_score = away_score
    session.commit()

    
    if home_score > away_score:
        match.result.winner = match.home_team.name
        match.result.loser = match.away_team.name
        match.result.draw = "No"
    elif away_score > home_score:
        match.result.winner = match.away_team.name
        match.result.loser = match.home_team.name
        match.result.draw = "No"
    else:
        match.result.winner = "None"
        match.result.loser = "None"
        match.result.draw = "Yes"
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

def delete_match(match):
    if match.result:
        session.delete(match.result)
    session.delete(match)
    session.commit()
