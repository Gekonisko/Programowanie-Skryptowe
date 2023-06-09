import re


def PrintWord(txt):
    if len(txt) > 0:
        print("Wyraz: " + txt)


if __name__ == '__main__':
    text = 'psów20342fdsfsd 4342 r3& few3423'
    offset = 0
    m = re.search('[0-9]+', text[offset:])
    while m is not None:
        PrintWord(text[0:m.start()])
        print("Liczba: " + m.group(0))
        offset += m.end()
        m = re.search('[0-9]+', text[offset:])
    PrintWord(text[offset:])
