class BlackjackTable():
    def __init__(self):
        self.__player_bets = {}
        pass

    def __str__(self):

        result = '<Table num_bets="%d">' % (len(self.__player_bets))
        result += "\n"

        for key, value in self.__player_bets.items():
            result += "    <PlayerBet player_id='%d' player_name='%s' bet_amount='%s' />\n" % (
            key, value["player"].get_name(), value["bet_amount"])

        result += "</Table>\n"

        return result

    def hold_bet(self, player, amount):

        if id(player) not in self.__player_bets:
            self.__player_bets[id(player)] = {
                "player": player,
                "bet_amount": 0
            }

        self.__player_bets[id(player)]["bet_amount"] += amount

    def get_bet_amount(self, player):
        bet_amount = 0

        if id(player) in self.__player_bets:
            bet_amount = self.__player_bets[id(player)]['bet_amount']

        return bet_amount

    def release_bet(self, player, amount=None):

        if id(player) not in self.__player_bets:
            self.__player_bets[id(player)] = {
                "player": player,
                "bet_amount": 0
            }

        if amount is not None:
            self.__player_bets[id(player)]["bet_amount"] -= amount
        else:
            self.__player_bets[id(player)]["bet_amount"] = 0

    def clear_for_next_round(self):
        print("Clearing the table for the next round...")
        self.__player_bets = {}

