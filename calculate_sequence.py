import sys
import networkx as nx
from random import shuffle
import time

perfectSquares = set()

def hamPathRec(G, path, pos, randomize):
    assert(type(G) == nx.Graph)
    
    # base case
    if pos == G.number_of_nodes():
        print(G.number_of_nodes(), path)
        return True

    N = list(G.nodes())
    if randomize:
        shuffle(N)
    for v in N:
        if v not in path:
            if len(path) == 0 or G.has_edge(path[-1],v):
                path.append(v)

                if hamPathRec(G, path, pos+1, randomize) == True:
                    return True

                path.remove(v)

    return False

def is_square(a):
    assert(a > 0)
    x = a // 2
    seen = set([x])
    while x * x != a:
        x = (x + (a // x)) // 2
        if x in seen: return False
        seen.add(x) #memoization
    return True

def isSumToPerfectSquare(a, b):
    if (a+b) in perfectSquares:
        return True
    elif is_square(a+b):
        perfectSquares.add(a+b)
        return True
    else:
        return False

def main():
    end = int(sys.argv[1])
    randomize = int(sys.argv[2])

    hasHamiltonianPath = set()

    G = nx.Graph()
    for i in range(1,end+1):
        G.add_node(i)
        for node in G.nodes():
            if isSumToPerfectSquare(i,node):
                G.add_edge(i,node)

        start = time.time()
        if hamPathRec(G.copy(), [], 0, randomize):
            hasHamiltonianPath.add(i)
            print("%d: %.2f Seconds" % (i, (time.time() - start) ))

    for i in range(1, end+1):
        if i in hasHamiltonianPath:
            print("%d: Yes" %i)
        else:
            print("%d: No" %i )



        



if __name__ == '__main__':
    main()