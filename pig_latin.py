import string


def to_pig_latin(text):
    words = text.split(' ')
    altered_words = []
    for word in words:
        punctuation = None
        if word[-1] in string.punctuation:
            punctuation = word[-1]
            word = word[:-1]
        if len(word) >= 2 and word[-2:] == 'ay':
            word = word[:-2]
        if len(word) >= 1:
            altered_word = '{}{}ay'.format(word[1:], word[0])
        else:
            if len(word) > 0:
                altered_word = word[0]
            else:
                altered_word = ''
        if punctuation:
            altered_word = '{}{}'.format(altered_word, punctuation)
        altered_words.append(altered_word)
    latin = ' '.join(altered_words)
    return latin


assert to_pig_latin('Pig latin is cool') == 'igPay atinlay siay oolcay'
assert to_pig_latin('This is my string') == 'hisTay siay ymay tringsay'
