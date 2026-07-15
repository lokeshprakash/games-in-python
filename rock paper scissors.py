#rock paper scissors
import random
li=["rock","paper","scissors"]
m=0
q=0
n=int(input("total no of times to play"))
for i in range(0,n):
    word = random.choice(li)
    print(f"computer point {m} syour points {q}")
    n2=input("Rock or paper or scissors")
    n1=n2.lower()
    if n1==word:
        print("draw")
    elif n1=="scissors" and word=="paper":
        print("you won")
        q=q+1
    elif n1=="rock" and word=="scissors":
        print("you won")
        q=q+1
    elif n1=="paper" and word=="rock":
        print("you won")
        q=q+1
    else:
        print("computer won")
        m=m+1
print("thank you")
'''                
                 ┌─────────────┐
                 │    START    │
                 └──────┬──────┘
                        │
                        ▼
           ┌────────────────────────┐
           │ Import random module   │
           └──────────┬─────────────┘
                      │
                      ▼
        ┌─────────────────────────────┐
        │ Create list                 │
        │ ["rock","paper","scissors"] │
        └──────────┬──────────────────┘
                   │
                   ▼
      ┌─────────────────────────────┐
      │ Initialize scores           │
      │ m = 0, q = 0                │
      └──────────┬──────────────────┘
                 │
                 ▼
      ┌─────────────────────────────┐
      │ Read number of rounds (n)   │
      └──────────┬──────────────────┘
                 │
                 ▼
          ┌──────────────────────┐
          │ Repeat n times       │
          └──────────┬───────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Computer selects random │
        │ rock/paper/scissors     │
        └──────────┬──────────────┘
                   │
                   ▼
        ┌─────────────────────────┐
        │ Display current scores  │
        └──────────┬──────────────┘
                   │
                   ▼
        ┌─────────────────────────┐
        │ Read player's choice    │
        │ Convert to lowercase    │
        └──────────┬──────────────┘
                   │
                   ▼
            ┌────────────────┐
            │ Player == CPU? │
            └──────┬─────────┘
              Yes  │   No
                   ▼
              Print "Draw"
                   │
                   ▼
                Next Round
                   ▲
                   │
              No   │
                   ▼
      ┌───────────────────────────────┐
      │ Does player beat computer?    │
      └──────┬────────────────────────┘
        Yes  │   No
             ▼
      Print "You Won"
      Player Score++
             │
             ▼
         Next Round
             ▲
             │
        No   │
             ▼
     Print "Computer Won"
     Computer Score++
             │
             ▼
         Next Round
             │
             ▼
       Loop Finished?
             │
             ▼
     Print "Thank You"
             │
             ▼
            END'''
