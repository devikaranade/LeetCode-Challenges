"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}
        def dfs(node):
            if node in seen:
                return seen[node]
            clone = Node(node.val)
            seen[node] = clone

            for child in node.neighbors:
                clone.neighbors.append(dfs(child))
            return clone
        return dfs(node) if node else None


        