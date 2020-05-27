import random

print("H A N G M A N")
looping = True
while (looping is True):
    game = input("Type play to play the game, exit to quit: ")
    if(game == "play"):
        languages = ['python', 'java', 'kotlin', 'javascript']
        # selecting a random language
        answer = random.choice(languages)
        hint = list("-" * len(answer))
        same_input = []
        # Time to guess
        print("\n")
        i = 0
        while i < 8:
            print("".join(hint))
            current_letter = input("Input a letter: ")
            if(len(current_letter) > 1):
                print("You should input a single letter")
                print("\n")
            elif(not(current_letter.islower())):
                print("It is not an ASCII lowercase letter")
                print("\n")
            else:
                if(current_letter in same_input):
                    print("You already typed this letter")
                elif (current_letter not in answer):
                    print("No such letter in the word")
                    i += 1
                elif current_letter in hint:
                    print("No improvements")
                    #i += 1
                else:
                    for j in range(len(answer)):
                        if (answer[j] == current_letter):
                            hint[j] = current_letter
                same_input.append(current_letter)
                if "".join(hint) == answer:
                    print("You guessed the word!")
                    print("You survived!")
                    break
                else:
                    if i == 8:
                        print("You are hanged!")
            print("\n")

    elif(game == "exit"):
        exit()
