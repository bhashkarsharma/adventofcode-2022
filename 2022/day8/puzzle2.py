from functools import reduce
from sys import stdin

def getScenicScore(trees, x, y):
    rowlen = len(trees[0])
    treelen = len(trees)
    if x == 0 or y == 0 or x == rowlen - 1 or y == treelen - 1:
        return 0
    
    val = trees[x][y]
    t1 = [val > trees[i][y] for i in range(x-1, -1, -1)]
    t2 = [val > trees[i][y] for i in range(x+1, rowlen)]
    t3 = [val > trees[x][i] for i in range(y-1, -1, -1)]
    t4 = [val > trees[x][i] for i in range(y+1, treelen)]
    arr = [t1, t2, t3, t4]
    res = list(map(lambda x : x.index(False) + 1 if False in x else len(x), arr))
    return reduce(lambda x, y: x*y, res)

if __name__=="__main__":
    trees = []
    for line in stdin:
        items = map(int, list(line.strip()))
        trees.append(list(items))
    
    res = [[getScenicScore(trees, ix, iy) for ix, x in enumerate(y)] for iy, y in enumerate(trees)]
    print(max(max(l) for l in res))