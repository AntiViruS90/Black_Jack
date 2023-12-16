import random


def create_deck():
    suits = ['♠️', '♥️', '♦️', '♣️']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck


def deal_card(deck, hand):
    card = deck.pop()  # Удаляем из колоды
    hand.append(card)  # Добавляем в руку


def calculate_hand_value(hand):
    values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
        'K': 10, 'A': 11
    }
    total = sum(values[card[0]] for card in hand)
    aces = sum(card[0] == 'A' for card in hand)
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total


def print_hand(hand, conseal_first_card=False):  # Выводит на экран карты игрока
    if conseal_first_card:
        cards = ['?', hand[1][0]]
    else:
        cards = [card[0] for card in hand]
    print(' '.join(cards))


def play_game():
    deck = create_deck()  # Включаем функцию
    player_hand = []  # Создаём пустой массив игрока
    dealer_hand = []  # Создаём пустой массив компьютера

    for _ in range(2):
        deal_card(deck, player_hand)
        deal_card(deck, dealer_hand)

    game_over = False
    print(f"Your cards: {player_hand}\nDealer's cards: {dealer_hand}")
    while not game_over:
        print('Your cards: ')
        print_hand(player_hand)
        print(f'Total sum of your cards: {calculate_hand_value(player_hand)}')

        print("Dealer's cards:")
        print_hand(dealer_hand, conseal_first_card=True)

        player_score = calculate_hand_value(player_hand)
        dealer_score = calculate_hand_value(dealer_hand)

        if player_score == 21 and len(player_hand) == 2:
            print('Black Jack! You Win!!!')
            game_over = True
        elif dealer_score == 21 and len(dealer_hand) == 2:
            print('Black Jack! Dealer Win!!!')
            game_over = True
        elif player_score > 21:
            print("Too much! You Lost...")
            game_over = True
        elif dealer_score > 21:
            print("The dealer's overdrawn. You Win!")
            game_over = True
        else:
            user_choice = input("Would you like to get another card? Enter 'yes' or 'no': ")
            if user_choice.lower() == 'yes':
                deal_card(deck, player_hand)
            else:
                game_over = True
    print("Your cards: ")
    print_hand(player_hand)
    print(f"The sum of your cards: {calculate_hand_value(player_hand)}")

    print("Dealer's cards: ")
    print_hand(dealer_hand)
    print(f"The sum of your cards: {calculate_hand_value(player_hand)}")

    if (21 >= player_score > dealer_score) or (dealer_score > 21 >= player_score):
        print("You win!")
    elif player_score == dealer_score:
        print("Tie")
    else:
        print('Dealer win!')


play_game()
