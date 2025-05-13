#tento program vypisuje text ve sloupci zprava doleva
muj_text = "Ahoj, jak se máš?"
#tento program vypisuje text ve sloupci zprava doleva
def vypis_text_sloupce_zprava_doleva(muj_text):
    #vypis textu ve sloupcích zprava doleva
    for i in range(len(muj_text)):
        print(muj_text[i], end="")
    print()

