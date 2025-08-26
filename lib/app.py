
from .db import session
from .models import Team, Player, Coach

def main_menu():
    while True:
        print("\n--- Pitch Side Manager ---")
        print("1. View all teams")
        print("2. Add a new team")
        print("3. Add a player to a team")
        print("4. Add a coach to a team")
        print("5. Update a team/coach/player")
        print("6. Delete a team/coach/player")
        print("7. Exit")

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
            update_menu()
        elif choice == "6":
            delete_menu()
        elif choice == "7":
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
    team = choose_team()
    if not team: return
    player_name = input("Enter player name: ")
    player = Player(name=player_name, team=team)
    session.add(player)
    session.commit()
    print(f"Player '{player_name}' added to {team.name}.")

def add_coach():
    team = choose_team()
    if not team: return
    coach_name = input("Enter coach name: ")
    coach = Coach(name=coach_name, team=team)
    session.add(coach)
    session.commit()
    print(f"Coach '{coach_name}' added to {team.name}.")


def update_menu():
    print("\n--- Update Menu ---")
    print("1. Update Team name")
    print("2. Update Player name")
    print("3. Update Coach name")
    choice = input("Enter choice: ")

    if choice == "1":
        update_team()
    elif choice == "2":
        update_player()
    elif choice == "3":
        update_coach()

def update_team():
    team = choose_team()
    if not team: return
    new_name = input(f"Enter new name for team '{team.name}': ")
    team.name = new_name
    session.commit()
    print("Team updated.")

def update_player():
    player = choose_player()
    if not player: return
    new_name = input(f"Enter new name for player '{player.name}': ")
    player.name = new_name
    session.commit()
    print("Player updated.")

def update_coach():
    coach = choose_coach()
    if not coach: return
    new_name = input(f"Enter new name for coach '{coach.name}': ")
    coach.name = new_name
    session.commit()
    print("Coach updated.")


def delete_menu():
    print("\n--- Delete Menu ---")
    print("1. Delete Team")
    print("2. Delete Player")
    print("3. Delete Coach")
    choice = input("Enter choice: ")

    if choice == "1":
        delete_team()
    elif choice == "2":
        delete_player()
    elif choice == "3":
        delete_coach()

def delete_team():
    team = choose_team()
    if not team: return
    session.delete(team)
    session.commit()
    print("Team deleted (along with its players and coaches).")

def delete_player():
    player = choose_player()
    if not player: return
    session.delete(player)
    session.commit()
    print("Player deleted.")

def delete_coach():
    coach = choose_coach()
    if not coach: return
    session.delete(coach)
    session.commit()
    print("Coach deleted.")


def choose_team():
    teams = session.query(Team).all()
    if not teams:
        print("No teams found.")
        return None
    for i, t in enumerate(teams, 1):
        print(f"{i}. {t.name}")
    choice = int(input("Select team number: "))
    if choice < 1 or choice > len(teams):
        print("Invalid choice.")
        return None
    return teams[choice - 1]

def choose_player():
    players = session.query(Player).all()
    if not players:
        print("No players found.")
        return None
    for i, p in enumerate(players, 1):
        print(f"{i}. {p.name} (Team: {p.team.name})")
    choice = int(input("Select player number: "))
    if choice < 1 or choice > len(players):
        print("Invalid choice.")
        return None
    return players[choice - 1]

def choose_coach():
    coaches = session.query(Coach).all()
    if not coaches:
        print("No coaches found.")
        return None
    for i, c in enumerate(coaches, 1):
        print(f"{i}. {c.name} (Team: {c.team.name})")
    choice = int(input("Select coach number: "))
    if choice < 1 or choice > len(coaches):
        print("Invalid choice.")
        return None
    return coaches[choice - 1]

if __name__ == "__main__":
    main_menu()
