def main():
    class Card(object):
        def init(self,value,suit):
            self.value = value
            self.suit
       
    
    class StandardDeck(list):
        def init(self):
            super().init()
            suits = list(range(4))
            values = list(range(13))
            [[self.append(Card(i,j))for j in suits]for i in values]
    
    deck = StandardDeck()
    for card in deck:
        print(card.value,card.suit)


if __name__ == "__main__":
    main()



        