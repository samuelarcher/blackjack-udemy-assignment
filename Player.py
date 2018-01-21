import re

from Hand import Hand
from SimpleGUI import SimpleGUI
import inspect


class Player():
    def __init__(self, name):
        self.__player_name = name
        self.__chip_count = 0
        self.__hand = Hand()

    def __str__(self):

        result = '<Player name="%s">' % (self.__player_name)
        result += "\n"
        result += str(self.__hand)
        result += "\n"
        result += "</Player>"

        return result

    def place_initial_bet(self, table):

        bet_amount = 0
        input_ok = False

        print("Line {} of file {}...".format(inspect.currentframe().f_lineno, __file__))

        while not input_ok:

            user_input = SimpleGUI.ask_text_input(
                "{}, you have ${} chips. How much would you like to bet this round?: ".
                format(self.__player_name, self.__chip_count))

            re_match = re.match("^\d+$", user_input)
            if re_match is None:
                SimpleGUI.alert("Please enter how much you'd like to bet.")
            else:
                int_val = int(user_input)
                if int_val > 0:
                    if int_val > self.__chip_count:
                        SimpleGUI.warn("Sorry, you only have %d chips!" % self.__chip_count)
                    else:
                        bet_amount = int_val
                        input_ok = True
                else:
                    SimpleGUI.alert("Please enter how much you'd like to bet.")

        table.hold_bet(self, bet_amount)

    def stand_or_hit(self):

        stand_or_hit = ""
        input_ok = False

        while not input_ok:

            user_input = SimpleGUI.ask_text_input(
                "Your hand is {}.\n{}, would you like to stand or hit?: ".
                format(self.__hand, self.__player_name))

            re_match = re.match("^(stand|hit)$", user_input, flags=re.IGNORECASE)
            if re_match is None:
                SimpleGUI.warn("Please choose to stand or hit...")
            else:
                stand_or_hit = user_input.lower()
                input_ok = True

        return stand_or_hit

    def get_name(self):
        return self.__player_name

    def is_bust(self):
        is_bust = self.get_hand_value() > 21
        return is_bust

    def is_21(self):
        is_21 = self.get_hand_value() == 21
        return is_21

    def get_hand_value(self):
        return self.__hand.get_value()

    def buy_chips(self):

        amount = 0
        input_ok = False

        while not input_ok:

            user_input = SimpleGUI.ask_text_input(
                "{}, you have {} chips. How many chips would you like to BUY this round?: ".
                format(self.__player_name, self.__chip_count))

            re_match = re.match("^\s*\d+\s*$", user_input, flags=re.IGNORECASE)
            if re_match is None:
                SimpleGUI.warn("Please enter how many chips you'd like to buy.")
            else:
                amount = int(user_input)
                input_ok = True

        self.__chip_count += amount

    def win_chips(self, amount):
        self.__chip_count += amount

    def lose_chips(self, amount):
        self.__chip_count -= amount

    def get_hand_str(self):
        return str(self.__hand)

    def receive_dealt_card(self, card):

        if self.__hand is None:
            self.__hand = Hand()

        self.__hand.add_card(card)

    def relinquish_hand(self):
        self.__hand = None

