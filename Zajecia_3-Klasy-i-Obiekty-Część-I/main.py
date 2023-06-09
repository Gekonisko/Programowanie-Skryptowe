from klasa import Klasa
from Zajecia_3.DeanerySystem.Day import Day


print(Day.nthDayFrom(10, Day.SAT))



obiekt = Klasa([4, 5, 6], 10, 20)

print(obiekt.tab)
print(obiekt._zmienna1)
print(obiekt._zmienna2)


obiekt1 = Klasa(['a', 'b', 'c'],1,2)
obiekt2 = Klasa(['x', 'y', 'z'],3,4)
print('*' * 30)
print("Po utworzeniu obiektów")
print('\tKlasa.tab   ->', Klasa.tab)
print('\tobiekt1.tab ->', obiekt1.tab)
print('\tobiekt2.tab ->', obiekt2.tab)
print('-' * 10)
Klasa.tab = [4, 5, 6]
print("Po wykonaniu instrukcji \u001b[31mKlasa.tab = [4, 5, 6]\u001b[0m'")
print('\tKlasa.tab   ->', Klasa.tab)
print('\tobiekt1.tab ->', obiekt1.tab)
print('\tobiekt2.tab ->', obiekt2.tab)
print('-' * 10)
print("Po wykonaniu instrukcji \u001b[31mobiekt1.tab = [7, 8, 9]\u001b[0m'")
obiekt1.tab = [7, 8, 9]
print('\tKlasa.tab   ->', Klasa.tab)
print('\tobiekt1.tab ->', obiekt1.tab)
print('\tobiekt2.tab ->', obiekt2.tab)
print('-' * 10)
print(
    "Po wykonaniu instrukcji '\u001b[31mobiekt2.tab = [-3, -2, -1]\u001b[0m'")
obiekt2.tab = [-3, -2, -1]
print('\tKlasa.tab   ->', Klasa.tab)
print('\tobiekt1.tab ->', obiekt1.tab)
print('\tobiekt2.tab ->', obiekt2.tab)
print('*' * 30)

