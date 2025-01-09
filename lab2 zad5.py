
def SystemDynamicznegoGenerowaniaKodów():
    listaNazwSzablonów = []
    listaSzablonów = []
    listaZmiennych = []
    listaTypowZmiennych = []
    print("Witaj w Systemie Dynamicznego Generowania Kodów SDGK!")
    print("")
    print("W swojej ofercie mamy do wyboru operacje: ")
    print("1. Wprowadź zmienne")
    print("2. Wyświetl wprowadzone zmienne")
    print("3. Wprowadź szablon działania")
    print("4. Wykonaj wprowadzony szablon działania")
    print("5. Wyjście")
    while True:
        operacja = int(input("## Wybierz operację wpisując numer od 1 do 5: "))
        if operacja == 1:
            print("Dotychczasowo wprowadzone zmienne: ")
            print(listaZmiennych)
            licznikPętli = int(input("Ile chcesz wprowadzić zmiennych?: "))
            for i in range(licznikPętli):
                nazwaZmiennej = chr(97 + len(listaZmiennych))
                y = input(f"Wprowadź typ (int, chr, str) nowej zmiennej {nazwaZmiennej}: ")
                if y == "int":
                    listaTypowZmiennych.append(type(1))
                elif y == "chr":
                    listaTypowZmiennych.append(type('c'))
                elif y == "str":
                    listaTypowZmiennych.append(type("str"))
                x = input(f"Wprowadź wartość nowej zmiennej {nazwaZmiennej}: ")
                listaZmiennych.append(x)
        elif operacja == 2:
            print("Dotychczasowo wprowadzone zmienne: ")
            for i in range(len(listaZmiennych)):
                print(f"{chr(97 + i)} = {listaZmiennych[i]}")
        elif operacja == 3:
            flaga = True
            while flaga:
                nowaNazwaSzablonu = input("Wprowadź nazwę nowego szablonu: ")
                if nowaNazwaSzablonu in listaNazwSzablonów:
                    print("Wprowadzona nazwa szablonu już istnieje")
                else:
                    flaga = False
            nowySzablon = input("Wprowadź nowy szablon zaczynając od definicji (np. def f(x): return x): ")
            listaNazwSzablonów.append(nowaNazwaSzablonu)
            listaSzablonów.append(nowySzablon)
            print("Szablon został wprowadzony poprawnie!")
        elif operacja == 4:
            print("Wprowadzone szablony: ")
            for i in range(len(listaNazwSzablonów)):
                print(f"{i+1}. {listaNazwSzablonów[i]}")
            nrSzablonu = int(input("Który numer szablonu chcesz wykonać?: "))
            print(str(listaSzablonów[nrSzablonu-1]))
            print("Lista zmiennych: ")
            for i in range(len(listaZmiennych)):
                print(f"{chr(97 + i)} = {listaZmiennych[i]}")
            zmienna = input("Której zmiennej chcesz użyć?: ")
            x = listaZmiennych[ord(zmienna)-97]
            print(type(x))
            if listaTypowZmiennych[ord(zmienna) - 97] == type(1):
                suma = 0
                for i in range(len(x)):
                    suma = suma + (int(x[i]) * pow(10, len(x)-i))
                x = suma
            else:
                x = '"' + x + '"'

            nazwaFunkcji = ""
            listaZnakowFunkcji = []
            for i in listaSzablonów[nrSzablonu-1]:
                listaZnakowFunkcji.append(i)
            for i in range(4, len(listaZnakowFunkcji)):
                if listaZnakowFunkcji[i] == '(':
                    break
                else:
                    nazwaFunkcji = nazwaFunkcji + listaZnakowFunkcji[i]

            cialoFunkcji = str(listaSzablonów[nrSzablonu-1]) + "\n" + str(nazwaFunkcji) + "(" + str(x) + ")"
            print(cialoFunkcji + " = ")

            try:
                wynik = exec(cialoFunkcji)
                print(wynik)
            except:
                print("BŁĄD: Działanie szablonu jest niepoprawne")

        elif operacja == 5:
            print("Działanie Systemu Dynamicznego Generowania Kodów SDGK zostało zakończone")
            break


SystemDynamicznegoGenerowaniaKodów()
