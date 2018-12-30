import random


def BinairSearch(target, lst):
    if len(lst) == 0:                                       # Als er geen items meer in de lijst zitten
        return False                                        # Geef niet terug
    else:
        midden = int(len(lst) / 2)                          # Midden bepalen
        if target == lst[midden]:                           # Als de target het midden is, zit het in de lijst
            return True                                     # Geef wel terug
        elif target > lst[midden]:                          # Als het nummer van de target groter is dan het midden
            return BinairSearch(target, lst[midden+1:])     # Recursie met lijst groter dan midden
        else:                                               # Als het nummer van de target kleiner is dan het midden
            return BinairSearch(target, lst[:midden])       # Recursie met lijst kleinder dan midden


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
        lst.sort()                                          # De lijst MOET gesorteerd zijn om Binair te kunnen zoeken
        target = random.randint(1, 99)                      # Random target
        print('Lijst: {}'.format(lst))                      # Printen van lijst
        print('Target: {}'.format(target))                  # Printen van target
        print(BinairSearch(target, lst) and target in lst, '\n') # Printen van het algoritme in combinatie met check van python
        i -= 1                                              # i verminderen met 1


test()
