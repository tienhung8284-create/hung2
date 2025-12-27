import random

superhero = 'Spider man', 'Iron man', 'Wonderwoman', 'Batman','Super man'
action1 = 'fight','dance','jump', 'scream'
action2 = 'eating','studying','sleeping','pooping'

choice1 = random.choice(superhero)
choice2 = random.choice(action1)
choice3 = random.choice(action2)

print(f'{choice1} {choice2} while {choice3}')