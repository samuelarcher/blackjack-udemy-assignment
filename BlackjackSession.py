import inspect


class BlackjackSession():
    def __init__(self, table, dealer, players):
        self.__table = table
        self.__dealer = dealer
        self.__players = players

    def play(self):

        table = self.__table
        dealer = self.__dealer
        players = self.__players
        player_bets = []  # should become an an equal number to 'players' list above

        # Give players a chance to buy more chips
        print("\n*** Players are buying chips...", flush=True)
        for player in players:
            player.buy_chips()

        # Place initial bets on table
        print("\n*** Players are placing bets...", flush=True)
        for player in players:
            player.place_initial_bet(table)

        # Deal initial hand to players
        print("\n*** Dealing initial hand to players...", flush=True)
        for player in players:
            for i in [1, 2]:
                dealer.deal_card_to_player(player)

        # Deal initial hand to dealer
        print("\n*** Dealer is dealing a hand to self...", flush=True)
        for i in [1, 2]:
            dealer.deal_card_to_self()

        # Dealer interacts with each player to hit/stand/etc
        print("\n*** Getting player moves...", flush=True)
        for player in players:
            if not player.get_hand_value() == 21:
                dealer.get_player_moves(player)

        print("\n*** Determining the winner...", flush=True)

        # Figure out if all players got 21 or all players busted
        busted_player_count = 0
        blackjack_player_count = 0
        player_count = len(players)

        print("\n*** Counting busts & blackjacks...", flush=True)
        for player in players:
            if player.is_bust():
                busted_player_count += 1
            elif player.is_21():
                blackjack_player_count += 1

        all_players_are_bust = player_count == busted_player_count
        all_players_are_blackjack = player_count == blackjack_player_count

        print("\n*** Doing dealer stand or hit...", flush=True)
        # The dealer is done dealing to players and should deal to self unless
        # all players busted or all players got blackjack
        if not (all_players_are_blackjack or all_players_are_bust):
            # Dealer hits/stands as house calls for...
            dealer.stand_or_hit_according_to_house_rules()

        # Settle up
        print("\n*** Settling up...", flush=True)
        dealer.settle_round(table, players)

        print("\n*** Relinquishing hands...", flush=True)
        # Give all the cards back to the deck
        dealer.relinquish_hand()
        for player in players:
            player.relinquish_hand()

        dealer.shuffle_deck()
