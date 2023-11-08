import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def check_win(user_cards_list, computer_cards_list):
    if sum(user_cards_list) == 21:
        print("You win!")
        return True
    elif 21 >= sum(user_cards_list) > sum(computer_cards_list):
        print("You win!")
        return True
    elif sum(user_cards_list) > 21:
        print("Bust! You lose!")
        return True
    elif sum(computer_cards_list) == 21:
        print("You lose!")
        return True
    elif 21 > sum(computer_cards_list) > sum(user_cards_list):
        print("You lose!")
        return True
    elif sum(computer_cards_list) > 21 > sum(user_cards_list):
        print("You win!")
        return True

    elif sum(user_cards_list) == sum(computer_cards_list):
        print("Tie!")
        return True


computer_cards_list = []
user_cards_list = []
game_on = True
while game_on:
    start = input('Do you want to play a game of Blackjack? Type "y" or "n":').lower()
    if start == "y":
        print(logo)
        game_on = True
        print("Welcome to the Game! BlackJack!")
        user_cards_list.append(random.choice(cards))
        user_cards_list.append(random.choice(cards))
        print(f"Your cards: {user_cards_list}")
        if sum(user_cards_list) == 21:
            print("You win!")
        else:
            computer_cards_list.append(random.choice(cards))
            print(f"Computer's cards: {computer_cards_list}")
        while sum(user_cards_list) < 21 and sum(computer_cards_list) < 21 and game_on:
            user_continues = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_continues == "n":
                computer_cards_list.append(random.choice(cards))
                print(f"Your final hand: {user_cards_list}\nComputer's final hand: {computer_cards_list}")

                game_on = False
                break
            elif user_continues == "y":
                user_next_random_number = random.choice(cards)
                if sum(user_cards_list) == 20 and user_next_random_number == cards[0]:
                    user_next_random_number = 1
                user_cards_list.append(user_next_random_number)
                print(f"Your cards: {user_cards_list}")
                computer_next_random_number = random.choice(cards)
                if sum(computer_cards_list) == 20 and computer_next_random_number == cards[0]:
                    computer_next_random_number = 1
                computer_cards_list.append(computer_next_random_number)
                print(f"Computer's cards: {computer_cards_list}")

        result = check_win(user_cards_list, computer_cards_list)
        if result:
            game_on = False
            break

    else:
        print("You chose not to play. So, we close the casino!")
        game_on = False
        break

