# Välja ett tal

correctNumber= 6
numOFGusses= 3

# Be om en siffra

while (numOFGusses > 0):
    print("guess a number")
    guess = int(input)()
    print("you guessed")
    print(guess)

    numOFGusses -= 1
    # kolla om siffran är större eller mindre eller lika

    if (guess > correctNumber):
        print ("you guessed to high, try again.")
    elif (guess < correctNumber):
        print("You guessed to low, try again")
    else:
        print("You guessed right! Good job")
        numOFGusses = 0


    # göra tre gånger