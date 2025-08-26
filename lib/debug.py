from .db import Base, engine, session
from .models import Team, Player


Base.metadata.create_all(engine)


team1 = Team(name="Pitchside FC")


player1 = Player(name="Dan Bradley", team=team1)
player2 = Player(name="Chris Stone", team=team1)


session.add(team1)
session.add_all([player1, player2])
session.commit()


teams = session.query(Team).all()
for t in teams:
    print(f"Team: {t.name}")
    for p in t.players:
        print(f" - Player: {p.name}")
