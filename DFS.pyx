from Search_Algorithm import SearchAlgorithm, can_move, generate_new_state, is_not_back_move


# Depth First Search - stosujemy kolejke LIFO
class DFS(SearchAlgorithm):
    def __init__(self, initial_state, search_order):
        super().__init__(initial_state, search_order)
        self.max_possible_depth = 22
    def find_solution(self):
        if self.is_solution(self.state):
            return self.state.move_set, self.max_depth, 1, 1
       # dopoki sa stany do
       # open("logfile.txt", 'w').close()
       # f = open("logfile.txt", 'w')
        while self.frontier.__len__() > 0:
           # zdejmij stan
            self.state = self.frontier.pop()
           # f.write(self.state.move_set +" " + str(self.state.depth) + '\n')
           # f.write(str(self.state.values) + '\n')
           # f.write(str(self.state.__hash__()) + '\n')
            # sprawdz maks glebokosc
            if self.max_depth < self.state.depth:
                self.max_depth = self.state.depth
                # jesli nie jestesmy za gleboko
            if self.state.depth < self.max_possible_depth:
                self.explored.add(self.state.__hash__())
                neighbour_arr = []
                for direction in self.search_order:
                    if can_move(self.state, direction) and is_not_back_move(self.state, direction):
                        neighbour = generate_new_state(self.state, direction)
                        if self.is_solution(neighbour):
                            self.visited += 1
                        #    f.write("----rozwiazanie!" + '\n')
                        #    f.write("----" + neighbour.move_set + '\n')
                            return neighbour.move_set, self.max_depth, self.visited, self.processed
                        elif neighbour.__hash__() not in self.explored:
                        #    f.write("----nowysasiad!" + '\n')
                        #    f.write("----" + neighbour.move_set + '\n')
                            self.visited += 1
                            neighbour_arr.insert(0,neighbour)
                        #elif neighbour.__hash__() in self.explored:
                        #    f.write("----staaaaarysasiad!" + '\n')
                        #    f.write("----" + neighbour.move_set + '\n')
                        #    f.write(str(neighbour.__hash__()) + '\n')
                self.frontier.extend(neighbour_arr)
                self.processed += 1

       # f.close()




