class Card(object):
    def __init__(self, name, suit, face_up=False):
        self.__name = name
        self.__suit = suit
        self.__face_up = face_up

    def __str__(self):
        return '<Card name="%s" suit="%s" />' % (self.__name, self.__suit)

    def get_suit(self):
        return self.__suit

    def get_name(self):
        return self.__name

    def turn_face_up(self):
        self.__face_up = True

    def is_face_up(self):
        return self.__face_up
