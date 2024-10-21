import random
from collections import Counter


def evaluation(cards):
    print("Evaluating cards:", cards)
    check_pair(cards)


def check_pair(hand):
    values = [card.split(",")[1] for card in hand.values()]
    counts = Counter(values)
    pairs = [value for value, count in counts.items() if count >= 2]
    if pairs:
        print(f"Es gibt ein Paar: {pairs}")
    else:
        print("Es gibt kein Paar.")


def draw(deck, amount):
    shuffled_deck = list(deck.values())
    random.shuffle(shuffled_deck)
    drawn_cards = {i: shuffled_deck[i] for i in range(amount)}
    evaluation(drawn_cards)


def main():
    farben = ("Herz", "Karo", "Pik", "Kreuz")
    zahlen = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass")
    deck = {i: farbe + "," + zahl for i, (farbe, zahl) in enumerate((f, z) for f in farben for z in zahlen)}
    draw(deck, 5)


if __name__ == "__main__":
    main()
