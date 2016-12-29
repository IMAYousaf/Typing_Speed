import random
import time
import difflib

def main():
    choice = input("Type in \"EASY\" or \"HARD\" based upon your desired difficulty level:")
    if choice in {"EASY", "easy"}:
        text = open("The_Arabian_Nights.txt").readlines()
        selection = random.choice(text).strip()
        word_count = len(selection.split())
    elif choice in {"HARD", "hard"}:
        with open("The_Arabian_Nights.txt") as paragraphs:
            text = paragraphs.read()
            selection = text.split('\n\n')
            selection = random.choice(selection)
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
    d = difflib.Differ()
    difference = d.compare(selection.split(), assessment.split())
    file.write("\n")
    file.write(str(''.join(difference)))
    s = difflib.SequenceMatcher(None, selection, assessment)
    print("You were", s.ratio() * 100, "% correct")

main()
