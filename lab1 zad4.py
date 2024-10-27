listaWag = [1.5, 0.5, 2, 1, 3, 0.5, 1] #w kg, laptop, komorka, woda 2l, ksiązki, buty, batoniki, portfel, kilo cukru
listaWartości = [3000, 1500, 2, 200, 200, 4000, 5] #w zł
maxWagaPlecaka = 5 #w kg

listaKolejnosciWag = []
listaKolejnosciWartosci =[]

for i in range(len(listaWartości)):
    for j in range(len(listaWartości)):
        if listaWartości[j] == max(listaWartości):
            listaKolejnosciWartosci.append(max(listaWartości))
            listaKolejnosciWag.append(listaWag[j])
            listaWartości[j] = 0
            listaWag[j] = 0
            break

print(listaKolejnosciWag)
print(listaKolejnosciWartosci)

sumaWag = 0
sumaWartosci = 0
for i in range(len(listaKolejnosciWag)):
    if listaKolejnosciWag[i] + sumaWag <= maxWagaPlecaka:
        sumaWag = listaKolejnosciWag[i] + sumaWag
        sumaWartosci = listaKolejnosciWartosci[i] + sumaWartosci

print(sumaWag)
print(sumaWartosci)