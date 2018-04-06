__author__ = 'petergraham'
import re


def striped_words(text):
    words = re.findall(r"[\w']+", text)
    vowels = ["a", "e", "i", "o", "u", "y"]
    good_words = []
    for word in words:
        word = word.lower()
        vowel = False
        consonant = False
        striped = True
        if word.isalpha():
            for letter in word:
                if letter in vowels:
                    if vowel:
                        striped = False
                    else:
                        vowel = True
                        consonant = False
                else:
                    if consonant:
                        striped = False
                    else:
                        vowel = False
                        consonant = True
            if striped:
                good_words.append(word)
    for word in good_words:
        if len(word) == 1:
            good_words.remove(word)
    return len(good_words)

print striped_words("A quantity of striped words")
print striped_words('Are there any striped words in this sentence?')
print striped_words('Are any in')
