(*
type Person(name: string, age: int) =
//pola
let mutable _name = name
let mutable _age = age

// właściwości
member this.Name
with get() = _name
and set(value) = _name <- value

member this.Age
with get() = _age
and set(value) = _age <- value

//metody
member this.Introduce() =
printfn "Witaj %s, twoj wiek: %i" _name _age

let person = Person("Jan", 24)
person.Introduce()

//dziedziczenie
type Pracownik(name: string, age: int, position: string) =
inherit Person(name, age)

member this.Position = position

override this.Introduce() =
printfn "Witaj %s lat %i! Pracujesz jako: %s" this.Name this.Age this.Position
*)


(*
//abstrakcja
type IWalkable =
abstract member Walk : unit -> //unit?

type Person(name: string) =
member val Name = name with get, set

interface IWalkable with
member this.Walk () =
printfn "%s chodzi na grzyby" this.Name
*)

(*
//polimorfizm
type Animal() =
member this.Speak() = printfn "Zwierze wydaje głos"

type Dog() =
inherit Animal()
override this.Speak() = printfn "Pies szczeka"
*)

open System
open System.Collections.Generic

//klasa ksiazki
type Book(title: string, author: string, pageCount: int) =
    member this.Title = title
    member this.Author = author
    member this.PageCount = pageCount

    member this.GetInfo() =
        printfn "Tytuł: %s /nAutor: %s /nLiczba stron: %d" this.Title this.Author this.PageCount


//klasa użytkownika
type User(name: string) =
    member this.Name = name
    member this.BorrowedBooks = new List()

    member this.BorrowBook (book: Book) =
        this.BorrowedBooks.Add(book)
        printfn "%s wypożyczył książkę: %s" this.Name book.Title

    member this.ReturnBook (book: Book) =
        if this.BorrowedBooks.Remove(book) then
            printfn "udalo sie..."
        else
            printfn "nie udalo sie..."

//klasa biblioteki
type Library() =
    let books = new List()

    member this.AddBook (book: Book) =
        books.Add(book)
        printfn "dodano.."

    member this.RemoveBook (book: Book) =
        if books.Remove(book) then
            printfn "usunieto..."
        else
            printfn "nie udalo sie usunac ksiazki..."

    member this.ListBooks () =
        printfn "Książki w bibliotece"
        for book in books do
            printfn " - %s" (book.GetInfo())

            []
let main argv =
    let library = Library()

    let book1 = Book("Ksiazka 1 ", "Autor 1", 123)

    library.AddBook(book1)

    library.ListBooks()

    let user = User("Jan K")

    user.BorrowedBooks(book1)

    user.ReturnBook(book1)

    library.ListBooks()