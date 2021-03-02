""" https://www.interviewcake.com/question/python/word-cloud """


def simple_build_cloud(sentence):
    word_counter = {}

    for word in sentence.split(" "):
        word = word.lower()
        if not str.isalpha(word[-1]):
            word = word[:-1]

        if word_counter.get(word):
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    print(word_counter)


def build_cloud(sentence):
    word_counter = {}

    starting_position = 0
    for i, char in enumerate(sentence):
        if not str.isalpha(char) and char not in ('-', "'"):
            if i - starting_position > 0:
                word = sentence[starting_position:i]
                if starting_position == 0:
                    word = word.lower()

                if word_counter.get(word):
                    word_counter[word] += 1
                else:
                    word_counter[word] = 1

            starting_position = i + 1
    print(word_counter)


build_cloud('After beating the eggs, Dana read the next step:')
build_cloud('Add milk and eggs, then add flour and sugar.')
build_cloud("The long-term effects of smoking include lung cancer.")
build_cloud("We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake. Then we ate another cake.")
build_cloud('The bill came to five dollars.')
