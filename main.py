import random
import time


def main():
    text = open("The_Arabian_Nights.txt").readlines()
    speed_test_selection = random.choice(text)

    print("You will be tested based upon how fast you can type a randomly selected line from \"The Arabian Nights\"")
    continuation = input("Push ENTER to continue.")
    print("You will have a 15 second delay to read the passage, and to get ready to type.")
    print("Afterwards, a timer will count down from 3 and prompt you to begin.")
    continuation = input("Push ENTER to continue.")
    print("This is going to be your tested passage:")
    print(speed_test_selection)
    time.sleep(15)
    print("15 Seconds have Elapsed.")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    print("Begin!")

    assessment = input()
    if assessment == speed_test_selection:
        print("Congratulations!")
    else:
        print("Learn to type!")


main()


'''
a = "Mary had a little lamb"

def test():
    x = input()
    if x == a:
        print("Correct")
    else:
        print("Incorrect")

test()
'''
