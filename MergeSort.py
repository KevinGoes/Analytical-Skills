import random


def my_sort(lst):
    if len(lst) <= 1:                                   # Er is nu niks meer te sorteren
        return lst

    midden = int(len(lst) / 2)                          # Int omdat je anders een komma getal krijgt
    links = my_sort(lst[:midden])                       # Recurie met linker helft van de lijst
    rechts = my_sort(lst[midden:])                      # Recursie met rechter helft van de lijst

    i = 0                                               # Teller op 0 zetten

    while len(links) != 0 and len(rechts) != 0:         # Zolang er nog items in de links en rechts zitten
        if links[0] < rechts[0]:                        # Eerste item van links is kleiner dan eerste item van rechts
            tmp = links[0]                              # Opslaan van eerste item van links
            links.pop(0)                                # Verwijderen van eerste item van links3
            lst[i] = tmp                                # Bij lijst wordt het opgeslagen item geplaatst

        else:                                           # Eerste item van links is groter dan eerste item van rechts
            tmp = rechts[0]                             # Opslaan van eerste item van rechts
            rechts.pop(0)                               # Verwijderen van eerste item van rechts
            lst[i] = tmp                                # Bij lijst wordt het opgeslagen item geplaatst

        i += 1                                          # Teller wordt met 1 verhoogd

    return lst[:-len(links + rechts)] + links + rechts  # hierbij geeft hij de lijsten terug, links of rechts is leeg


def random_lst():
    lst = []
    i = random.randint(5, 25)                           # Random lengte van de lijst (binnen bereik 5 en 25)
    while i != 0:                                       # Zolang de lengte nog niet 0 is
        lst.append(random.randint(1, 99))               # Random getal toevoegen aan lijst
        i -= 1                                          # Lengte verminderen met 1
    return lst


def random_lst_no_duplicate():
    lst = []
    i = random.randint(5, 25)                           # Random lengte van de lijst (binnen bereik 5 en 25)
    while i != 0:                                       # Zolang de lengte nog niet 0 is
        newInt = random.randint(1, 99)                  # Random getal bepalen
        if newInt not in lst:                           # Als het random getal nog niet in de lijst zit
            lst.append(newInt)                          # Random getal toevoegen
            i -= 1                                      # Lengte verminderen met 1 alleen als item is toegevoegd
    return lst


def check_sort(lst):
    if len(lst) <= 1:                                   # Als de lengte kleiner of gelijk is aan 1
        return True                                     # Er is niks meer te sorteren, geef True terug

    else:
        return lst[0] <= lst[1] and check_sort(lst[1:]) # Geef True terug als index 0 kleiner is dan index 1 en recursie


# Test functie, hierbij kunt u regel 62 aanpassen om een lijst met of zonder duplicates te gebruiken
# Gebruik hiervoor: tmpLst = random_lst() met duplicates. tmpLst = random_lst_no_duplicate() zonder duplicates
def test():
    i = 10                                                  # 10 keer random getal opvragen
    while i != 0:                                           # Zolang het nog niet 10 keer heeft afgespeeld
        tmpLst = random_lst()                               # Random lijst opslaan
        print('{} \nCheck = {}\n'.format(my_sort(tmpLst), check_sort(my_sort(tmpLst))))
        i -= 1                                              # I verminderen met 1
    return 'Finished'


print(test())
