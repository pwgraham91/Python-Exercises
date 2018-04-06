__author__ = 'GoldenGate'
import random
clean_shirts = ["Chuck", "Isabelle", "Robert", "Garrett", "Peter", "Molly", "Julian", "Adam", "Mani", "Josh", "Zach", "Miguel", "Brittney", "Bryan", "Niki", "Jon", "Michael", "Pat", "Johanna", "Jeff"]
dirty_shirts =[]
day = 1
def choosing():
    global clean_shirts, dirty_shirts, day
    available_shirts = len(clean_shirts)
    choose_shirt = random.randint(0, (available_shirts-1))
    chosen_shirt = clean_shirts[choose_shirt]
    dirty_shirts.append(chosen_shirt)
    clean_shirts.remove(chosen_shirt)
    day += 1
    print "dirty", dirty_shirts
    print "clean", clean_shirts
while len(clean_shirts) > 0:
    choosing()