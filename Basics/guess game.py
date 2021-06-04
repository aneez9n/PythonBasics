# NumberGuessingGame



i=1
while i <= 3:
    correct_number = 7
    guess_number = int(input("guess the number !  "))
    if guess_number == correct_number:
        print("you guess the wright number !  ")
        break
    i=i+1

else:
    print("sorry you lost")
