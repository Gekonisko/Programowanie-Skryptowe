from enum import Enum
from sqlite3 import Date
from datetime import datetime


class LibraryData:
    def __init__(self, BookData, Amount, Person):
        self.Book = BookData
        self.Amount = Amount
        self.Person = Person


class Book:
    def __init__(self, idKsiazki: int, peselCzytelnika: str, autor: str, tytul: str, dataWyporzyczenia: Date,
                 dataZwrotu: Date):
        self.idKsiazki = idKsiazki
        self.peselCzytelnika = peselCzytelnika
        self.autor = autor
        self.tytul = tytul
        self.dataWyporzyczenia = dataWyporzyczenia
        self.dataZwrotu = dataZwrotu

    @classmethod
    def BaseData(cls, autor: str, tytul: str):
        return cls(hash(autor + tytul), None, autor, tytul, None, None)

    def __str__(self):
        return f'{self.idKsiazki}, {self.autor}, {self.tytul}'

    def __hash__(self):
        return hash(self.autor + self.tytul)


class Reader:
    def __init__(self, imię: str, nazwisko: str, pesel: str):
        self.imie = imię
        self.nazwisko = nazwisko
        self.pesel = pesel

    def __add__(self, book: Book):
        if Library.Books.keys().__contains__(book.idKsiazki):
            raise Exception(f"Książka {book.tytul} została już wypożyczona")
        if not Library.Readers.keys().__contains__(self.pesel):
            Library.Readers[self.pesel] = self
        Library.Books[book.idKsiazki] = Book(book.idKsiazki, self.pesel, book.autor, book.tytul, datetime.now(), None)

    def __sub__(self, book: Book):
        if not Library.Readers.keys().__contains__(self.pesel):
            raise Exception(f"{str(self)} nie wyporzyczyła nic w naszej bibliotece")
        if not Library.Books.keys().__contains__(book.idKsiazki):
            raise Exception(f"Nie posiadamy Książki {book.tytul}")
        wyporzyczoneKsiazki = 0
        czyZwrot = False
        for key, value in Library.Books.items():
            if value.peselCzytelnika == self.pesel:
                wyporzyczoneKsiazki += 1
                if value.__hash__() == book.__hash__():
                    czyZwrot = True
        if czyZwrot:
            Library.Books.pop(book.idKsiazki)
        if Library.Books.keys().__contains__(book.idKsiazki):
            raise Exception(f"{str(self)} Nie posiada Książki {book.tytul}")
        if wyporzyczoneKsiazki == 1:
            Library.Readers.pop(self.pesel)

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'


class Library:
    Books = {}
    Readers = {}

    def __init__(self, ksiegozbior):
        pass
        # self.Books = {}
        # self.Clients = {}
        #self.__ReadBooks(ksiegozbior)

    def print(self, books: {int: Book}):
        for book in books.values():
            print(book)

    def print(self, readers: {int: Reader}):
        for reader in readers.values():
            print(reader)

    def print(self, book: Book):
        print(book)

    def print(self, reader: Reader):
        print(reader)

    def __ReadBooks(self, ksiegozbior):
        with open(ksiegozbior) as f:
            line = f.readline()
            while line != "":
                self.parseFileLine(line)
                line = f.readline()

    def parseFileLine(self, line):
        data = line.split("-")
        self.Books[data[0].strip()] = int(data[1])

    def BorrowBook(self, data):
        if not self.Books.keys().__contains__(data.Book):
            print("Nie posiadamy ksiazki: ", data.Book)
            return
        if self.Books[data.Book] >= data.Amount:
            self.Books[data.Book] -= data.Amount
            if not self.Clients.keys().__contains__(data.Person):
                self.Clients[data.Person] = {data.Book: data.Amount}
                return
            if not self.Clients[data.Person].keys().__contains__(data.Book):
                self.Clients[data.Person][data.Book] = data.Amount
                return
            self.Clients[data.Person][data.Book] += data.Amount
        else:
            print("Nie mamy tyle ksiazek '", data.Book, "' na magazynie")

    def ReturnBook(self, data):
        if not self.Clients.keys().__contains__(data.Person):
            print("Osoba o imieniu '", data.Person, "' nic u nas nie wyporzyczala")
            return
        if self.Clients[data.Person].keys().__contains__(data.Book):
            if self.Clients[data.Person][data.Book] >= data.Amount:
                self.Clients[data.Person][data.Book] -= data.Amount
                self.Books[data.Book] += data.Amount
            else:
                print("Nie wypozyczyles tylu ksiazek :", data.Book)
        else:
            print("Nie wypozyczyles ksiazki: ", data.Book)


def borrowInput():
    print()
    ksiazka = input("Jaką książkę wyporzyczasz: ")
    ile = int(input("Ile książek wyporzyczasz: "))
    nazwa = input("Na kogo wypozyczasz książkę: ")
    print()
    return LibraryData(Book=ksiazka, Amount=ile, Person=nazwa)


def returnInput():
    print()
    ksiazka = input("Jaką książkę zwracasz: ")
    ile = int(input("Ile książek zwracasz: "))
    nazwa = input("Na kogo zwracasz książkę: ")
    print()
    return LibraryData(Book=ksiazka, Amount=ile, Person=nazwa)


if __name__ == '__main__':
    library = Library("ksiazki.txt")

    book1 = Book.BaseData("Max Kolanko", "Kroniki Prezydentury")
    book2 = Book.BaseData("MEDUSA", "23 kilometry do")
    reader1 = Reader("Nalaia", "Majka", "08223547851")
    reader2 = Reader("Maciej", "Majka", "08223547852")

    reader1 + book1
    reader2 + book2
    print(Library.Books)

    # try:
    #     while True:
    #         print("Stan Bilblioteki: ", library.Books)
    #         print("Osoby ktore wyporzyczyly ksiazki: ", library.Clients)
    #         print("Co chcesz zrobic:")
    #         print("1 - pożycz książkę")
    #         print("2 - zwróć książkę")
    #         opcja = int(input("Co wybierasz: "))
    #         if opcja == 1:
    #             dane = borrowInput()
    #             library.BorrowBook(dane)
    #         if opcja == 2:
    #             dane = returnInput()
    #             library.ReturnBook(dane)
    #         print()
    #
    # except EOFError:
    #     print()
    #     print("Stan Magazynu:")
    #     for key, value in library.Books.items():
    #         print(f"{key} = {value}")
    #     print()
    #     print("Klienci wypożyczyli")
    #     for key, value in library.Clients.items():
    #         print(f"{key} wypożyczył  {value}")
    #     exit()
