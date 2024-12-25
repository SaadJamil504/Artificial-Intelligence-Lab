from copy import deepcopy
from collections import deque
def index_empty(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

def bfs(init_st, goal_st):
    queue = deque([(init_st,[])])
    visi = [init_st]
    moves = [(1,0),(-1,0),(0,1),(0,-1)]

    while queue:
        current_st, path = queue.popleft()
        if current_st == goal_st:
            print("Solution Found.")
            return current_st
        i, j = index_empty(current_st)
        for move in moves:
            new_state = deepcopy(current_st)
            new_i, new_j = i + move[0], j + move[1]
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state[i][j] = new_state[new_i][new_j]
                new_state[new_i][new_j] = 0
                if new_state not in visi:
                    visi.append(new_state)
                    queue.append((new_state, path + [new_state]))
    return None

def display_puzzle(puzzle):
    for row in puzzle:
        print(row)
    print()

def main():
    init= [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    out = bfs(init, goal)
    if out:
        display_puzzle(out)
    else:
        print("No Solution exists")

main()
