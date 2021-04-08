import unittest
from src.rock_paper_scissors import *
# from src.player_class import Player ???


class TestRockPaperScissors(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Lina", "rock")
        self.player_2 = Player("Mark", "scissors")
        self.player_3 = Player("Colin", "paper")
        self.player_4 = Player("Sky", "rock")
        self.player_5 = Player("Hannah", "lizard") 
        self.player_6 = Player("Roosa", "Spock")

    def test_if_its_a_draw(self):
        self.assertEqual("It's a draw!", play_game(self.player_1, self.player_4))

    def test_if_gesture1_does_not_equal_gesture2(self):
        self.assertEqual("Rock wins!", play_game(self.player_1, self.player_2))

    def test_draw_is_declared_when_gestures_equal(self):
        self.assertEqual("It's a draw!", play_game(self.player_1, self.player_4))

    def test_rock_beats_scissors(self):
        self.assertEqual("Rock wins!", play_game(self.player_1, self.player_2))

    def test_scissors_beats_paper(self):
        self.assertEqual("Scissors wins!", play_game(self.player_2, self.player_3))

    def test_paper_beats_rock(self):
        self.assertEqual("Paper wins!", play_game(self.player_3, self.player_4))

################
#  extensions  #
################

#rock paper scissors9 lizard spock 

    def test_spock_beats_rock(self):
        self.assertEqual("Spock wins!", play_game(self.player_6, self.player_1))

    def test_spock_beats_scissors(self):
        self.assertEqual("Spock wins!", play_game(self.player_6, self.player_2))

    def test_spock_loses_to_lizard(self):
        self.assertEqual("Lizard wins!", play_game(self.player_6, self.player_5))

    def test_spock_loses_paper(self):
        self.assertEqual("Paper wins!", play_game(self.player_6, self.player_3))

    def test_lizard_beats_spock(self):
        self.assertEqual("Lizard wins!", play_game(self.player_5, self.player_6))

    def test_lizard_beats_paper(self):
        self.assertEqual("Lizard wins!", play_game(self.player_5, self.player_3))

    def test_lizard_loses_to_rock(self):
        self.assertEqual("Rock wins!", play_game(self.player_5, self.player_1))

    def test_lizard_loses_to_scissors(self):
        self.assertEqual("Scissors wins!", play_game(self.player_5, self.player_2))

