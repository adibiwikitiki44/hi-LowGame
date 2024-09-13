low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1

while True:
    print("\tGuessing in the range of {} to {}".format(low, high))

    guess = low + (high - low) // 2  # Using binary search to find the guessed value

    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h (Higher) or l (Lower) or c (Correct): "
                     .format(guess)).casefold()

    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes one less than the guess.
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")

    guesses = guesses + 1