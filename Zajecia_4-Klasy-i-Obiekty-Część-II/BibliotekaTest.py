import unittest

from Zajecia_4.Biblioteka import Library, LibraryData, Reader, Book


class BibliotekaTest(unittest.TestCase):

    def test(self):
        library = Library("ksiazki.txt")
        book1 = Book.BaseData("Max Kolanko", "Kroniki Prezydentury")
        book2 = Book.BaseData("MEDUSA", "23 kilometry do")
        reader1 = Reader("Nalaia", "Legalna", "08223547851")
        reader2 = Reader("Maciej", "Legalna", "08223547852")

        reader1 + book1
        reader2 + book2

        self.assertEqual(len(library.Books), 2)
        self.assertEqual(len(library.Readers), 2)
        self.assertEqual(library.Books.get(book1.idKsiazki).idKsiazki, book1.idKsiazki)
        self.assertEqual(library.Books.get(book2.idKsiazki).idKsiazki, book2.idKsiazki)
        self.assertEqual(library.Readers.get(reader1.pesel).pesel, reader1.pesel)
        self.assertEqual(library.Readers.get(reader2.pesel).pesel, reader2.pesel)

        reader1 - book1

        self.assertEqual(library.Books.get(book1.idKsiazki), None)
        self.assertEqual(library.Readers.get(reader1.pesel), None)

        # library.BorrowBook(LibraryData("Potop", 2, "Marcin"))
        # library.BorrowBook(LibraryData("Wiedzmin Miecz Przeznaczenia", 8, "Mirek"))
        # self.assertEqual(library.Clients.__contains__('Marcin'), True)
        # self.assertEqual(library.Clients["Marcin"] == {'Potop': 2}, True)
        # self.assertEqual(library.Clients["Mirek"] == {'Wiedzmin Miecz Przeznaczenia': 8}, True)
        # library.ReturnBook(LibraryData("Potop", 1, "Marcin"))
        # library.ReturnBook(LibraryData("Wiedzmin Miecz Przeznaczenia", 4, "Mirek"))
        # library.ReturnBook(LibraryData("Wies", 4, "Marcin"))
        # self.assertEqual(library.Clients["Marcin"] == {'Potop': 1}, True)
        # self.assertEqual(library.Clients["Mirek"] == {'Wiedzmin Miecz Przeznaczenia': 4}, True)
        # self.assertEqual(library.Clients["Marcin"] == {'Wies': 4}, False)




if __name__ == '__main__':
    unittest.main()
    unittest.main()
