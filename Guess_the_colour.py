colours = ["red","orange","pink"]

guess = input("Guess the colour: ").lower()

if guess in colours :
    print("Well done! You guessed correctly.")
else:
    print("That was wrong! Try again.")

