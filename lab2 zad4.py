import numpy as np
import functools as func

A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 4], [6, 8]])
C = np.array([[3, 6], [9, 12]])
D = np.array([[4, 8], [12, 16]])

listaMacierzy = []
listaMacierzy.append(A)
listaMacierzy.append(B)
listaMacierzy.append(C)
listaMacierzy.append(D)

def mnożenieMacierzy(listaMacierzy):
    for i in range(len(listaMacierzy)-1):
        if listaMacierzy[i].shape != listaMacierzy[i+1].shape:
            print("Podane macierze mają różne wymiary; mnożenie niemożliwe")
            break
    macierzKoncowa = []
    macierzKoncowa.append(listaMacierzy[0])
    i = 1
    while i < len(listaMacierzy):
        macierzKoncowa = np.dot(macierzKoncowa, listaMacierzy[i])
        i = i + 1
    print(macierzKoncowa)

def matrixOperator(listaMacierzy):
    print("Witaj w operatorze macierzy (cos w stylu kalkulatora na macierzach tylko, że na liscie w ktorej sa wszystkie macierze i operacja jest stosowana dla nich wszystkich)")
    print("Podałeś następującą listę macierzy: ")
    for macierz in listaMacierzy:
        print(macierz)
    while True:
        operacja = input("Jaką operacje chcesz teraz wykonać? (dodawanie, mnożenie, niestandardowa operacja, exit):  ")
        if operacja == "dodawanie":
            print("Wynik dodawania macierzy w liście: ")
            print(func.reduce(lambda A, B: A + B, listaMacierzy))
        elif operacja == "mnożenie":
            print("Wynik mnożenia macierzy z listy: ")
            mnożenieMacierzy(listaMacierzy)
        elif operacja == "niestandardowa operacja":
            kod = input("Podaj kod twojej operacji: ")
            try:
                wynik = eval(kod)
                print("Wynikiem twojego kodu jest: ")
                print(wynik)
            except:
                print("BŁĄD: Wpisałeś niepoprawny kod")
        elif operacja == "exit":
            break
        else:
            print("Podałeś niewłaściwą nazwę operacji")
    print("Działanie programu matrixOperator zostało zakończone")

matrixOperator(listaMacierzy)