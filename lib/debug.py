from .db import Base, engine, session
from .models import Team, Player, Coach

Base.metadata.create_all(engine)

team1 = Team(name="Pitchside FC")
coach1 = Coach(name="Coach Alex", team=team1)
player1 = Player(name="Dan Bradley", team=team1)

session.add(team1)
session.add(coach1)
session.add(player1)
session.commit()

teams = session.query(Team).all()
for t in teams:
    print(f"Team: {t.name}")
    for c in t.coaches:
        print(f" Coach: {c.name}")
    for p in t.players:
        print(f" Player: {p.name}")
