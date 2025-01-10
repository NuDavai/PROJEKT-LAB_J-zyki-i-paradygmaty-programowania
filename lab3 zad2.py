class Employee:
    def __init__(self, fname, lname, age, salary):
        self.firstname = fname
        self.lastname = lname
        self.age = age
        self.salary = salary
    def info(self):
        print(f"Pracownik o imieniu {self.firstname} i nazwisku {self.lastname}, lat {self.age} zarabia {self.salary}zl")

pracownikAreczek = Employee("Areczek", "Kowalski", 28, 3000)
pracownikAreczek.info()

listaPracownikow = []
class EmployeeManager(Employee):
    def __init__(self, fname, lname, age, salary, list):
        super().__init__(fname, lname, age, salary)
        self.listaPracownikow = list
    def DodajPracownika(self, fname, lname, age, salary):
        pracownik = []
        pracownik.append(self.firstname)
        pracownik.append(self.lastname)
        pracownik.append(self.age)
        pracownik.append(self.salary)
        self.listaPracownikow.append(pracownik)
        print(self.listaPracownikow)
    def WyswietlListe(self):
        print(listaPracownikow)
    def UsunPracownikaPoWieku(self, wiekMin, wiekMax):
        czyZnalezionoPracownikaDoUsuniecia = False
        for i in range(len(listaPracownikow)):
            if self.listaPracownikow[i][2] < wiekMax and self.listaPracownikow[i][2] > wiekMin:
                print(f"Usunieto pracownika {self.listaPracownikow[i]}")
                self.listaPracownikow.pop(i)
                czyZnalezionoPracownikaDoUsuniecia = True
        if not czyZnalezionoPracownikaDoUsuniecia:
            print("W podanym przedziale nie znaleziono pracownikow do usuniecia")
    def WyszukiwaniePracownikaPoImieniuINazwisku(self, imie, nazwisko):
        x = 0
        for i in range(len(listaPracownikow)):
            if self.listaPracownikow[i][0] == imie and self.listaPracownikow[i][1] == nazwisko:
                print(f"Wyszukano pracownika o podanym imieniu i nazwisku: {self.listaPracownikow[i]}")
                x = 1
        if x == 0:
            print("Nie znaleziono pracownika o podanym imieniu i nazwisku")
    def PodwyzkaMaker(self, imie, nazwisko, siano):
        x = 0
        for i in range(len(listaPracownikow)):
            if self.listaPracownikow[i][0] == imie and self.listaPracownikow[i][1] == nazwisko:
                print(f"Znaleziono pracownika {imie} {nazwisko} i podwyzszono jego pensje o {abs(self.listaPracownikow[i][3]-siano)}zl")
                self.listaPracownikow[i][3] = siano
                x = 1
        if x == 0:
            print("Nie znaleziono pracownika o podanym imieniu i nazwisku, wiec nie podwyzszono mu pensji")

JanuszSknerski = EmployeeManager("Janusz", "Sknerski", 45, 9000, listaPracownikow) #obiekty nazywane są imieniem i nazwiskiem zaczynając z duzych liter, pisane łącznie
JanuszSknerski.DodajPracownika("Janusz", "Sknerski", 45, 9000)
JanuszSknerski.WyswietlListe()
JanuszSknerski.UsunPracownikaPoWieku(40,50)
JanuszSknerski.UsunPracownikaPoWieku(30,40)
JanuszSknerski.DodajPracownika("Janusz", "Sknerski", 45, 9000)
MichałDrzymała = EmployeeManager("Michał", "Drzymała", 32, 9999, listaPracownikow)
MichałDrzymała.DodajPracownika("Michał", "Drzymała", 32, 9999)
MichałDrzymała.WyszukiwaniePracownikaPoImieniuINazwisku("Janusz", "Sknerski")
AreczekKowalski = EmployeeManager("Areczek", "Kowalski", 28, 3000, listaPracownikow)
AreczekKowalski.DodajPracownika("Areczek", "Kowalski", 28, 3000)
AreczekKowalski.PodwyzkaMaker("Areczek", "Kowalski", 3599)


def EmployeesSystemProject(listaPracownikow):
    print("Witaj w menadżerze do zarządzania twoimi pracownikami!")
    print("Masz do wyboru opcje: ")
    print("1. Dodawanie nowych pracowników")
    print("2. Wyświetlanie listy istniejących pracowników")
    print("3. Usuwanie pracowników na podstawie przedziału wiekowego")
    print("4. Aktualizacja wynagrodzeń pracowników według nazwiska")
    print("5. Exit")
    print("Aby wybrać którąś z powyższych opcji wpisz jej numer")
    while True:
        operacja = int(input("Jaką operacje wybierasz? "))
        if operacja == 1:
            imie = input("Wprowadz imie pracownika: ")
            nazwisko = input("Wprowadz nazwisko: ")
            wiek = input("Wprowadz wiek: ")
            zarobki = input("Wprowadz zarobki: ")
            pracownik = []
            pracownik.append(imie)
            pracownik.append(nazwisko)
            pracownik.append(wiek)
            pracownik.append(zarobki)
            listaPracownikow.append(pracownik)
            nowyPracownik = str(imie) + str(nazwisko)
            instrukcja = "nowyPracownik = EmployeeManager(imie, nazwisko, wiek, zarobki, listaPracownikow)"
            try:
                wynik = exec(instrukcja)
                print(wynik)
            except:
                print("BŁĄD: przy dodawaniu nowego pracownika wystąpił błąd")
            print(f"Dodano pracownika {pracownik}")

        elif operacja == 2:
            print("Pracownicy wprowadzeni do systemu: ")
            for pracownik in listaPracownikow:
                print(pracownik)

        elif operacja == 3:
            print("W jakim przedziale wiekowym chcesz usunąć pracownikow?")
            od = int(input("Od: "))
            do = int(input("do lat: "))
            listaPracownikowDoDelete = []
            for pracownik in listaPracownikow:
                if pracownik[2] > od and pracownik[2] < do:
                    imieINazwisko = str(pracownik[0]) + str(pracownik[1])
                    listaPracownikowDoDelete.append(imieINazwisko)
            for pracownikWon in listaPracownikowDoDelete:
                instrukcja = str(pracownikWon) + ".UsunPracownikaPoWieku(od,do)"
                try:
                    exec(instrukcja)
                except:
                    print(f"BŁĄD: przy usuwaniu pracowników w przedziale wiekomym od {od} do {do} lat")

        elif operacja == 4:
            print("Podaj imie i nazwisko pracownika, ktoremu chcesz dac podwyzke")
            imie = input("Imie: ")
            nazwisko = input("Nazwisko: ")
            podwyzka = int(input("Ile ma wynosić nowa pensja?: "))
            imieINazwisko = str(imie) + str(nazwisko)
            instrukcja = imieINazwisko + ".PodwyzkaMaker(" + '"' + imie + '"' + ", " + '"' + nazwisko + '"' + ", " + str(podwyzka) + ")"
            try:
                exec(instrukcja)
            except:
                print(f"BŁĄD: przy dawaniu podwyżki panu {imie} {nazwisko}")

        elif operacja == 5:
            print("Działanie Employees System Project zostaje zakończone!")
            break

        else:
            print("Podano błędny numer operacji")



EmployeesSystemProject(listaPracownikow)