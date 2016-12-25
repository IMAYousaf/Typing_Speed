import random
import time


def main():
    text = open("The_Arabian_Nights.txt").readlines()
    speed_test_selection = random.choice(text).strip()

    print("You will be tested based upon how fast you can type a randomly selected line from \"The Arabian Nights\"")
    continuation = input("Push ENTER to continue.")
    print("You will have a 15 second delay to read the passage, and to get ready to type.")
    print("Afterwards, a timer will count down from 3 and prompt you to begin.")
    continuation = input("Push ENTER to continue.")
    print("This is going to be your tested passage:")
    print("\"" + speed_test_selection + "\"")
    time.sleep(15)
    print("15 Seconds have Elapsed.")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    print("Begin!")
    begin = time.time()

    assessment = input()

    end = time.time()

    if assessment == speed_test_selection:
        print("Congratulations!")
    else:
        print("Incorrect! Learn to type!")


    print(str(end-begin) + "seconds have elapsed. You are so slow!")
    #print("You type as a speed of " + str((WORDS/((end-begin)/60))) + " words per minute."

'''
    for char in assessment:
        if assessment[1] != speed_test_selection[1]:
            mistake += 1
            return

    print(str(mistake))
'''

main()


'''
import random

text = open("file.txt").readlines()
selection = random.choice(text).strip

def main():
    assessment = input()
    if assessment == selection:
        print("Correct")
    else:
        print("Incorrect")
    for char in assessment:
        if assessment[i] != selection[i]:
            error += 1
    print(error)

main()
'''
