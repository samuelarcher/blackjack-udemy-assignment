from random import shuffle

from Hand import Hand
from Card import Card
from SimpleGUI import SimpleGUI
import inspect


class Dealer():

    def __init__(self):

        self.__hand = Hand()
        self.__deck = []

        # The dealer has a ridiculous number of chips, however much that may be
        self.__chip_count = 1000000000000

        self.__shuffle_deck()

    def __str__(self):

        result = "<Dealer>"

        result += "\n"
        result += str(self.__hand)
        result += "\n"

        result += "<Deck num_cards='%s'>\n" % (len(self.__deck))
        for card in self.__deck:
            result += "    "
            result += str(card)
            result += "\n"
        result += "</Deck>"

        result += "</Dealer>"

        return result

    def deal_card_to_player(self, player, face_up=True):
        next_card = self.__get_next_card()

        if face_up:
            next_card.turn_face_up()

        # print("Dealing card to player {}: {}".format(player.get_name(), next_card))

        player.receive_dealt_card(next_card)

    def deal_card_to_self(self, face_up=True):

        next_card = self.__get_next_card()

        if face_up:
            next_card.turn_face_up()

        if self.__hand is None:
            self.__hand = Hand()

        self.__hand.add_card(next_card)

    def stand_or_hit_according_to_house_rules(self):
        """
        After all boxes have finished playing, the dealer's hand is resolved by
        drawing cards until the hand busts or achieves a value of 17 or higher
        (a dealer total of 17 including an ace, or "soft 17", must be drawn to
        in some games and must stand in others)
        """
        hand = self.__hand

        while hand.get_value() < 17:
            self.deal_card_to_self()

    def get_player_moves(self, player):

        finished_making_moves = False

        while not finished_making_moves:
            stand_or_hit = player.stand_or_hit()

            if stand_or_hit == 'hit':
                self.deal_card_to_player(player)

            finished_making_moves = player.get_hand_value() >= 21 or stand_or_hit == 'stand'

        return

    def lose_chips(self, amount):
        pass

    def win_chips(self, amount):
        pass

    def settle_round(self, table, players):

        msg = "Dealer has hand {}\n".format(self.__hand)

        if self.is_bust():
            # Dealer busted -- pay players who didn't bust

            msg += "\nDealer is BUST"

            # Pay players who didn't bust
            for player in players:
                if not player.is_bust():
                    # Win chips
                    player_bet = table.get_bet_amount(player)
                    player.win_chips(player_bet)
                    self.lose_chips(player_bet)
                    msg += "\nPlayer {} with hand {} wins {} chips!".\
                        format(player.get_name(), player.get_hand_str(), player_bet)

        elif self.is_21():
            # Dealer has blackjack/21 -- pick up cash from those who don't also have 21
            msg += "\nDealer has BLACKJACK"

            # Win chips from players who are not blackjack
            for player in players:
                if not player.is_21():
                    player_bet = table.get_bet_amount(player)
                    self.win_chips(player_bet)
                    player.lose_chips(player_bet)
                    msg += "\nPlayer {} with hand {} loses {} chips to the dealer.".\
                        format(player.get_name(), player.get_hand_str(), player_bet)

        else:
            # Pay players who have a better hand;
            # Fine players who have a worse hand

            for player in players:

                player_bet = table.get_bet_amount(player)

                if player.is_bust():
                    player.lose_chips(player_bet)
                    self.win_chips(player_bet)
                    msg += "\nPlayer {} is BUST with hand {} and loses {} chips to the dealer.".\
                        format(player.get_name(), player.get_hand_str(), player_bet)
                elif player.is_21():
                    player.win_chips(player_bet)
                    self.lose_chips(player_bet)
                    msg += "\nPlayer {} has blackjack (21) with hand {} and wins {} chips!\n".\
                        format(player.get_name(), player.get_hand_str(), player_bet)
                elif player.get_hand_value() > self.get_hand_value():
                    player.win_chips(player_bet)
                    self.lose_chips(player_bet)
                    msg += "\nPlayer {} with hand {} wins {} chips!\n".\
                        format(player.get_name(), player.get_hand_str(), player_bet)
                elif self.get_hand_value() > player.get_hand_value():
                    player.lose_chips(player_bet)
                    self.win_chips(player_bet)
                    msg += "\nPlayer {} with hand {} loses {} chips to the dealer.\n".\
                        format(player.get_name(), player.get_hand_str(), player_bet)
                else:
                    msg += "\nGiven the stalemate, player {} with hand {} gets their chips back".\
                        format(player.get_name(), player.get_hand_str())

        SimpleGUI.alert(msg, "Who won?")

        table.clear_for_next_round()

    def is_bust(self):
        is_bust = self.get_hand_value() > 21
        return is_bust

    def is_21(self):
        is_21 = self.get_hand_value() == 21
        return is_21

    def get_hand_value(self):
        return self.__hand.get_value()

    def relinquish_hand(self):
        self.__hand = None

    def shuffle_deck(self):
        self.__deck = []
        self.__shuffle_deck()

    def __get_next_card(self):
        # TODO throw exception if no cards in deck
        print("Line {} of file {}...".format(inspect.currentframe().f_lineno, __file__))
        next_card = self.__deck.pop(0)  # take the first card from the top of the deck
        print("Line {} of file {}...".format(inspect.currentframe().f_lineno, __file__))

        # print("Cards left in deck: %s\n" % (len(self.__deck)))

        return next_card

    def __shuffle_deck(self):
        """
        Create an shuffle a deck of cards
        """
        card_suits = ['spades', 'hearts', 'clubs', 'diamonds']
        card_names = ['ace', 'two', 'three',
                      'four', 'five', 'six',
                      'seven', 'eight', 'nine',
                      'ten', 'jack', 'queen',
                      'king']

        for card_suit in card_suits:
            for card_name in card_names:
                self.__deck.append(Card(name=card_name, suit=card_suit))

        shuffle(self.__deck)
