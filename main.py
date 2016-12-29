import random
import time


def main():
    text = open("The_Arabian_Nights.txt").readlines()
    speed_test_selection = random.choice(text).strip()
    word_count = len(speed_test_selection.split())

    print("You will be tested based upon how fast you can type a randomly selected line from \"The Arabian Nights\"")
    continuation = input("Push ENTER to continue.")
    print("You will have a 15 second delay to read the passage, and to get ready to type.")
    print("Afterwards, a timer will count down from 3 and prompt you to begin.")
    print("Your passage will be nestled between two sets of parentheses. Punctuation counts, but don't type those out!")
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
    elapsed = end-begin
    if assessment == speed_test_selection:
        print("Congratulations!")
    else:
        print("Incorrect!")
        print("Learn to type!")
    print("Here are your performance stats:")
    print(elapsed, " seconds have elapsed. You are so slow!")
    print("You type at a speed of ", 60 * word_count / elapsed, " words per minute.")

main()

#setting up accuracy test
'''
    for char in assessment:
        if assessment[1] != speed_test_selection[1]:
            mistake += 1
            return

    print(str(mistake))
'''
