import random
stages =['''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |      
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |

=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |

=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |

=========''', '''
 +---+
  |   |
  O   |
  |   |
      |
      |

=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |

=========''', '''
  +---+
  |   |
      |
      |
      |
      |

=========''']
print('''                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/             ''')

mylist = ["earoplane", "apple", "cake", "potatos", "maiil"]
print(mylist)
choosen = random.choice(mylist)
word_length = len(choosen)
lives = 6
display = []
for letter in range(word_length):
    display += "_"
print(display)
end_of_game = False
while not end_of_game:
    guess = input("guess the letter ").lower()
    for position in range(word_length):
        letter = choosen[position]
        if letter == guess:
            display[position] = letter
    if guess not in choosen:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("u lose")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("u win")
    print(stages[lives])




