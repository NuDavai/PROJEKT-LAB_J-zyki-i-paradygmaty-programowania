// lab6
// zad 1
printfn "zad 1"
open System

let tekst = "Geralt: Co jest w garnku?
Troll: Zupa z elfów i cebuli. Dobra. Chcesz jeść?
Geralt: Nie lubię cebuli.
Troll: Głupiś! Elf z cebulą dobry! Jak pomidor!"

printfn "%s" tekst

// liczba slow
let slowaWTekscie (text: string) =
    text.Split([|' '; '.'; ','; '\n'|], System.StringSplitOptions.RemoveEmptyEntries)
    |> Array.length

let liczbaSlow = slowaWTekscie tekst
printfn "Liczba slow w tekscie wynosi: %i" liczbaSlow

//liczba znakow (bez spacji)
let mutable licznik = 0
for i in tekst do
    if i <> ' ' then
        licznik <- licznik + 1
printfn "Liczba znakow w tekscie: %i" licznik

// zad 2
printfn "zad 2"
let palindrom = "kajak"
let niePalindrom = "jabłko"

let czyPalindrom (slowo: string) = 
    let dlugoscSlowa = String.length slowo
    let mutable flaga = true

    for i in 0 .. dlugoscSlowa-1 do
       if slowo[i] <> slowo[dlugoscSlowa - 1 - i] then
            flaga <- false

    if flaga = false then
        printfn "Słowo %s nie jest palindromem" slowo
    else
        printfn "Słowo %s jest palindromem" slowo

let test1 = czyPalindrom palindrom
let test2 = czyPalindrom niePalindrom

// zad 3
printfn "zad 3"

let listaZDuplikatami = ["cola"; "fanta"; "pepsi"; "cola"; "kawa"; "woda"; "cola"]

let sprawdzarkaDuplikatow (lista: string list)= 
    let rozmiarListy = List.length lista
    printfn "rozmiar tablicy wynosi: %i" rozmiarListy
    let mutable listaIndeksowDuplikatow = []
    for i in 0 .. rozmiarListy-1 do
        for j in i .. rozmiarListy-1 do
            if lista[i] = lista[j] then
                listaIndeksowDuplikatow <- [i] |> List.append listaIndeksowDuplikatow
    printfn "lista indeksow duplikatow: %A" listaIndeksowDuplikatow

    //let rozmiarListyIndeksow = List.length listaIndeksowDuplikatow
    //for i in 0 .. rozmiarListyIndeksow-1 do
    //    let mutable nowaLista = List.removeManyAt i lista
    //    printfn "dupa"
    //printfn "lista bez duplikatów %A" nowaLista

let testDuplikatow = sprawdzarkaDuplikatow listaZDuplikatami
