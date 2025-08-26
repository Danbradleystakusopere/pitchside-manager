
from . import crud

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
    teams = crud.get_all_teams()
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
    crud.create_team(name)
    print(f"Team '{name}' added.")

def add_player():
    team = choose_team()
    if not team: return
    player_name = input("Enter player name: ")
    crud.create_player(player_name, team)
    print(f"Player '{player_name}' added to {team.name}.")

def add_coach():
    team = choose_team()
    if not team: return
    coach_name = input("Enter coach name: ")
    crud.create_coach(coach_name, team)
    print(f"Coach '{coach_name}' added to {team.name}.")


def update_menu():
    print("\n--- Update Menu ---")
    print("1. Update Team name")
    print("2. Update Player name")
    print("3. Update Coach name")
    choice = input("Enter choice: ")

    if choice == "1":
        team = choose_team()
        if team:
            new_name = input(f"Enter new name for team '{team.name}': ")
            crud.update_team(team, new_name)
            print("Team updated.")
    elif choice == "2":
        player = choose_player()
        if player:
            new_name = input(f"Enter new name for player '{player.name}': ")
            crud.update_player(player, new_name)
            print("Player updated.")
    elif choice == "3":
        coach = choose_coach()
        if coach:
            new_name = input(f"Enter new name for coach '{coach.name}': ")
            crud.update_coach(coach, new_name)
            print("Coach updated.")


def delete_menu():
    print("\n--- Delete Menu ---")
    print("1. Delete Team")
    print("2. Delete Player")
    print("3. Delete Coach")
    choice = input("Enter choice: ")

    if choice == "1":
        team = choose_team()
        if team:
            crud.delete_team(team)
            print("Team deleted.")
    elif choice == "2":
        player = choose_player()
        if player:
            crud.delete_player(player)
            print("Player deleted.")
    elif choice == "3":
        coach = choose_coach()
        if coach:
            crud.delete_coach(coach)
            print("Coach deleted.")

def choose_team():
    teams = crud.get_all_teams()
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
    players = crud.get_all_players()
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
    coaches = crud.get_all_coaches()
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
