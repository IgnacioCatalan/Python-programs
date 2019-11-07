import random
while True:
    deck=['As♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠',
          'As♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥',
          'As♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣',
          'As♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦']
    random.shuffle(deck)
    print('The deck has been shuffled')
    print()
    cont=input('Press enter to deal hands...')
    print()
    cont=0
    hand=[]
    op_hand=[]
    while cont<2:
        hand.append(deck[0])
        deck.remove(deck[0])
        op_hand.append(deck[0])
        deck.remove(deck[0])
        cont=cont+1
    print('Your hand:',hand)
    print('Opponent\'s hand is secret')
    print('Cards in deck:',len(deck))
    print()
    cont=input('Press enter to deal the Flop...')
    print()
    flop=[]
    table=[]
    cont=0
    burned=[]
    burned.append(deck[0])
    deck.remove(deck[0])
    while cont<3:
        flop.append(deck[0])
        deck.remove(deck[0])
        cont=cont+1
    table=flop
    print('Cards on the table:',table)
    print('Your hand:',hand)
    print('Cards in deck:',len(deck))
    print()
    cont=input('Press enter to deal the Turn...')
    print()
    burned.append(deck[0])
    deck.remove(deck[0])
    turn=(deck[0])
    deck.remove(deck[0])
    table.append(turn)
    print('Cards on the table:',table)
    print('Your hand:',hand)
    print('Cards in deck:',len(deck))
    print()
    cont=input('Press enter to deal the River...')
    print()
    burned.append(deck[0])
    deck.remove(deck[0])
    river=(deck[0])
    deck.remove(deck[0])
    table.append(river)
    print('Cards on the table:',table)
    print('Your hand:',hand)
    print('Opponent\' hand:',op_hand)
    print('Cards in deck:',len(deck))
    print()
    print('Burned cards:',burned)
    print()
    restart=input('Press enter to start another game...')
    print()
                
