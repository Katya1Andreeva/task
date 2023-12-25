from collections import deque


class Node:
    def __init__(self, id):
        self.edges = []
        self.depth = 0
        self.id = id
        self.visited = False


nodes = [Node(i) for i in range(51)]
ans = [0] * 51


def makeComponent(start):
    ret = []
    s = deque()
    s.append(start)
    start.visited = True
    while s:
        n = s.popleft()
        ret.append(n)
        for v in n.edges:
            if not v.visited:
                v.visited = True
                s.append(v)
    return ret


def test(start):
    for i in range(51):
        nodes[i].visited = False
    s = deque()
    s.append(start)
    start.visited = True
    max_depth = 0
    start.depth = 1
    while s:
        n = s.popleft()
        for v in n.edges:
            if not v.visited:
                v.visited = True
                v.depth = n.depth + 1
                max_depth = max(n.depth + 1, max_depth)
                s.append(v)
            elif abs(v.depth - n.depth) != 1:
                return -1
    return max_depth


def assign(start, dir):
    for i in range(51):
        nodes[i].visited = False
    s = deque()
    s.append(start)
    start.depth = 1 if dir > 0 else 50
    start.visited = True
    while s:
        n = s.popleft()
        ans[n.id] = n.depth
        for v in n.edges:
            if not v.visited:
                v.depth = n.depth + dir
                v.visited = True
                s.append(v)


def algoritm():
    n, p = map(int, input().split())
    ansmax = -1
    components = []

    for i in range(p + 1):
        nodes[i].id = i

    for _ in range(n):
        x, y = map(int, input().split())
        nodes[x].edges.append(nodes[y])
        nodes[y].edges.append(nodes[x])

    for i in range(1, p + 1):
        if not nodes[i].visited:
            components.append(makeComponent(nodes[i]))

    for comp in components:
        max_depth = -1
        for node in comp:
            result = test(node)
            if result > max_depth:
                assign(node, -1 if ansmax >= 0 else 1)
                max_depth = result
        if max_depth < 0:
            print("-1")
            return
        else:
            ansmax = max_depth

    min_depth, max_depth = 50, 0
    for i in range(1, p + 1):
        min_depth = min(min_depth, ans[i])
        max_depth = max(max_depth, ans[i])

    print(max_depth - min_depth)
    for i in range(1, p + 1):
        print(ans[i], end=" ")


if __name__ == '__main__':
    algoritm()
