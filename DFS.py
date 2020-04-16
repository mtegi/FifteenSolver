from Search_Algorithm import SearchAlgorithm


# Depth First Search - stosujemy kolejke LIFO
class DFS(SearchAlgorithm):
    def __init__(self, initial_state, search_order):
        super().__init__(initial_state, search_order)
        self.max_possible_depth = 19

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
                # jesli nie jestesmy za gleboko
                if self.state.depth < self.max_possible_depth:
                    # dodaj do przeszukanych
                    self.explored.append(self.state)
            # generuj sasiednie stany
                    for state in self.generate_next_states():
                # jesli stan nie byl przetworzony to trzeba go sprawdzic - dodaj do kolejki wedlug fifo
                        if state not in self.explored:
                            self.frontier.append(state)
            # aktualizuj liczniki stanow
            self.visited = len(self.frontier) + len(self.explored)
            self.processed = len(self.explored)
