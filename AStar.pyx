from Search_Algorithm import SearchAlgorithm, can_move, generate_new_state, is_not_back_move
from queue import PriorityQueue

from State cimport State


class AStar(SearchAlgorithm):
    def __init__(self, initial_state, heuristic):
        super().__init__(initial_state, "ludr")
        self.heuristic = heuristic
        self.frontier = PriorityQueue()
        self.frontier.put((0, initial_state))
    def find_solution(self):
        if self.is_solution(self.state):
            return self.state.move_set, self.max_depth, 1, 1
        while not self.frontier.empty():
            self.state = self.frontier.get()[1]
            if self.max_depth < self.state.depth:
                self.max_depth = self.state.depth
            for direction in self.search_order:
                if can_move(self.state, direction) and is_not_back_move(self.state, direction):
                    neighbour = generate_new_state(self.state, direction)
                    if self.is_solution(neighbour):
                        self.visited += 1
                        return neighbour.move_set, self.max_depth, self.visited, self.processed
                    elif neighbour.__hash__() not in self.explored:
                        self.visited += 1
                        distance = get_distance(neighbour, self.heuristic)
                        cost = distance + neighbour.depth
                        self.frontier.put((cost, neighbour))
            self.explored.add(self.state.__hash__())
            self.processed += 1

cdef manhattan(state):
    cdef int distance, x, y
    distance = 0
    for i in range(0, state.width):
        for j in range(0, state.height):
            val = state.values[i, j]
            if val != 0:
                val -= 1
                x = val % state.width
                y = val // state.height
                distance += abs(i - y) + abs(j - x)
    return distance


cdef hamming(state):
    cdef int distance, val
    distance = 0
    for i in range(0, state.width):
        for j in range(0, state.height):
            if i == state.height - 1 and j == state.height - 1:
                val = 0
            else:
                val = i * state.height + j + 1
            if state.values[i, j] != val:
                distance += 1
    return distance

cdef get_distance(State state, str heuristic):
    if heuristic == "manh":
        return manhattan(state)
    else:
        return hamming(state)
