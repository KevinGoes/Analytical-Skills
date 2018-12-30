import random


def LineairSearch(target, lst):
    if len(lst) == 1 and target != lst[0]:                  # Als de lijst nog 1 item heeft en dit niet de target is
        return False                                        # Geef niet terug
    elif lst[0] == target:                                  # Als de 1ste item van lijst het target is
        return True                                         # Geef wel terug
    else:
        return LineairSearch(target, lst[1:])               # Recursie met lijst zonder eerste item


def random_lst_no_duplicate():
    lst = []
    i = random.randint(20, 40)                              # Random lengte van de lijst (binnen bereik 20 en 40)
    while i != 0:                                           # Zolang de lengte nog niet 0 is
        newInt = random.randint(1, 99)                      # Random getal bepalen
        if newInt not in lst:                               # Als het random getal nog niet in de lijst zit
            lst.append(newInt)                              # Random getal toevoegen
            i -= 1                                          # Lengte verminderen met 1 alleen als item is toegevoegd
    return lst


def test():
    i = 10
    while i != 0:
        lst = random_lst_no_duplicate()                     # Opvragen van random lijst
        target = random.randint(1, 99)                      # Random target
        print('Lijst: {}'.format(lst))                      # Printen van lijst
        print('Target: {}'.format(target))                  # Printen van target
        print(LineairSearch(target, lst) and target in lst, '\n') # Printen van het algoritme in combinatie met check van python
        i -= 1                                              # i verminderen met 1


test()
