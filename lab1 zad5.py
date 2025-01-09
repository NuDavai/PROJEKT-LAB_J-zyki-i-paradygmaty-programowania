Zadania = [[0,3,2], [4,7,2], [6,9,3], [10,15,10], [11, 13, 20], [12, 16, 30]] # lista w liscie w ktorej pierwszy element elementu jest czasem rozpoczecia, drugi zakonczenia, a trzeci nagrodą
listaNumerowWykonanychZadan = []
sumaNagród = 0

zadaniaPosortowane = sorted(Zadania, key=lambda x: x[1])

czasZakonczeniaOstatniegoZadania = 0
for i in range(len(zadaniaPosortowane)):
    if czasZakonczeniaOstatniegoZadania <= zadaniaPosortowane[i][0]:
        listaNumerowWykonanychZadan.append(i)
        sumaNagród = sumaNagród + zadaniaPosortowane[i][2]
        czasZakonczeniaOstatniegoZadania = zadaniaPosortowane[i][1]

print("Id wykonanych zadań: ")
print(listaNumerowWykonanychZadan)
print("Suma nagród: ")
print(sumaNagród)