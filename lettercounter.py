import os
import matplotlib.pyplot as plt
import numpy as np

english_alphabet = [chr(i) for i in range(97,97+26)]
    #analysis of the letters occurring in the words listed in the main entries of the Concise Oxford Dictionary (11th edition revised, 2004) 
    #http://www.english-for-students.com/Frequency-of-Letters.html

average_english_letters = {'a': 8.4966, 'b': 2.0720, 'c': 4.5388,
                            'd': 3.3844, 'e': 11.1607, 'f': 1.8121,
                            'g': 2.4705, 'h': 3.0034, 'i': 7.5448,
                            'j': 0.1965, 'k': 1.1016, 'l': 5.4893,
                            'm': 3.0129, 'n': 6.6544, 'o': 7.1635,
                            'p': 3.1671, 'q': 0.1962, 'r': 7.5809,
                            's': 5.7351, 't': 6.9509, 'u': 3.6308,
                            'v': 1.0074, 'w': 1.2899, 'x': 0.2902,
                            'y': 1.7779, 'z': 0.2722}

def showPlots(text_directory_pathname, title, legend_label_main,
                alphabet=english_alphabet,
                average_letters=average_english_letters,
                frequency_label="Average frequency",
                legend_label_comparison="in English"):
    
    def count_letters(file_name):
        with open(file_name, "r+", encoding='utf-8-sig') as file:
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


    def accumulate_letter_count(path_name):
        letters_in_stories = {letter:[] for letter in alphabet}
        for filename in os.listdir(path_name):
            story = count_letters(path_name + filename)
            for letter in alphabet:
                (letters_in_stories[letter]).append(story[letter])
        return {letter: np.mean(value) for letter, value in letters_in_stories.items()}

    accumulated_letters = accumulate_letter_count(text_directory_pathname)

    ax1 = plt.subplot2grid((2,2), (0,0), rowspan=1, colspan=2)
    plt.title(title)
    plt.ylabel('{} [%]'.format(frequency_label))
    ax2 = plt.subplot2grid((2,2), (1,0), rowspan=1, colspan=2)

    def plot_letters():
        percent_axis_doyle = [accumulated_letters[letter] for letter in alphabet]
        percent_axis_english = [average_letters[letter] for letter in alphabet]
        ax1.bar(alphabet, percent_axis_doyle, label=legend_label_main, color='b')
        ax1.plot(alphabet, percent_axis_english, label=legend_label_comparison, color='c')  
        ax1.legend()

    def plot_pie_letters(): 
        percent_axis_doyle = [accumulated_letters[letter] for letter in alphabet]
        explode = [0 for i in range(len(alphabet))]
        explode[percent_axis_doyle.index(max(percent_axis_doyle))] = 0.1  
        ax2.pie(percent_axis_doyle, labels=alphabet, startangle=90, explode=explode, counterclock=False)

    plot_letters()
    plot_pie_letters()
    plt.show()