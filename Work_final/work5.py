def maze_solver_with_conveyors(maze):
    rows = len(maze)
    cols = len(maze[0])

    start = end = None
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    if start is None or end is None:
        return {"distance": -1, "path": []}

    moves = [(0,1),(0,-1),(1,0),(-1,0)]
    conveyors = {">":(0,1), "<":(0,-1), "^":(-1,0), "v":(1,0)}

    def follow(r, c):
        path = [(r, c)]
        seen = set()
        while 0 <= r < rows and 0 <= c < cols and maze[r][c] in conveyors:
            if (r, c) in seen:
                return None
            seen.add((r, c))
            dr, dc = conveyors[maze[r][c]]
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols):
                return None
            if maze[nr][nc] == "#":
                return None
            r, c = nr, nc
            path.append((r, c))
            if (r, c) == end:
                break
        return path

    queue = [(start[0], start[1], 0, [[start[0], start[1]]])]
    visited = set([start])

    while queue:
        r, c, d, path = queue.pop(0)

        if (r, c) == end:
            return {"distance": d, "path": path}

        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if maze[nr][nc] == "#":
                continue

            if maze[nr][nc] in conveyors:
                sp = follow(nr, nc)
                if sp is None:
                    continue
                last = sp[-1]
                if last not in visited:
                    visited.add(last)
                    new_path = path + [[x, y] for (x, y) in sp]
                    queue.append((last[0], last[1], d + 1, new_path))
            else:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, d + 1, path + [[nr, nc]]))

    return {"distance": -1, "path": []}


if __name__ == "__main__":
    maze1 = [
        ['S', '.', '>', '>', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    print(maze_solver_with_conveyors(maze1))

    maze2 = [
        ['S', '.', '>', '#', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    print(maze_solver_with_conveyors(maze2))

    maze3 = [
        ['S', '.', 'v', '.', 'E'],
        ['#', '#', 'v', '.', '#'],
        ['.', '.', 'v', '.', '.'],
        ['#', '#', '.', '.', '#'],
        ['.', '.', '.', '.', '.']
    ]
    print(maze_solver_with_conveyors(maze3))
