import random


name=input("what is your name? ")

print("All the Best",name)

colour = ["red","orange","blue","green","yellow","white","black","violet","silver","golden","brown","pink","purple","grey"]

word=random.choice(colour);
print("Guess the characters in colour:")
guesses=''

turn=6
while turn>0:
    count=0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print("---")
            count +=1

    if count == 0:
        print("congratulations............you are winner",name)
        print("the colour is",word)
        break

    guess=input("guess a character in country:")
    guesses += guess

    if guess not in word:
        turn -= 1
        print("sorry!.....you are worng guess")
        print("you have",+ turn,'more guesses:')
        if turn == 0:
            print("you loose......Sorry")


