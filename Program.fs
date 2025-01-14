//zad 1
printfn "####### zad 1"
let rec Fibonacchi n =
    if n <= 1 then n
    else Fibonacchi(n-1) + Fibonacchi(n-2)

let wynik = Fibonacchi 4
printfn "Fibonacchi dla n = 4 wynosi: %d" wynik

let FibTail n =
    let rec loop n =
        if n <= 1 then n
        else loop(n-1) + loop(n-2)
    loop n

let wynik1 = FibTail 4
printfn "Fibonacchi (tail) dla n = 4 wynosi: %d" wynik1

//zad 2
printfn "####### zad 2"
//let rec permutacje lista =
//    let rozmiarListy = List.length lista
//    if rozmiarListy = 1 then
//        printfn "%A" lista
//
//    let mutable wyniki = []
//
//    for i in 0 .. rozmiarListy do
//        let mutable reszta = lista[i] + lista[i+1]
//
//        for perm in permutacje reszta do
//            let mutable wyniki = listaAdd wyniki lista[i]
//            let mutable wyniki = List.append wyniki perm
//            printfn "dupa"
//    printfn "wynik: %A" wyniki

let rec permutacje lista =
    match lista with
    | [] -> [[]] 
    | [x] -> [[x]] 
    | _ -> 
        lista
        |> List.collect (fun x ->
            let reszta = List.filter (fun y -> y <> x) lista
            printfn "x: %i, reszta: %A" x reszta
            permutacje reszta
            |> List.map (fun perm -> x :: perm))  

let lista = [1; 2; 3]
let wyniki = permutacje lista

printfn "Wszystkie możliwe permutacje listy %A wynoszą: %A" lista wyniki