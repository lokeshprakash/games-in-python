'''START
   │
   ▼
Generate random number
   │
   ▼
Display instructions
   │
   ▼
Repeat 7 times
   │
   ▼
Read user's guess
   │
   ├── Guess > Secret Number?
   │        │
   │       Yes
   │        ▼
   │   Print "Lesser"
   │   Show next Hangman
   │
   ├── Guess < Secret Number?
   │        │
   │       Yes
   │        ▼
   │   Print "Higher"
   │   Show next Hangman
   │
   └── Otherwise
            │
            ▼
   Print "Congratulations"
   Saved your man
            │
            ▼
           END'''


import random
n=random.randint(10,100)
print("welcome to hangman\nyou provided with 4 chance to save your man\nguess the number in between 10 to 100\nall the best ")
li = [
'''
 +---+
 |   |
     |
     |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
     |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
''',
'''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
'''
]
m=7
for i in range(0,7):
    num=int(input())
    if num>n:
        print("Lesser:")
        m=m-1
        print((li[m]))
            
    elif num<n:
        print("higher:")
        m=m-1
        print((li[m]))
        
    else:
        print("congrats\nsaved your man")
        print((li[m]))

