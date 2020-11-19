import random
import string

print("""H A N G M A N""")

words = ['python', 'java', 'kotlin', 'javascript']
search_word = random.choice(words)
hint = list("-" * (len(search_word)))
shot = 0
guessed_letters = set()

while shot < 8:
    print()
    print("".join(hint))
    if ("".join(hint)) == search_word:
        print("You guessed the word!\nYou survived!")
        break
    x = input("Input a letter:")
    if x in search_word:
        if x in guessed_letters:
            print("You've already guessed this letter")
        else:
            for i in range(len(search_word)):
                if search_word[i] == x:
                    hint[i] = x
            guessed_letters.add(x)
    elif len(x) != 1:
        print("You should input a single letter")
    elif x not in string.ascii_lowercase:
        print("Please enter a lowercase English letter")
    else:
        if x in guessed_letters:
            print("You've already guessed this letter")
        else:
            shot += 1
            guessed_letters.add(x)
            print("That letter doesn't appear in the word")
else:
    print("You lost!")