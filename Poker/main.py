import random
from collections import Counter


def evaluation(cards, counter):
    if is_royal_flush(cards):
        counter["royal_flush"] += 1
    elif is_straight_flush(cards):
        counter["straight_flush"] += 1
    elif is_four_of_a_kind(cards):
        counter["four_of_a_kind"] += 1
    elif is_full_house(cards):
        counter["full_house"] += 1
    elif is_flush(cards):
        counter["flush"] += 1
    elif is_straight(cards):
        counter["straight"] += 1
    elif is_three_of_a_kind(cards):
        counter["three_of_a_kind"] += 1
    elif is_two_pairs(cards):
        counter["two_pair"] += 1
    elif is_pair(cards):
        counter["pair"] += 1
    return counter


def is_pair(cards):
    values = [card.split(",")[1] for card in cards.values()]
    counts = Counter(values)
    return sum(1 for count in counts.values() if count == 2) == 1


def is_two_pairs(cards):
    values = [card.split(",")[1] for card in cards.values()]
    counts = Counter(values)
    return sum(1 for count in counts.values() if count == 2) == 2


def is_three_of_a_kind(cards):
    values = [card.split(",")[1] for card in cards.values()]
    counts = Counter(values)
    return 3 in counts.values()


def is_four_of_a_kind(cards):
    values = [card.split(",")[1] for card in cards.values()]
    counts = Counter(values)
    return 4 in counts.values()


def is_full_house(cards):
    values = [card.split(",")[1] for card in cards.values()]
    counts = Counter(values)
    return 3 in counts.values() and 2 in counts.values()


def is_flush(cards):
    suits = [card.split(",")[0] for card in cards.values()]
    return len(set(suits)) == 1


def is_straight(cards):
    card_values = sorted(int(card.split(",")[1]) for card in cards.values())
    # normal Straight
    if all(card_values[i] + 1 == card_values[i + 1] for i in range(len(card_values) - 1)):
        return True
    # Wheel Straight
    return card_values == [2, 3, 4, 5, 14]


def is_straight_flush(cards):
    return is_flush(cards) and is_straight(cards)


def is_royal_flush(cards):
    card_values = [int(card.split(",")[1]) for card in cards.values()]
    if is_straight_flush(cards) and sorted(card_values) == [10, 11, 12, 13, 14]:
        return True
    return False


def draw(deck, card_num, counter):
    drawn_cards = random.sample(list(deck.values()), card_num)
    drawn_cards = {i: drawn_cards[i] for i in range(len(drawn_cards))}
    counter = evaluation(drawn_cards, counter)
    return counter


def how_many():
    number = input("How many cards would you like to draw?")
    return int(number)


def conclusion(counter, probabilities, draws):  #Formatierung mit ChatGPT für schönere Ausgabe
    for variant, count in counter.items():
        print(f"{'Hand':<20} {'Count':<10} {'Probability (%)':<20} {'Expected (%)':<20} {'Difference':<10}")
        if variant in probabilities:
            observed_prob = (count / draws) * 100
            expected_prob = probabilities[variant] * 100
            difference = observed_prob - expected_prob
            print(f"{variant:<20} {count:<10} {observed_prob:<20.2f} {expected_prob:<20.2f} {difference:<10.2f}")
        else:
            print(f"{variant:<20} {count:<10} {'N/A':<20} {'N/A':<20} {'N/A':<10}")
        print("-" * 80)


def main():
    colours = ("Herz", "Karo", "Pik", "Kreuz")
    values = range(2, 15)
    deck = {i: f"{col},{val}" for i, (col, val) in enumerate((c, v) for c in colours for v in values)}
    counter = {
        "pair": 0,
        "two_pair": 0,
        "three_of_a_kind": 0,
        "straight": 0,
        "flush": 0,
        "full_house": 0,
        "four_of_a_kind": 0,
        "straight_flush": 0,
        "royal_flush": 0
    }
    possibility = {
        "pair": 0.4225,
        "two_pair": 0.0475,
        "three_of_a_kind": 0.0211,
        "straight": 0.0039,
        "flush": 0.002,
        "full_house": 0.0014,
        "four_of_a_kind": 0.00024,
        "straight_flush": 0.00000139,
        "royal_flush": 0.00000154
    }
    draws = how_many()
    for _ in range(draws):  # Anzahl der Simulationen
        counter = draw(deck, 5, counter)
    conclusion(counter, possibility, draws)
    #print(counter)


if __name__ == "__main__":
    main()
