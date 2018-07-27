# LettersOfSherlock
Demo of using Python 3 with NumPy and Matplotlib


A small program creating two charts from the given set of documents in txt files:

1. A bar chart with average of percenttage frequencies of occurance of each letter of alphabet in the given set of texts with comparison to average values.

2. A pie chart with average of percenttage frequencies of occurance of each letter of alphabet in the given set of texts

Options for customisation / default values:

1. Alphabet used for the charts - if not spcified, standard 26 small letters (a-z) of English alpabet are used
2. Average frequencies of letter occurance used for comparison - if not specified the default is for English letters
  source: analysis of the letters occurring in the words listed in the main entries of the Concise Oxford Dictionary (11th edition revised, 2004) 
          http://www.english-for-students.com/Frequency-of-Letters.html
3. Frequency label - label for the Y axis of the bar chart (always with [%] sign). If not specified the default is "Average frequency"
4. Label for the comparison data in the legend of in the bar chart - if not specified the default is "in English"

In this demo I used Sir Arthur Conan Doyle's books taken from the Gutenberg Project. https://www.gutenberg.org/ebooks/author/69
A full license text from Gutenberg Project is a part of this repository.
