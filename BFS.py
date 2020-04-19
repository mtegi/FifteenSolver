from Search_Algorithm import SearchAlgorithm


class BFS(SearchAlgorithm):
    def find_solution(self):
        if self.is_solution(self.state):
            return self.state.move_set, self.max_depth, 1, 1
        while self.frontier.__len__() > 0:
            self.state = self.frontier.pop()
            self.processed += 1
            for direction in self.search_order:
                if self.state.can_move(direction) and self.is_not_back_move(direction):
                    neighbour = self.state.generate_new_state(direction)
                    if self.is_solution(neighbour):
                        self.visited += 1
                        return neighbour.move_set, len(neighbour.move_set), self.visited, self.processed
                    elif neighbour not in self.explored:
                        self.visited += 1
                        self.frontier.appendleft(neighbour)
            self.explored.append(self.state)
