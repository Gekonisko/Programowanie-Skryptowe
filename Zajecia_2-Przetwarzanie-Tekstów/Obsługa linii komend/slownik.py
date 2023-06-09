slownik = {}

print('Ładowanie modułu "{0}"'.format(__name__))


def wypisz():
    result = ""
    for key, value in slownik.items():
        result += str(key) + ":" + str(value) + ", "
    print(result)


def zapisz(values):
    global slownik
    for value in values:
        if not slownik.keys().__contains__(value):
            slownik[value] = 0
        slownik[value] += 1


print('Załadowano moduł "{0}"'.format(__name__))
