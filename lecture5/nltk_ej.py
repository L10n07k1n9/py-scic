import nltk.book as books
# from nltk.corpus import gutenberg

text1 = books.text1
text2 = books.text2
text3 = books.text3
text4 = books.text4

# concordance of a word  in a context
text1.concordance("damn")

text2.common_contexts(["monstrous", "very"])

# plot word's dispersion among the text
text4.dispersion_plot(
    ["citizens", "democracy", "freedom", "duties", "America"])
'''
A token is the
technical name for a sequence of characters—such as hairy, his, or :)—that we want
to treat as a group. When we count the number of tokens in a text, say, the phrase to
be or not to be, we are counting occurrences of these sequences. Thus, in our example
phrase there are two occurrences of to, two of be, and one each of or and not. But there
are only four distinct vocabulary items in this phrase. 
'''
primary_words = sorted(set(text3))

m = len(primary_words)

# Frecuency of a word
from nltk import FreqDist
w0, w1 = "monstrous", "the"
freq = FreqDist(text1)
print("Frec of word <{}>: {}".format(w0, freq[w0]))
print("Frec of word <{}>: {}".format(w1, freq[w1]))
# Cumulative frequency plot for the 50 most frequently used words in Moby Dick, which account for nearly half of the tokens
freq.plot(50, cumulative=True)

# search for words of length with freq  greater than 20
words = set([word for word in text1 if len(word) == 5 and freq[word] > 600])
