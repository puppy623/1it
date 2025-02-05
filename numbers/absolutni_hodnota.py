#absolutni hodnota
#vstup: cislo
#vystup: absolutni hodnota cisla

a = float(input("Zadejte cislo: "))
if a < 0:
    a = -a
print("Absolutni hodnota cisla je", a)