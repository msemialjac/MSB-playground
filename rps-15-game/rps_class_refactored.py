import random
from read_csv_refactored import outcomes_csv, rolls_csv

rolls_list = rolls_csv
outcomes = outcomes_csv
roller = [[idx, rol] for idx, rol in enumerate(rolls_list, start=1)]


def main():
    print_header()
    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("Computer")

    game_loop(player1, player2, rolls)


def game_loop(player1, player2, rolls):
    count = 0
    p1_wins = 0
    p2_wins = 0
    while count < 3:
        p2_roll = random.choice(rolls)
        possible_rolls()
        try:
            p1_roll = rolls[int(input(f"What is your role {player1.name}: ").strip().lower()) - 1]
        except IndexError:
            print("You can only choose 1-15")
            print()
            continue
        except ValueError:
            print("You can only choose whole numbers between 1-15. Text is not allowed!")
            print()
            continue

        # display throws
        print(f"{player1.name} rolls {p1_roll.name}")
        print(f"{player2.name} rolls {p2_roll.name}")

        # draw - roll again
        if p1_roll.name == p2_roll.name:
            print("It is a tie! Roll again")
            print(f"Current score: {player1.name}: {p1_wins} vs. {player2.name}: {p2_wins} ")
            print()
            continue

        outcome = p1_roll.can_defeat(p2_roll.name)
        if not outcome:
            print(f"{player2.name} wins the round!")
            p2_wins += 1
            print()
            if p2_wins >= 2:
                break
        elif outcome:
            print(f"{player1.name} wins the round!")
            p1_wins += 1
            print()
            if p1_wins >= 2:
                break

        # display winner for this round
        print(f"Current score: {player1.name}: {p1_wins} vs. {player2.name}: {p2_wins} ")
        count += 1

    # Compute who won
    if p2_wins >= 2:
        print(f"{player2.name} wins with score {p2_wins}:{p1_wins}")
    elif p1_wins >= 2:
        print(f"{player1.name} wins with score {p1_wins}:{p2_wins}")


def possible_rolls():
    print(f"Possible rolls: ")
    i = len(roller)
    for _ in roller:
        print(f"{roller[len(roller)-i][0]}. {roller[len(roller)-i][1]}")
        i -= 1
    print()


def print_header():
    print("---------------------------------------------------")
    print("         Rock-Paper-Scissors class version Game")
    print("---------------------------------------------------")


def build_the_three_rolls():
    build_rolls = []
    for r in rolls_list:
        build_rolls.append(Roll(r))
    return build_rolls


def get_players_name():
    name = input("What is your name, player? ").strip().title()
    return name


class Roll:
    def __init__(self, name):
        self.name = name

    def can_defeat(self, roll):
        return roll in outcomes[self.name]["defeats"]

    def defeated_by(self, roll):  # This is unused - it was in the task, but I ended up not using it
        return roll in outcomes[self.name]["defeated_by"]


class Player:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    main()
