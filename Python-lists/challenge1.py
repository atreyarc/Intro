import random

card_colors = ['spades', 'clubs', 'hearts', 'diamonds']
card_numbers =[2,3,4,5,6,7,8,9,10,'A','J','Q','K']
deck=[]
deal_hand1 = []
for colors in card_colors:
    for number in card_numbers:
        deck.append(str(number)+' of ' + colors)
print('There are ' + str(len(deck)) + ' cards in the deck.')
print('Dealing..')
deal_hand1_choice = ''
card_count = 1

while(card_count<=5):
    deal_hand1_choice = random.choices(deck)
    deck.pop(int(deck.index(deal_hand1_choice[0])))
    deal_hand1.append(deal_hand1_choice)
    card_count+=1

print('There are ' + str(len(deck)) + ' cards in the deck.')
print('Player has the following cards in their hand:')
print(deal_hand1)

#this is sub-optimal