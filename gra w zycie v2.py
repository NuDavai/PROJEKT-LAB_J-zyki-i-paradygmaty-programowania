import time
from typing import List
import matplotlib.pyplot as plt
import numpy as np
import random

class Komorka:
    def __init__(self, is_alive: bool = False):
        self.is_alive = is_alive

class Plansza:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = [[Komorka(False) for _ in range(cols)] for _ in range(rows)]

    def set_alive(self, row: int, col: int):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col].is_alive = True

    def randomize(self, probability: float = 0.2):
        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col].is_alive = random.random() < probability

    def count_alive_neighbors(self, row: int, col: int) -> int:
        sąsiedzi = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        count = 0
        for xSąsiada, ySąsiada in sąsiedzi:
            x, y = row + xSąsiada, col + ySąsiada
            if 0 <= x < self.rows and 0 <= y < self.cols:
                count = count + self.grid[x][y].is_alive
        return count

    def next_generation(self):
        new_grid = [[Komorka() for j in range(self.cols)] for i in range(self.rows)]

        for row in range(self.rows):
            for col in range(self.cols):
                alive_neighbors = self.count_alive_neighbors(row, col)
                if self.grid[row][col].is_alive:
                    # Zasada 1 Gry w Życie: Każda komórka mająca dwóch lub trzech żywych sąsiądów przechodzi do następnej rundy
                    new_grid[row][col].is_alive = alive_neighbors in (2, 3)
                else:
                    # Zasada 2 Gry w Życie: Jakakolwiek komórka posiadająca dokładnie 3 martwych sąsiadów ożywa
                    new_grid[row][col].is_alive = alive_neighbors == 3

        self.grid = new_grid

    def to_numpy_array(self):
        return np.array([[1 if cell.is_alive else 0 for cell in row] for row in self.grid])

class GraWZycie:
    def __init__(self, rows: int, cols: int):
        self.board = Plansza(rows, cols)

    def seed_random(self, probability: float = 0.3):
        self.board.randomize(probability)

    def run(self, generations: int, delay: float = 0.5):
        plt.ion()
        fig, ax = plt.subplots()

        for _ in range(generations):
            ax.clear()
            grid_array = self.board.to_numpy_array()
            ax.imshow(grid_array, cmap="binary", extent=[0, self.board.cols, 0, self.board.rows])

            for x in range(self.board.cols + 1):
                ax.axvline(x, color='gray', linewidth=0.5)
            for y in range(self.board.rows + 1):
                ax.axhline(y, color='gray', linewidth=0.5)

            ax.set_title("Symulacja Gry w Życie Conwaya")
            ax.axis("tight")
            ax.set_xticks([])
            ax.set_yticks([])

            plt.pause(delay)
            self.board.next_generation()

        plt.ioff()
        plt.show()

if __name__ == "__main__":
    print("")
    print("Witaj w programie symulującym Gre w Życie Conwaya!")
    print("Defaultowo symulacja wykonuje się na planszy 20 rzędów na 40 kolumn")
    rows, cols = 20, 40
    print("Symulacja gry zostanie stworzona na podstawie losowego prawdobodopieństwa wynoszącego domyślnie 20% szansy na to, że komórka będzie żywa na starcie")
    prawdopodobieństwoSeeda = 0.3
    print("Symulacja Gry w Życie na potrzeby tego projektu będzie mieć domyślnie 50 interacji")
    interacjeSymulacji = 50
    print("Aby zmienić domyślne wartośći wpisz 1, aby uruchomić symulacje wpisz 2")
    while True:
        operacja1 = int(input("[Główne MENU symulacji] Zmiana wartości (1) lub uruchomienie symulacji (2)?: "))
        if operacja1 == 1:
            print("Którą z wartości chcesz zmienić?")
            print(f"1. Rzędy planszy: {rows}")
            print(f"2. Kolumny planszy: {cols}")
            print(f"3. Prawdopodbieństwo (seed) : {prawdopodobieństwoSeeda}")
            print(f"4. Liczba iteracji symulacji : {interacjeSymulacji}")
            print("5. Powrót")
            while True:
                operacja2 = int(input("[MENU zmian wartośći] Podaj numer operacji: "))
                if operacja2 == 1:
                    newRows = int(input("Podaj nową liczbę rzędów: "))
                    rows = newRows
                    print("Zapisano nową wartość!")
                elif operacja2 == 2:
                    newCols = int(input("Podaj nową liczbę kolumn: "))
                    cols = newCols
                    print("Zapisano nową wartość!")
                elif operacja2 == 3:
                    newSeed = float(input("Podaj nowego seeda: "))
                    prawdopodobieństwoSeeda = newSeed
                    print("Zapisano nową wartość!")
                elif operacja2 == 4:
                    newIloscIteracji = int(input("Podaj nową ilość iteracji symulacji: "))
                    interacjeSymulacji = newIloscIteracji
                    print("Zapisano nową wartość!")
                elif operacja2 == 5:
                    break
        if operacja1 == 2:
            break

    gra = GraWZycie(rows, cols)
    gra.seed_random(probability=prawdopodobieństwoSeeda)
    gra.run(generations=interacjeSymulacji, delay=0.5)