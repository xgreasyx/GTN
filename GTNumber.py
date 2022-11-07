def game():
    # import the random int module
    import random

    # input name. using .title capitalizes all names they use.
    nm = input("whats your name? ")
    print("G'day", nm.title(), "Let's play a game: ")
    # welcome note

    # here we made variable for number AI to choose a number between 1 and 99
    rn = random.randint(1, 99)
    # here we are creating a variable for the random number & asking the User to guess a number
    gs = int(input("Choose a Number between 1 & 99? "))

    while True:
        while gs not in range(1, 100):  # while gs not in range means to only choose numbers in the range.
            gs = int(input("Between 1 & 99: "))
        print()
        if gs > rn:
            print("Too High! ")
            if (gs - rn) <= 10:
                print("warm")
                gs = int(input("try again: "))
            else:
                gs = int(input("Cold: "))
        elif gs < rn:
            print("Too Low! ")
            if (rn - gs) <= 10:
                print("warm")
                gs = int(input("try again: "))
            else:
                gs = int(input("Cold: "))
        elif gs == rn:
            print("You Did It", nm.title())
            restart = input("Want to Play Again y/n? ")
            if restart == "y":
                game()
            elif restart == "n":
                print()
                print("See You Next Time", nm.title())
                break
            else:
                print()
                print("*** Please Use Only 'y' or 'n' *** ")
        else:
            pass


game()
