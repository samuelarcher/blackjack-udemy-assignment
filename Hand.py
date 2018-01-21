import inspect


class Hand(object):
    ACE_LOW = 1
    ACE_HIGH = 11

    card_value_by_name = {
        "ace": ACE_HIGH,  # or 1 if it would cause a bust
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "jack": 10,
        "queen": 10,
        "king": 10
    }

    def __init__(self):
        self.__cards = []

    def __str__(self):

        result = "<Hand value='{}'>\n".format(self.get_value())

        if len(self.__cards) == 0:
            result += "\n"
        else:
            for card in self.__cards:
                result += "    "
                result += str(card)
                result += "\n"

        result += "</Hand>"

        return result

    def add_card(self, card):
        # Add card to hand
        self.__cards.append(card)

    def card_count(self):
        return len(self.__cards)

    def is_bust(self):
        return self.__get_hand_max_value() > 21

    def is_21(self):
        return self.__get_hand_max_value() == 21

    def get_value(self):
        return self.__get_hand_max_value()

    def __get_hand_max_value(self):

        temp_value = 0
        ace_count = 0

        # 'Stole' scoring logic from
        # https://brilliant.org/wiki/programming-blackjack/
        for card in self.__cards:
            card_name = card.get_name()

            temp_value += __class__.card_value_by_name[card_name]

            # Keep track of number of aces
            if card_name == "ace":
                ace_count += 1

        # Make Aces count as 1 if counting them as 11 would cause the hand to bust
        while ace_count > 0:
            if temp_value > 21:
                ace_count -= 1  # Don't want to double-count an ACE
                temp_value -= 10  # Ace becomes 1 instead of 11
            else:
                break

        return temp_value
