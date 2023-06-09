import lista
import slownik
import sys
import getopt
#-*-coding: utf-8-*-
if __name__ == '__main__':
    args = sys.argv[1:]
    optlist, args = getopt.getopt(args, 'x', ['moduł='])
    name = optlist[0][1]
    if name == "lista":
        lista.zapisz(args)
        lista.wypisz()
    if name == "slownik":
        slownik.zapisz(args)
        slownik.wypisz()
