import tk as tk

baza = {
    "myszka": [{"marcin": 2}, {"tomek": 5}],
    "klawiatura": [{"karol": 1}, {"jakub": 20}, {"mateusz": 200}],
    "rj-45": [{"michal": 10}]
}


def intTryParse(value):
    try:
        return int(value)
    except ValueError:
        raise "Nieprawidłowy Format Danych"


def printOptions():
    print("\nJaką operację chcesz wykonać")
    print("1 - sprzedaż")
    print("2 - zwrot")


def GetSelectedDevice():
    print("\nJaki Produkt Sprzedajesz: ")
    for device, people in baza.items():
        print("\t" + device)
    return input("Wybierz Produkt")


def TryAddClient(device, client, addedAmount):
    global baza
    for i in range(len(baza[device])):
        for person, amount in baza[device][i].items():
            if person == client:
                baza[device][i][person] += addedAmount
                return True
    return False


def getOptionFromInput():
    printOptions()
    option = intTryParse(input("wybierasz: "))
    while option != 1 and option != 2:
        printOptions()
        option = intTryParse(input("wybierasz: "))
    return option


def TrySell(device, seller, soldAmount):
    global baza
    for i in range(len(baza[device])):
        for person, amount in baza[device][i].items():
            if person == seller:
                if baza[device][i][person] < soldAmount:
                    raise "Nie mamy tyle sprzetu na magazynie"
                baza[device][i][person] = (baza[device][i][person] - soldAmount)
                return True
    return False


def sprzedaz():
    global baza
    device = GetSelectedDevice()
    while not baza.keys().__contains__(device):
        device = GetSelectedDevice()
    seller = input("Komu go sprzedajesz: ")
    amount = intTryParse(input("Jaka ilosc: "))
    if not TrySell(device, seller, amount):
        raise "Nie można sprzedać komus lub czegoś co nie istnieje w bazie"


def zwrot():
    global baza
    device = input("\nJakie urządzenie chcesz zwrócić: ")
    client = input("Komu chcesz je zwrócić: ")
    amount = intTryParse(input("Jaka ilosc: "))
    if not TryAddClient(device, client, amount):
        baza[device].add({client: amount})


if __name__ == '__main__':
    print("Witam w internetowej bazie x-kom:")
    chosenOption = getOptionFromInput()
    while chosenOption != 0:
        print(baza)
        if chosenOption == 1:
            sprzedaz()
        if chosenOption == 2:
            zwrot()
        chosenOption = getOptionFromInput()

