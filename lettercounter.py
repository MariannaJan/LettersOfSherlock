import os
import matplotlib.pyplot as plt
import numpy as np

alphabet = [chr(i) for i in range(97,97+26)]

def count_letters(fn):
    with open(fn, "r+", encoding='utf-8-sig') as file:
        content = file.read().lower()
        letters = {}
        letter_count = 0
        for letter in content:
            if letter.isalpha():
                letter_count += 1
                if letter not in letters:
                    letters[letter] = 1
                else:
                    letters[letter] += 1
        return {letter: round(value/letter_count, 4)*100 for letter, value in letters.items()}


def accumulate_letter_count():
    letters_in_stories = {letter:[] for letter in alphabet}
    for filename in os.listdir("./Books/"):
        story = count_letters("./Books/{}".format(filename))
        for letter in alphabet:
            (letters_in_stories[letter]).append(story[letter])
    return {letter: np.mean(value) for letter, value in letters_in_stories.items()}


def plot_letters():
    accumulated_letters = accumulate_letter_count()
    percent_axis = [accumulated_letters[letter] for letter in alphabet]
    plt.plot(alphabet, percent_axis)
    plt.show()

plot_letters()




