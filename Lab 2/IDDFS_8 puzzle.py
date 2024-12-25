from copy import deepcopy

def index_empty(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

def dfs(initial_state, goal_state, depth, visi):
    if initial_state == goal_state:
        print("Solution Found.")
        return initial_state

    if depth <= 0:
        return None

    i, j = index_empty(initial_state)
    for move in [(1,0),(-1,0),(0,1),(0,-1)]:
        new_state = deepcopy(initial_state)
        new_i, new_j = i + move[0], j + move[1]

        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state[i][j] = new_state[new_i][new_j]
            new_state[new_i][new_j] = 0

            if new_state not in visi:
                visi.append(new_state)
                result = dfs(new_state, goal_state, depth - 1, visi)
                if result:
                    return result
    return None

def iddfs(initial_state, goal_state, max_depth):
    for depth in range(max_depth):
        visited = [initial_state]
        result = dfs(initial_state, goal_state, depth, visited)
        if result:
            return result
    return None

def display_puzzle(puzzle):
    for row in puzzle:
        print(row)
    print()

def main():
    initial = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    max_depth = 20

    result = iddfs(initial, goal, max_depth)
    if result:
        display_puzzle(result)
    else:
        print("No Solution exists")
main()
