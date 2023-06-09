lista = []
print('Ładowanie modułu "{0}"'.format(__name__))


def wypisz():
    result = ""
    for i in range(0, len(lista), 2):
        result += str(lista[i]) + ":" + str(lista[i + 1]) + ", "
    print(result)


def zapisz(values):
    global lista
    for value in values:
        if not Contains(value):
            lista.append(value)
            lista.append(0)
        lista[GetIndex(value) + 1] += 1


def GetIndex(value):
    for i in range(0, len(lista), 2):
        if lista[i] == value:
            return i
    return -1


def Contains(value):
    for i in range(0, len(lista), 2):
        if lista[i] == value:
            return True
    return False


print('Załadowano moduł "{0}"'.format(__name__))
