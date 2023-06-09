if __name__ == '__main__':
    lancuch1 = "gdy się jest między szalonymi, staje się także szalonym," \
               " a co więcej, znajduje się pewien urok w szaleństwach"
    lancuch2 = "Żyłem jak chciałem i umrę jak mi się podoba." \
               "Szczęście jest zawsze tam, gdzie je człowiek widzi…"

    print((lancuch1 + lancuch2) * 3)
    lancuch = "dowolny tekst"
    print(lancuch[0])
    print(lancuch[:2])
    print(lancuch[2:])
    print(lancuch[-2])
    print(lancuch[-3:])
    print(lancuch[1::2])
    try:
        lancuch[0] = 'a'
    except:
        print("Nieudane przypisanie wartości")
