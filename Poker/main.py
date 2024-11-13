import random
from collections import Counter

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

colour = ("Herz", "Karo", "Pik", "Kreuz")
value = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass")


def evaluation(cards):
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


def is_pair(cards):
    values = [card.split(",")[1] for card in cards.values()]
    counts = Counter(values)
    pair = [val for val, count in counts.items() if count == 2]
    if len(pair) == 1:
        return True


def is_two_pairs(cards):
    values = [card.split(",")[1] for card in cards.values()]
    counts = Counter(values)
    pairs = [val for val, count in counts.items() if count == 2]
    if len(pairs) == 2:
        return True


def is_three_of_a_kind(cards):
    values = [card.split(",")[1] for card in cards.values()]
    counts = Counter(values)
    three_of_kind = [val for val, count in counts.items() if count == 3]
    if three_of_kind:
        return True


def is_four_of_a_kind(cards):
    values = [card.split(",")[1] for card in cards.values()]
    counts = Counter(values)
    four_of_kind = [val for val, count in counts.items() if count == 4]
    if four_of_kind:
        return True


def is_full_house(cards):
    if is_three_of_a_kind(cards) and is_pair(cards):
        return True


def is_flush(cards):
    values = [card.split(",")[0] for card in cards.values()]
    return len(set(values)) == 1


def is_straight(cards):
    card_values = [card.split(",")[1] for card in cards.values()]
    sorted_cards = sorted(card_values, key=lambda x: value.index(x))

    start_index = value.index(sorted_cards[0])
    if sorted_cards == list(value[start_index:start_index + len(sorted_cards)]):
        return True


def is_straight_flush(cards):
    if is_flush(cards) and is_straight(cards):
        return True


def is_royal_flush(cards):
    if is_straight_flush(cards) and 'Ass' in cards:
        return True


def draw(deck, card_num):
    shuffled_deck = list(deck.values())
    random.shuffle(shuffled_deck)
    drawn_cards = {i: shuffled_deck[i] for i in range(card_num)}
    evaluation(drawn_cards)


def main():
    deck = {i: col + "," + val for i, (col, val) in enumerate((f, z) for f in colour for z in value)}
    for _ in range(10000):
        draw(deck, 5)

    print(counter)


if __name__ == "__main__":
    main()
