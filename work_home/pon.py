def maze_solver_with_conveyors(maze: list[list[str]]) -> dict:
    R, C = len(maze), len(maze[0])

    # หาตำแหน่ง S และ E
    start = end = None
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)
    if not start or not end:
        return {"distance": -1, "path": []}

    # ทิศทางการเคลื่อน
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    conveyor_dir = {'^': (-1,0), 'v': (1,0), '<': (0,-1), '>': (0,1)}

    # ฟังก์ชันจำลองการเลื่อนสายพาน
    def slide(r, c):
        path = [(r,c)]
        while True:
            if maze[r][c] not in conveyor_dir:
                return (r, c), path
            dr, dc = conveyor_dir[maze[r][c]]
            nr, nc = r+dr, c+dc
            if not (0 <= nr < R and 0 <= nc < C):
                return None, []
            if maze[nr][nc] == '#':
                return None, []
            r, c = nr, nc
            path.append((r,c))

    # ใช้ list เป็นคิว
    queue = [start]
    dist = {start: 0}
    parent = {start: None}
    head = 0  # ชี้ index ปัจจุบันใน queue

    while head < len(queue):
        r, c = queue[head]
        head += 1
        if (r, c) == end:
            break
        for dr, dc in moves:
            nr, nc = r+dr, c+dc
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if maze[nr][nc] == '#':
                continue

            cost = 1
            final = (nr, nc)

            # ถ้าเป็นสายพาน → จำลองเลื่อน
            if maze[nr][nc] in conveyor_dir:
                slide_end, slide_path = slide(nr, nc)
                if slide_end is None:
                    continue
                final = slide_end

            new_dist = dist[(r, c)] + cost
            if final not in dist or new_dist < dist[final]:
                dist[final] = new_dist
                parent[final] = (r, c)
                queue.append(final)

    if end not in dist:
        return {"distance": -1, "path": []}

    # reconstruct path
    path = []
    cur = end
    while cur is not None:
        path.append(list(cur))
        cur = parent[cur]
    path.reverse()

    return {"distance": dist[end], "path": path}


if _name_ == "_main_":
    maze = [
        ['S', '.', '>', '>', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    print(maze_solver_with_conveyors(maze))
    # {'distance': 2, 'path': [[0,0],[0,1],[0,2],[0,3],[0,4]]}

    maze = [
        ['S', '.', '>', '#', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    print(maze_solver_with_conveyors(maze))
    # {"distance": -1, "path": []}

    maze = [
        ['S', '.', 'v', '.', 'E'],
        ['#', '#', 'v', '.', '#'],
        ['.', '.', 'v', '.', '.'],
        ['#', '#', '.', '.', '#'],
        ['.', '.', '.', '.', '.']
    ]
    print(maze_solver_with_conveyors(maze))
    # {'distance': 7, 'path': [[0,0],[0,1],[0,2],[1,2],[2,2],[3,2],[3,3],[2,3],[1,3],[0,3],[0,4]]}