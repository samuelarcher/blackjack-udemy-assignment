from BlackjackSession import BlackjackSession
from BlackjackTable import BlackjackTable
from Dealer import Dealer
from Player import Player
import os
from SimpleGUI import SimpleGUI


def want_to_play_again():
    want_to_play = None
    valid_answer = False

    while not valid_answer:
        print("\n\n---------------------------------------------------------------\n")
        answer = SimpleGUI.ask_yes_no("Do you want to play again?")
        answer = answer[0]
        if answer is None or not (answer.lower() == 'y' or answer.lower() == 'n'):
            SimpleGUI.warn("Sorry, you must answer 'yes' or 'no'")
        if answer.lower() == 'y':
            want_to_play = True
            valid_answer = True
        elif answer.lower() == 'n':
            want_to_play = False
            valid_answer = True

    return want_to_play


def play_blackjack():
    want_to_play = True

    single_player = Player(name="Sam")
    players = [single_player]  # Currently, only one player, but think about the future

    while want_to_play:
        table = BlackjackTable()
        dealer = Dealer()

        blackjack = BlackjackSession(table, dealer, players)
        blackjack.play()

        want_to_play = want_to_play_again()

    SimpleGUI.alert("Game over. Thanks for playing!")


################
# Main Program #
################
play_blackjack()