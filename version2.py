import random
import time

def main():
    choice = input("Type in \"EASY\" or \"HARD\" based upon your desired difficulty level:")
    if choice in {"EASY", "easy"}:
        easy()
    elif choice in {"HARD", "hard"}:
        hard()

def easy():
    text = open("The_Arabian_Nights.txt").readlines()
    selection = random.choice(text).strip()
    word_count = len(selection.split())
    print(selection)
    begin = time.time()
    assessment = input()
    end = time.time()
    if assessment == selection:
        print("Correct")
    else:
        print("Incorrect")
    elapsed = end - begin
    print(elapsed, "seconds have elapsed.")
    print ("You type at a speed of", 60 * word_count / elapsed, "words per minute.")
    file = open("test.txt", "w")
    file.write(selection)
    file.write("\n\n")
    file.write(assessment)

def hard():
    with open("The_Arabian_Nights.txt") as paragraphs:
        text = paragraphs.read()
    paragraph = text.split('\n\n')
    paragraph = random.choice(paragraph)
    word_count = len(paragraph.split())
    print(paragraph)
    begin = time.time()
    assessment = input()
    end = time.time()
    if assessment == paragraph:
        print("Correct")
    else:
        print("Incorrect")
    elapsed = end - begin
    print(elapsed, "seconds have elapsed.")
    print ("You type at a speed of", 60 * word_count / elapsed, "words per minute.")
    file = open("test.txt", "w")
    file.write(paragraph)
    file.write("\n\n")
    file.write(assessment)

main()

'''
file = open("test.txt", "w")
file.write(paragraph)
file.write("\n")
file.write(assessment)
'''
