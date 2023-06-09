from Zajecia_5.Klasa_abstrakcyjna.BasicTimetable import BasicTimetable, Term, Lesson, Action


class Timetable(BasicTimetable):
    def parse(self, actions):
        pass

    def perform(self, actions):
        pass

    def busy(self, term):
        pass

    def put(self, lesson):
        pass


# Sprawdź, czy można tworzyć instancję klasy abstrakcyjnej — 'BasicTimetable'

# Nie da się bo zawiera abstrakcyjne metody
# timeTable = BasicTimetable()

# Sprawdź, czy można tworzyć instancję klasy pochodnej — 'Timetable'
timeTable = Timetable()

# Wywołujemy metodę, która NIE JEST zdefiniowana w klasie 'Timetable', a w klasie 'BasicTimetable'
timeTable.get(Term)
timeTable.busy(Term)
timeTable.put(Lesson)
timeTable.parse([str])
timeTable.perform([Action])
