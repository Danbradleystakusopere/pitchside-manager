from . import crud
from colorama import Fore, Style, init # type: ignore

init(autoreset=True)

def main_menu():
    while True:
        print(Fore.CYAN + "\n--- Pitch Side Manager ---" + Style.RESET_ALL)
        print(Fore.YELLOW + "1. View all teams" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. Add a new team" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. Add a player to a team" + Style.RESET_ALL)
        print(Fore.YELLOW + "4. Add a coach to a team" + Style.RESET_ALL)
        print(Fore.YELLOW + "5. Update a team/coach/player" + Style.RESET_ALL)
        print(Fore.YELLOW + "6. Delete a team/coach/player" + Style.RESET_ALL)
        print(Fore.YELLOW + "7. Exit" + Style.RESET_ALL)

        choice = input(Fore.CYAN + "Enter choice: " + Style.RESET_ALL)

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
            print(Fore.GREEN + "Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice, try again." + Style.RESET_ALL)


def view_teams():
    teams = crud.get_all_teams()
    if not teams:
        print(Fore.RED + "No teams found." + Style.RESET_ALL)
        return
    for t in teams:
        print(Fore.CYAN + f"\nTeam: {t.name}" + Style.RESET_ALL)
        for c in t.coaches:
            print(Fore.MAGENTA + f"  Coach: {c.name}" + Style.RESET_ALL)
        for p in t.players:
            print(Fore.BLUE + f"  Player: {p.name}" + Style.RESET_ALL)


def add_team():
    name = input(Fore.CYAN + "Enter team name: " + Style.RESET_ALL)
    crud.create_team(name)
    print(Fore.GREEN + f"Team '{name}' added." + Style.RESET_ALL)


def add_player():
    team = choose_team()
    if not team: return
    player_name = input(Fore.CYAN + "Enter player name: " + Style.RESET_ALL)
    crud.create_player(player_name, team)
    print(Fore.GREEN + f"Player '{player_name}' added to {team.name}." + Style.RESET_ALL)


def add_coach():
    team = choose_team()
    if not team: return
    coach_name = input(Fore.CYAN + "Enter coach name: " + Style.RESET_ALL)
    crud.create_coach(coach_name, team)
    print(Fore.GREEN + f"Coach '{coach_name}' added to {team.name}." + Style.RESET_ALL)


def update_menu():
    print(Fore.CYAN + "\n--- Update Menu ---" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Update Team name" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Update Player name" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Update Coach name" + Style.RESET_ALL)
    choice = input(Fore.CYAN + "Enter choice: " + Style.RESET_ALL)

    if choice == "1":
        team = choose_team()
        if team:
            new_name = input(Fore.CYAN + f"Enter new name for team '{team.name}': " + Style.RESET_ALL)
            crud.update_team(team, new_name)
            print(Fore.GREEN + "Team updated." + Style.RESET_ALL)
    elif choice == "2":
        player = choose_player()
        if player:
            new_name = input(Fore.CYAN + f"Enter new name for player '{player.name}': " + Style.RESET_ALL)
            crud.update_player(player, new_name)
            print(Fore.GREEN + "Player updated." + Style.RESET_ALL)
    elif choice == "3":
        coach = choose_coach()
        if coach:
            new_name = input(Fore.CYAN + f"Enter new name for coach '{coach.name}': " + Style.RESET_ALL)
            crud.update_coach(coach, new_name)
            print(Fore.GREEN + "Coach updated." + Style.RESET_ALL)


def delete_menu():
    print(Fore.CYAN + "\n--- Delete Menu ---" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Delete Team" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Delete Player" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Delete Coach" + Style.RESET_ALL)
    choice = input(Fore.CYAN + "Enter choice: " + Style.RESET_ALL)

    if choice == "1":
        team = choose_team()
        if team:
            crud.delete_team(team)
            print(Fore.RED + "Team deleted." + Style.RESET_ALL)
    elif choice == "2":
        player = choose_player()
        if player:
            crud.delete_player(player)
            print(Fore.RED + "Player deleted." + Style.RESET_ALL)
    elif choice == "3":
        coach = choose_coach()
        if coach:
            crud.delete_coach(coach)
            print(Fore.RED + "Coach deleted." + Style.RESET_ALL)


def choose_team():
    teams = crud.get_all_teams()
    if not teams:
        print(Fore.RED + "No teams found." + Style.RESET_ALL)
        return None
    for i, t in enumerate(teams, 1):
        print(Fore.YELLOW + f"{i}. {t.name}" + Style.RESET_ALL)
    choice = int(input(Fore.CYAN + "Select team number: " + Style.RESET_ALL))
    if choice < 1 or choice > len(teams):
        print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
        return None
    return teams[choice - 1]


def choose_player():
    players = crud.get_all_players()
    if not players:
        print(Fore.RED + "No players found." + Style.RESET_ALL)
        return None
    for i, p in enumerate(players, 1):
        print(Fore.YELLOW + f"{i}. {p.name} (Team: {p.team.name})" + Style.RESET_ALL)
    choice = int(input(Fore.CYAN + "Select player number: " + Style.RESET_ALL))
    if choice < 1 or choice > len(players):
        print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
        return None
    return players[choice - 1]


def choose_coach():
    coaches = crud.get_all_coaches()
    if not coaches:
        print(Fore.RED + "No coaches found." + Style.RESET_ALL)
        return None
    for i, c in enumerate(coaches, 1):
        print(Fore.YELLOW + f"{i}. {c.name} (Team: {c.team.name})" + Style.RESET_ALL)
    choice = int(input(Fore.CYAN + "Select coach number: " + Style.RESET_ALL))
    if choice < 1 or choice > len(coaches):
        print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
        return None
    return coaches[choice - 1]


if __name__ == "__main__":
    main_menu()
