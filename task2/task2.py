# 1291. Gear-wheels - http://acm.timus.ru/problem.aspx?num=1291

# Strategy:
# From the information given, we already know the number of cogs/second that all gears will be
# spinning at, so all we need to do is run through the graph and figure out the spin directions
# before printing out the final results.

# Performance:
# O(N); runs the tests in 0.001s using 320KB memory.

import sys
from collections import deque

class Gear:
    def __init__(self):
        self.adj = []
        self.cogs = 0
        self.visited = False
        self.parity = False  # направление вращения

def bfs(gear):
    queue = deque([gear])
    gear.visited = True
    while queue:
        curr = queue.popleft()
        for v in curr.adj:
            if not v.visited:
                v.parity = not curr.parity
                v.visited = True
                queue.append(v)


def euclid_algorithm(a, b):
    if b == 0:
        return a
    return euclid_algorithm(b, a % b)

def start():
    gears = [Gear() for _ in range(1001)]
    n = int(sys.stdin.readline())
    for i in range(1, n + 1):
        line = list(map(int, sys.stdin.readline().split()))
        gears[i].cogs = line[0]
        for x in line[1:]:
            if x == 0:
                break
            gears[i].adj.append(gears[x])

    start, v = map(int, sys.stdin.readline().split())
    v *= gears[start].cogs
    if v < 0:
        v = -v
        gears[start].parity = True
    bfs(gears[start])

    for i in range(1, n + 1):
        if not gears[i].visited:
            print("0/1")
        else:
            g = euclid_algorithm(gears[i].cogs, v)
            print(("" if not gears[i].parity else "-") + str(v // g) + "/" + str(gears[i].cogs // g))

if __name__ == "__main__":
    start()

