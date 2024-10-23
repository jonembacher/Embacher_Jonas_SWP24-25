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


def evaluation(middel, my_cards):
    cards = my_cards and middel
    # print("Evaluating cards:", cards)
    check_pairs(cards)
    flush(cards, True)
    straight(cards)


def check_pairs(cards):
    values = [card.split(",")[1] for card in cards.values()]
    counts = Counter(values)
    pairs = [value for value, count in counts.items() if count >= 2]
    three_of_a_kind = [value for value, count in counts.items() if count >= 3]
    four_of_a_kind = [value for value, count in counts.items() if count >= 4]
    if pairs:
        if four_of_a_kind:
            counter["full_house"] += 1
            # print(f"Fullhouse: {three_of_a_kind} {pairs}")
        elif len(pairs) == 2 and three_of_a_kind:
            counter["four_of_a_kind"] += 1
            # print(f"Four Of a kind: {four_of_a_kind}")
        elif three_of_a_kind:
            counter["three_of_a_kind"] += 1
            # print(f"Three Of a kind: {three_of_a_kind}")
        elif len(pairs) == 2:
            counter["two_pair"] += 1
            # print(f"Two Pairs: {pairs}")
        else:
            counter["pair"] += 1
            # print(f"Es gibt ein Paar {pairs}")


def flush(cards, is_flush):
    values = [card.split(",")[0] for card in cards.values()]
    # print("Flushing cards:", values)
    counts = Counter(values)
    flush_value = [value for value, count in counts.items() if count >= 5]
    if flush_value and is_flush:
        counter["flush"] += 1
        return True
        # print("Flush cards:", flush_value)


def straight(cards):
    zahlen = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass")
    card_values = [card.split(",")[1] for card in cards.values()]
    card_values = set(card_values)  # keine doppelten Werte
    sorted_cards = sorted(card_values, key=lambda x: zahlen.index(x))
    if len(card_values) < 5:
        return False

    for i in range(len(sorted_cards) - 4):
        start_index = zahlen.index(sorted_cards[i])
        if sorted_cards[i:i + 5] == list(zahlen[start_index:start_index + 5]):
            if 'Ass' in sorted_cards[i:i + 5] and flush(cards, False):
                counter["royal_flush"] += 1
            elif flush(cards,False):
                counter["straight_flush"] += 1
            else:
                counter["straight"] += 1


def draw(deck, middel, own):
    shuffled_deck = list(deck.values())
    random.shuffle(shuffled_deck)
    drawn_cards = {i: shuffled_deck[i] for i in range(middel + own)}
    my_cards = {i: drawn_cards[i] for i in range(own)}
    cards = {i: drawn_cards[i] for i in range(own)}
    evaluation(drawn_cards, my_cards)


def main():
    farben = ("Herz", "Karo", "Pik", "Kreuz")
    zahlen = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass")
    deck = {i: farbe + "," + zahl for i, (farbe, zahl) in enumerate((f, z) for f in farben for z in zahlen)}
    for _ in range(1000):
        draw(deck, 5, 2)

    print(counter)


if __name__ == "__main__":
    main()
