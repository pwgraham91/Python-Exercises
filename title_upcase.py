def turn_upper(title):
    title2 = []
    title4 = []
    title = title.split()
    for letter in title:
        letter1 = letter[0].upper() + letter[1:]
        title2.append(letter1)
    pset = (['And', "Of", "In", "A", "An", "To", "By", "But", "Yet", "So", "With", "For", "The"])
    for letter in title2:
        if letter in pset:
            letter2 = letter[0].lower() + letter[1:]
            title4.append(letter2)
        else:
            title4.append(letter)
    title4 = " ".join(title4)
    print title4

turn_upper('my title')

