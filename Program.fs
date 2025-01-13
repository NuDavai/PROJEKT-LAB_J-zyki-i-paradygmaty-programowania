(*
//zad 1

printfn "Podaj swoje imie"
let imie = System.Console.ReadLine()
printfn "Witaj %s!" imie

printfn "Podaj swoją masę w kg"
let masa = System.Console.ReadLine()
let floatMasa = float masa

printfn "Podaj swój wzrost w metrach"
let wzrost = System.Console.ReadLine()
let floatWzrost = float wzrost

let BMI = floatMasa/(floatWzrost*floatWzrost)
printfn "Twoje BMI %s wynosi: %F" imie BMI

let przydzielKategorieBMI bmi =
    match bmi with
    | bmi when bmi < 18.5 -> printfn "Masz niedowagę %s" imie
    | bmi when bmi >= 18.5 && bmi < 24.9 -> printfn "Jestes ok ;) %s" imie
    | bmi when bmi <= 25 -> printfn "Jestes gruby %s" imie

przydzielKategorieBMI BMI *)


(*
//zad 2
let EUR2USD = 1.03
let EUR2CNY = 7.52 
let USD2EUR = 0.98 
let USD2CNY = 7.33 
let CNY2EUR = 0.13 
let CNY2USD = 0.14 

printfn "EUR2USD: %F" EUR2USD

printfn " ## Witamy w kantorze w F#! ## "
printfn "Ile masz pieniędzy?: "
let piniondze = System.Console.ReadLine()
let floatPiniondze = float piniondze
let mutable nowaKwota = 0.0
printfn "Dostępne kursy wymian: "
printfn "1. EUR2USD"
printfn "2. EUR2CNY"
printfn "3. USD2EUR"
printfn "4. USD2CNY"
printfn "5. CNY2EUR"
printfn "6. CNY2USD"
printfn "7. Wyjście"
let rec pętla () =
    printf "Wybierz opcję od 1 do 7: "
    let opcja = System.Console.ReadLine()
    match opcja with
    | "1" ->
        printfn "Kurs EUR2USD wynosi: %f" EUR2USD
        nowaKwota <- floatPiniondze * EUR2USD
        printfn "Twoje pieniądze po przewalutowaniu wynoszą: %f USD" nowaKwota
        pętla() 
    | "2" ->
        printfn "Kurs EUR2CNY wynosi: %f" EUR2CNY
        nowaKwota <- floatPiniondze * EUR2CNY
        printfn "Twoje pieniądze po przewalutowaniu wynoszą: %f CNY" nowaKwota
        pętla() 
    | "3" ->
        printfn "Kurs USD2EUR wynosi: %f" USD2EUR
        nowaKwota <- floatPiniondze * USD2EUR
        printfn "Twoje pieniądze po przewalutowaniu wynoszą: %f EUR" nowaKwota
        pętla() 
    | "4" ->
        printfn "Kurs USD2CNY wynosi: %f" USD2CNY
        nowaKwota <- floatPiniondze * USD2CNY
        printfn "Twoje pieniądze po przewalutowaniu wynoszą: %f CNY" nowaKwota
        pętla() 
    | "5" ->
        printfn "Kurs CNY2EUR wynosi: %f" CNY2EUR
        nowaKwota <- floatPiniondze * CNY2EUR
        printfn "Twoje pieniądze po przewalutowaniu wynoszą: %f EUR" nowaKwota
        pętla() 
    | "6" ->
        printfn "Kurs CNY2USD wynosi: %f" CNY2USD
        nowaKwota <- floatPiniondze * CNY2USD
        printfn "Twoje pieniądze po przewalutowaniu wynoszą: %f USD" nowaKwota
        pętla() 
    | "7" ->
        printfn "Wyjście. Dziękujemy ze skorzystania z kalkulatora!"
        () 
    | _ ->
        printfn "Wybrałeś złą opcję"
        pętla() 

pętla() *)


// zad 3
let tekst = "Baba siała mak. Nie wiedziała jak. Dziadek wiedział, nie powiedział, a to było tak."

let listaZnakow = List.ofSeq tekst

let mutable licznikZnakow = 0
for znak in listaZnakow do
    if znak <> ' ' then
        licznikZnakow <- licznikZnakow + 1

printfn "licznikZnakow: %i" licznikZnakow

//printfn "listaZnakow[0] = %c" listaZnakow[0]

(* let mutable licznikSlow = 0
for znak in listaZnakow do
    if znak = ' ' then
        licznikSlow <- licznikSlow + 1

printfn "licznikSlow: %i" licznikSlow *)


let licznikSlow =
    List.fold (fun (acc, flaga) x -> 
        if x = ' ' && flaga then
            (acc + 1, false)
        elif x = ' ' then
            (acc + 1, flaga)
        elif x = '.' || x = ',' then
            (acc, true)  
        else
            (acc, flaga))  
        (1, false)   
        listaZnakow

let liczbaSlow = fst licznikSlow
printfn "Liczba słów: %d" liczbaSlow