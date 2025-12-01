import argparse
import heapq
import os
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import cache
from pprint import pprint
from typing import List, Set, Tuple

current_dir = os.path.dirname(os.path.abspath(__file__))

log = True
ansprint = print
if log:
    print = print
    pprint = pprint
else:
    print = lambda *x: None
    pprint = print
    
def pprint2d(arr):
    for x in arr:
        row = []
        for l in x:
            row.append(l)
        print("".join(map(str, row)))
        
        
def parse_args():
    parser = argparse.ArgumentParser(description="Process a file.")
    
    parser.add_argument("-f", "--file",
                        default=f"{current_dir}/dummy_inp.txt",
                        type=argparse.FileType("r"),
                        help="Path to the input file.")
    
    args = parser.parse_args()
    
    content = [x.strip() for x in args.file.readlines()]
    args.file.close()
    return content

def format_lines(lines: List[str]) -> List[Tuple[str, str]]:
    return [tuple(x.split('-')) for x in lines]
        

def load_file() -> List[List[str]]:
    lines = format_lines(parse_args())
    return lines


def A(lines: List[Tuple[str, str]]) -> None:
    nodes = set()
    adjacency_matrix = defaultdict(set)

    for (a, b) in lines:
        nodes.add(a)
        nodes.add(b)
        adjacency_matrix[a].add(b)
        adjacency_matrix[b].add(a)
    
    pprint(len(nodes))
    # pprint(adjacency_matrix)

    triplet_pairs = set()
    for node in nodes: # aq
        for neighbour1 in adjacency_matrix[node]: # {'yn', 'cg' |, 'vc', 'wq'}
            for neighbour2 in adjacency_matrix[neighbour1]: # {'tb', 'aq', 'yn' | , 'de'}
                # if neighbour2 == node:
                #     continue
                if node in adjacency_matrix[neighbour2]:
                    triplet_pairs.add(tuple(sorted([node, neighbour1, neighbour2])))
                
    # pprint(triplet_pairs)
    
    ansprint(sum([1 for trip in triplet_pairs if any([x.startswith('t') for x in trip])]))

def B(lines) -> None:
    nodes = set()
    adjacency_matrix = defaultdict(set)

    for (a, b) in lines:
        nodes.add(a)
        nodes.add(b)
        adjacency_matrix[a].add(b)
        adjacency_matrix[b].add(a)
    
    cliques = bron_kerbosch_cliques(adjacency_matrix)
    
    # pprint(cliques)
    max_cliq = max(cliques, key=lambda x: len(x))
    ansprint()
    ansprint(",".join(sorted(max_cliq)))
    
def bron_kerbosch_cliques(graph):
    """
    Finds all maximal cliques in the given graph using the Bron–Kerbosch algorithm.
    """
    cliques = []
    # All vertices
    vertices = set(graph.keys())
    # at start R = {}, P = all vertices, X = {}
    bron_kerbosch(set(), vertices, set(), graph, cliques)
    return cliques

def bron_kerbosch(R, P, X, graph, cliques):
    if not P and not X:
        # Found a maximal clique
        cliques.append(R)
        return

    # pivot
    if P or X:
        u = next(iter(P.union(X)))

        # vertices in P \ neighbors(u)
        for v in P.difference(graph[u]):
            R_v = R.union({v})
            P_v = P.intersection(graph[v])
            X_v = X.intersection(graph[v])

            bron_kerbosch(R_v, P_v, X_v, graph, cliques)

            P.remove(v)
            X.add(v)

if __name__ == "__main__":
    nums = load_file()
    B(nums)



