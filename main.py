import random
import time

def main():
    text = open("The_Arabian_Nights.txt").readlines()
    speed_test_selection = random.choice(text)

    print("You will be tested based upon how fast you can type a randomly selected line from \"The Arabian Nights\"")
    continuation = input("Push ENTER to continue.")
    if selection in {ENTER}:
        print("This is going to be your tested passage.")
        print("You will have a 15 second delay to read the passage, and to get ready to type.")
        time.sleep(15)

    print("\"" + speed_test_selection + "\"")

main()
