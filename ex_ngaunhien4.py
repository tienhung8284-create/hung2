import random

card_suite = ['Spades', 'Hear', 'Diamonds', 'Clubs']
card_face = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Ace', 'Jack', 'Queen', 'King']

choice1 = random.choice(card_face)
choice2 = random.choice(card_suite)

print(f'Random card is {choice1} of {choice2}')

