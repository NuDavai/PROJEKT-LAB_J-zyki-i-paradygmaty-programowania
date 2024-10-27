listaCzasuZadań = [5, 10, 15, 20, 26, 30] #w sekundach
listaNagródZadań = [5, 8, 10, 30, 25, 25] #w zlotowkach
listaStosunkuNagrodyDoCzasu = []
for i in range(len(listaCzasuZadań)):
    listaStosunkuNagrodyDoCzasu.append(listaNagródZadań[i]/listaCzasuZadań[i])

listaKolejności = []
listaStosunkuNagrodyDoCzasuSorted = sorted(listaStosunkuNagrodyDoCzasu, reverse=True)

for i in range(len(listaStosunkuNagrodyDoCzasu)):
    for j in range(len(listaStosunkuNagrodyDoCzasu)):
        if listaStosunkuNagrodyDoCzasu[j] == listaStosunkuNagrodyDoCzasuSorted[i]:
            listaKolejności.append(j)
            break

print(listaKolejności)
print(sum(listaCzasuZadań))