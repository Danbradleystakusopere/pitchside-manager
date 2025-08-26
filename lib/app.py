# app.py
from .db import session
from .models import Team, Player, Coach

def main_menu():
    while True:
        print("\n--- Pitch Side Manager ---")
        print("1. View all teams")
        print("2. Add a new team")
        print("3. Add a player to a team")
        print("4. Add a coach to a team")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            view_teams()
        elif choice == "2":
            add_team()
        elif choice == "3":
            add_player()
        elif choice == "4":
            add_coach()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

def view_teams():
    teams = session.query(Team).all()
    if not teams:
        print("No teams found.")
        return
    for t in teams:
        print(f"\nTeam: {t.name}")
        for c in t.coaches:
            print(f"  Coach: {c.name}")
        for p in t.players:
            print(f"  Player: {p.name}")

def add_team():
    name = input("Enter team name: ")
    team = Team(name=name)
    session.add(team)
    session.commit()
    print(f"Team '{name}' added.")

def add_player():
    teams = session.query(Team).all()
    if not teams:
        print("No teams found. Add a team first.")
        return
    print("\nAvailable Teams:")
    for i, t in enumerate(teams, 1):
        print(f"{i}. {t.name}")

    choice = int(input("Select team number: "))
    if choice < 1 or choice > len(teams):
        print("Invalid choice.")
        return
    team = teams[choice - 1]

    player_name = input("Enter player name: ")
    player = Player(name=player_name, team=team)
    session.add(player)
    session.commit()
    print(f"Player '{player_name}' added to {team.name}.")

def add_coach():
    teams = session.query(Team).all()
    if not teams:
        print("No teams found. Add a team first.")
        return
    print("\nAvailable Teams:")
    for i, t in enumerate(teams, 1):
        print(f"{i}. {t.name}")

    choice = int(input("Select team number: "))
    if choice < 1 or choice > len(teams):
        print("Invalid choice.")
        return
    team = teams[choice - 1]

    coach_name = input("Enter coach name: ")
    coach = Coach(name=coach_name, team=team)
    session.add(coach)
    session.commit()
    print(f"Coach '{coach_name}' added to {team.name}.")

if __name__ == "__main__":
    main_menu()
