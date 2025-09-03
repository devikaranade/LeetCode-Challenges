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
            nn = Node(node.val)
            seen[node]=nn

            for child in node.neighbors:
                nn.neighbors.append(dfs(child))
            return nn
        return dfs(node) if node else None