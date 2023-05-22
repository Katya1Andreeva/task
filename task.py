import sys


def path():
    M, N, S = map(int, input().split())

    nodes = {}
    for i in range(1, M + 1):
        nodes[i] = []

    visited_nodes = [True for _ in range(M+1)]

    for _ in range(N):
        P, Q, R = map(int, input().split())
        nodes[P].append((Q, R))
        nodes[Q].append((P, R))

    for i in range(1, M+1):
        if visited_nodes[i]:
            p = dfs(i, nodes, None, visited_nodes)
            if p[1] >= S:
                print("YES")
                sys.exit()

    print("NO")


def dfs(i, nodes, parent, visited_nodes):

    max_value, second_max_value, total_maximum = 0, 0, 0
    for neighbour in nodes[i]:
        if neighbour[0] == parent:
            continue
        if not visited_nodes[neighbour[0]]:
            return 1000000, 1000000
        visited_nodes[neighbour[0]] = False
        distance = dfs(neighbour[0], nodes, i, visited_nodes)

        current_node_distance = distance[0] + neighbour[1]
        if distance[1] > total_maximum:
            total_maximum = distance[1]
        if current_node_distance > max_value:
            second_max_value = max_value
            max_value = current_node_distance
        elif current_node_distance > second_max_value:
            second_max_value = current_node_distance

    if max_value + second_max_value > total_maximum:
        return max_value, max_value + second_max_value
    else:
        return max_value, total_maximum


if __name__ == "__main__":
    path()