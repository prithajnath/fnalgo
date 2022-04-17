#! /usr/bin/env python3

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def bfs(s):
    from collections import deque

    seen = set()
    q = deque()
    q.append(s)
    node_lookup = {s.val: Node(s.val, [])}
    while q:
        current_node = q.popleft()
        new_current_node = node_lookup[current_node.val]

        seen.add(current_node)
        for neighbor in current_node.neighbors:
            if neighbor.val not in node_lookup:
                new_current_neighbor_node = Node(neighbor.val, [])
                node_lookup[neighbor.val] = new_current_neighbor_node
                print(
                    f"Initializing new node for {new_current_neighbor_node.val} as a new neighbor node"
                )
            else:
                new_current_neighbor_node = node_lookup[neighbor.val]

            if new_current_neighbor_node in new_current_node.neighbors:
                continue

            new_current_node.neighbors.append(new_current_neighbor_node)

            if neighbor in seen:
                continue
            else:
                q.append(neighbor)
    return node_lookup


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return
        tree = bfs(node)
        return tree[1]
