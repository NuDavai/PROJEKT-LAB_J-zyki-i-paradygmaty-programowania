listaWag = [10, 5, 15, 20]
maksWaga = 25

def funkcja(listaWag, maksWaga):
    kursy = 0
    for i in range(len(listaWag)-1):
        j = i + 1
        while j < len(listaWag):
            if listaWag[i] + listaWag[j] == maksWaga:
                kursy = kursy + 1
                print(f"kurs nr: {kursy}, zapakowano paczki o wagach {listaWag[i]} i {listaWag[j]}")
                break
            j = j + 1
    print(f"Minimalna liczba kursów: {kursy}")

funkcja(listaWag, maksWaga)


