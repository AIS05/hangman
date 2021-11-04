__author__ = "Aaron Stacey"
__version__ = "1.0"


from requests import get

# GET Request
# number = N/O words returned
r= get(url = 'https://random-word-api.herokuapp.com/word', params = {'number':1})
# Word = output of GET request without special characters
word = ''.join(e for e in r.text if e.isalnum())

ltrs = []
gLtrs = []
prvGuess = []
cls = "\n" * 100

for i in word:
    ltrs.append(i.upper())
    gLtrs.append('_')

lives = 11
Win = False

def drawBoard():
    global prvGuess

    print(" ", end="")
    for i in gLtrs:
        print(str(i + " "), end ="")
    print(f" | Guesses Left: {lives}")
    print("")
    print("Previously Guessed Letters & Words: "+ ', '.join(prvGuess))
    userInput()

def userInput():
    global gLtrs
    global Win
    global lives
    global prvGuess

    while True:
        usrIn = str(input("Input a letter or a word -> ")).upper()
        if usrIn == "___":
            print(f"Word -> {word}")

        elif usrIn.isalpha() is True:
            if usrIn not in prvGuess:
                t = 0
                if len(usrIn) == 1:
                    for idx, val in enumerate(ltrs):
                        if usrIn == val:
                            gLtrs[idx] = val
                            t += 1
                else:
                    if usrIn == ''.join(ltrs):
                        gLtrs = ltrs
                        t=999
                        Win = True

                if t == 0:
                    lives -= 1

                prvGuess.append(usrIn)
                break
            else:
                print(f"You already guessed '{usrIn}'")
        else:
            print("Please Input A Letter or a Word")

print("Welcome to Hangman!")
print("You can try to guess the word by either letter by letter or whole word.")
print("If you guess incorrectly you lose a life!")
print("You start with 11 lives, if you lose them all you will lose!")
print("If you guess the word before you lose all your lives you will win!")
print("")
input("Press ENTER to start ")
print(cls)

while lives != 0:
    print(cls)
    drawBoard()


    if ''.join(gLtrs) == ''.join(ltrs):
        Win = True

    if Win is True:
        print(cls)
        print("You Won!")
        print("Word : " + ''.join(ltrs))
        print("")
        print(f"Lives Left : {lives} / 11")
        print("")
        break

if lives == 0:
    print("You Lost")
    print("Word : " + ''.join(ltrs))
    print("")

input("Press ENTER to exit ")