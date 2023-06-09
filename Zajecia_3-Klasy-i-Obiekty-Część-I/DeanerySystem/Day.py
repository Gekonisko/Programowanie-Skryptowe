from enum import Enum

import self


class Day(Enum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6

    def difference(self, day):
        distance = day.value - self.value
        if distance > 0:
            reversDistance = distance - 7
        else:
            reversDistance = distance + 7
        if abs(reversDistance) < abs(distance):
            return reversDistance
        return distance


def nthDayFrom(n, day):
    return Day((day.value + n) % 7)
