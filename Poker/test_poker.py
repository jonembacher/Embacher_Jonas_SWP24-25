import unittest
from main import *


class TestPoker(unittest.TestCase):
    def setUp(self):
        self.counter = {
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

    def test_is_royal_flush(self):
        cards = {
            0: "Pik,14",  # Ass
            1: "Pik,13",  # König
            2: "Pik,12",  # Dame
            3: "Pik,11",  # Bube
            4: "Pik,10"  # 10
        }
        self.assertTrue(is_royal_flush(cards))

    def test_is_straight_flush(self):
        cards = {
            0: "Pik,9",
            1: "Pik,8",
            2: "Pik,7",
            3: "Pik,6",
            4: "Pik,5"
        }
        self.assertTrue(is_straight_flush(cards))

    def test_is_four_of_a_kind(self):
        cards = {
            0: "Pik,8",
            1: "Herz,8",
            2: "Karo,8",
            3: "Kreuz,8",
            4: "Herz,2"
        }
        self.assertTrue(is_four_of_a_kind(cards))

    def test_is_full_house(self):
        cards = {
            0: "Pik,7",
            1: "Herz,7",
            2: "Karo,7",
            3: "Kreuz,9",
            4: "Herz,9"
        }
        self.assertTrue(is_full_house(cards))

    def test_is_flush(self):
        cards = {
            0: "Pik,2",
            1: "Pik,5",
            2: "Pik,7",
            3: "Pik,9",
            4: "Pik,11"
        }
        self.assertTrue(is_flush(cards))

    def test_is_straight(self):
        cards = {
            0: "Pik,2",
            1: "Herz,3",
            2: "Karo,4",
            3: "Kreuz,5",
            4: "Herz,6"
        }
        self.assertTrue(is_straight(cards))

    def test_is_three_of_a_kind(self):
        cards = {
            0: "Pik,10",
            1: "Herz,10",
            2: "Karo,10",
            3: "Kreuz,2",
            4: "Herz,5"
        }
        self.assertTrue(is_three_of_a_kind(cards))

    def test_is_two_pairs(self):
        cards = {
            0: "Pik,6",
            1: "Herz,6",
            2: "Karo,9",
            3: "Kreuz,9",
            4: "Herz,3"
        }
        self.assertTrue(is_two_pairs(cards))

    def test_is_pair(self):
        cards = {
            0: "Pik,4",
            1: "Herz,4",
            2: "Karo,7",
             3: "Kreuz,2",
            4: "Herz,9"
        }
        self.assertTrue(is_pair(cards))


if __name__ == '__main__':
    unittest.main()
