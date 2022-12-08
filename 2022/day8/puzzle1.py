from sys import stdin

def checkIfVisible(trees, x, y):
    rowlen = len(trees[0])
    treelen = len(trees)
    if x == 0 or y == 0 or x == rowlen - 1 or y == treelen - 1:
        return True
    
    val = trees[x][y]
    t1 = all([val > trees[i][y] for i in range(x)])
    t2 = all([val > trees[i][y] for i in range(x+1, rowlen)])
    t3 = all([val > trees[x][i] for i in range(y)])
    t4 = all([val > trees[x][i] for i in range(y+1, treelen)])
    return [t1, t2, t3, t4].count(True) > 0
    

if __name__=="__main__":
    trees = []
    for line in stdin:
        items = map(int, list(line.strip()))
        trees.append(list(items))
    
    res = [[checkIfVisible(trees, ix, iy) for ix, x in enumerate(y)] for iy, y in enumerate(trees)]
    
    print(sum(l.count(True) for l in res))