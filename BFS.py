from Search_Algorithm import SearchAlgorithm

# Bread First Search - stosujemy kolejke FIFO
class BFS(SearchAlgorithm):
    def find_solution(self):
        # dopoki sa stany do sprawdzenie
        while self.frontier.__len__() > 0:
            # zdejmij stan
            self.state = self.frontier.pop()
            # sprawdz maks glebokosc
            if self.max_depth < self.state.depth:
                self.max_depth = self.state.depth
            # stan jest rozwiazaniem
            if self.found_solution():
                # zwroc tuple z rzeczami do zapisu do pliku
                return self.state.move_set, self.max_depth, self.visited, self.processed
                break
            else:
                # jesli nie jest dodaj do przeszukanych
                self.explored.append(self.state)
            # generuj sasiednie stany
            for state in self.generate_next_states():
                # jesli stan nie byl przetworzony to trzeba go sprawdzic - dodaj do kolejki wedlug fifo
                if state not in self.explored:
                    self.frontier.appendleft(state)
            # aktualizuj liczniki stanow
            self.visited = len(self.frontier) + len(self.explored)
            self.processed = len(self.explored)
