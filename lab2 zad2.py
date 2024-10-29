import numpy as np
import re

A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 4], [6, 8]])
X = A
Y = B

dodawanieMacierzy = """
if X.shape == Y.shape:
    Z = X + Y
    print("Dodawanie macierzy X i Y wynosi:")
    print(Z)
else:
    print("Wymiary macierzy sa różne, podaj poprawne")
"""
exec(dodawanieMacierzy)

mnożenieMacierzy = """
if X.shape == Y.shape:
    Z = X.dot(Y)
    print("Mnożenie macierzy X i Y wynosi:")
    print(Z)
else:
    print("Wymiary macierzy sa różne, podaj poprawne")
"""
exec(mnożenieMacierzy)

transpozycjaMacierzy = """
print("Transpozycja macierzy X: ")
print(X.transpose())
"""

exec(transpozycjaMacierzy)


print("Witaj w kalkulatorze macierzy!")
print("Na macierzach X i Y jest możliwość wykonania trzech operacji: dodawania ich, ich mnożenia i transpozycja macierzy X, ale można też wyświetlić ich zawartość")
print("Dodawanie macierzy następuje po wpisaniu nazwy pierwszej dodawanej macierzy, znaku +, oraz drugiej dodawanej macierzy")
print("Mnożenie macierzy dzieje się kiedy wpiszemy X.dot(Y)")
print("Transponowanie macierzy wydarzy się kiedy wpiszemy X.transpose()")
print("Wyświetlenie macierzy następuje po wpisaniu print(), a w nawiasach nazwę macierzy (np. print(X) )")
print("Aby wprowadzić macierz X trzeba wpisać na przykład X = np.array([[1, 2], [3, 4]])")
print("Aby wyjść z kalkulatora należy wpisać słowo exit")
while True:
    operacja = input("Podaj twoją operacje: ")
    if operacja == "X + Y":
        if X.shape == Y.shape:
            print("Dodawanie macierzy X i Y wynosi:")
            exec(operacja)
        else:
            print("Wymiary dodawanych macierzy są różne, podaj poprawne macierze")
    elif operacja == "X.dot(Y)":
        if X.shape == Y.shape:
            print("Mnożenie macierzy X i Y wynosi:")
            exec(operacja)
        else:
            print("Wymiary mnożonych macierzy są różne, podaj poprawne macierze")
    elif operacja == "X.transpose()":
        print("Transpozycja macierzy X: ")
        print(X.transpose())
    elif operacja == "print(X)":
        exec(operacja)
    elif operacja == "print(Y)":
        exec(operacja)
    elif operacja == "X = ":# TU COS TRZA
    elif operacja == "exit":
        break
    else:
        print("Podałeś złą nazwę operacji")




