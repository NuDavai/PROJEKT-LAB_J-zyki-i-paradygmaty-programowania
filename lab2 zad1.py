tekst = """
Geralt: Co jest w garnku? 
Troll: Zupa z elfów i cebuli. Dobra. Chcesz jeść? 
Geralt: Nie lubię cebuli. 
Troll: Głupiś! Elf z cebulą dobry! Jak pomidor! 
"""

# ilosc zdan (ma byc 8)
liczbaZdań = list(filter(lambda x: x == "." or x == "!" or x == "?", tekst))
print(f"Ilość zdań w tekście wynosi: {len(liczbaZdań)}")

# ilosc slow (ma byc 26)
liczbaSłów = list(filter(lambda x: x == " " or x == ". " or x == "! " or x == ": " or x == "? ", tekst))
print(f"Ilość słów w tekście wynosi: {len(liczbaSłów)}")

# ilosc akapitow (ma byc 5)
liczbaAkapitów = list(filter(lambda x: x == "\n", tekst))
print(f"Ilość akapitów w tekście wynosi: {len(liczbaAkapitów)}")

# ilosc stop words (ma byc 3)
liczbaStopWords = list(filter(lambda x: x == " z " or x == " i " or x == " oraz " or x == " lub ", tekst))
print(f"Ilość stop words w tekście wynosi: {len(liczbaStopWords)}")


# odwracanie wyrazow na "c"
import re
słowaNaC = re.findall(r'\bc\w+', tekst)
słowaNaCReversed = [i[::-1] for i in słowaNaC]
print(słowaNaCReversed)

