from Search_Algorithm import SearchAlgorithm


# Bread First Search - stosujemy kolejke FIFO
class BFS(SearchAlgorithm):
    def find_solution(self):
        if self.is_solution(self.state):
            return self.state.move_set, self.max_depth, 1, 1
        # dopoki sa stany do sprawdzenie
        while self.frontier.__len__() > 0:
            # zdejmij stan
            self.state = self.frontier.pop()
            self.processed += 1
            # sprawdz maks glebokosc
            if self.max_depth < self.state.depth:
                self.max_depth = self.state.depth
            # generuj sasiednie stany
            for state in self.generate_next_states():
                if self.is_solution(state):
                    self.visited += 1
                    return state.move_set, self.max_depth, self.visited, self.processed
                # jesli stan nie byl przetworzony to trzeba go sprawdzic - dodaj do kolejki wedlug fifo
                elif state not in self.explored:
                    self.visited += 1
                    self.frontier.appendleft(state)
            self.explored.append(self.state)


