"""Tests for rock, paper, scissors game"""

import pytest

import rock_paper_scissors

POSSIBLE_GUESSES = ['rock', 'paper', 'scissors']

def test_get_guess_returns_valid_result():
    assert rock_paper_scissors.get_computer_guess() in POSSIBLE_GUESSES

def test_human_guess_is_valid_when_rock_is_chosen():
    assert rock_paper_scissors.is_human_guess_valid(1)

def test_human_guess_is_valid_when_paper_is_chosen():
    assert rock_paper_scissors.is_human_guess_valid(2)

def test_human_guess_is_valid_when_scissors_is_chosen():
    assert rock_paper_scissors.is_human_guess_valid(3)

def test_invalid_number_entered_by_human_causes_error():
    assert rock_paper_scissors.is_human_guess_valid(4) == False

def test_string_entered_by_human_causes_exception():
    with pytest.raises(ValueError):
        rock_paper_scissors.is_human_guess_valid("hello")

def test_human_rock_computer_rock_noone_wins():
    assert rock_paper_scissors.get_winner("rock", "rock") == "It's a draw!"

def test_human_rock_computer_paper_computer_wins():
    assert rock_paper_scissors.get_winner("rock", "paper") == "Computer wins!"

def test_human_rock_computer_scissors_human_wins():
    assert rock_paper_scissors.get_winner("rock", "scissors") == "You win!"

def test_human_paper_computer_rock_human_wins():
    assert rock_paper_scissors.get_winner("paper", "rock") == "You win!"

def test_human_paper_computer_paper_noone_wins():
    assert rock_paper_scissors.get_winner("paper", "paper") == "It's a draw!"

def test_human_paper_computer_scissors_computer_wins():
    assert rock_paper_scissors.get_winner("paper", "scissors") == "Computer wins!"

def test_human_scissors_computer_rock_computer_wins():
    assert rock_paper_scissors.get_winner("scissors", "rock") == "Computer wins!"

def test_human_scissors_computer_paper_human_wins():
    assert rock_paper_scissors.get_winner("scissors", "paper") == "You win!"

def test_human_scissors_computer_scissors_noone_wins():
    assert rock_paper_scissors.get_winner("scissors", "scissors") == "It's a draw!"
