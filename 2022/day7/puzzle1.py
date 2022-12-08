from sys import stdin

cwd = []
filetree = {}
sums = []

def handleCommand(cmd, arg):
    if cmd == "cd":
        if arg == '..':
            cwd.pop()
        else:
            cwd.append(arg)

def handleOutput(x, y):
    if x.isdigit(): # size
        updateTree(y, x)
    else:
        if x == 'dir': # dir
            updateTree(y)

def updateTree(name, size=None):
    curr = filetree
    for d in cwd:
        if d in curr:
            curr = curr[d]
    
    curr[name] = int(size) if size else {}

def processLine(line):
    tokens = line.split(' ')
    if tokens[0] == '$': # is command
        cmd = tokens[1]
        arg = tokens[2] if len(tokens) > 2 else None
        handleCommand(cmd, arg)
    else: # is output
        x, y = tokens
        handleOutput(x, y)

def processTree(tree):
    output = {}
    treeitems = tree.items()
    s = 0
    for k, v in treeitems:
        if isinstance(v, dict):
            output[k], innerS = processTree(v)
            s += innerS
        else:
            output['sum'] = output.get('sum', 0) + v
    output['sum'] = output.get('sum', 0) + s
    sums.append(output['sum'])

    return (output, output['sum'])


if __name__=="__main__":
    for line in stdin:
        processLine(line.strip())

    processTree(filetree)
    print(sum(filter(lambda x : x <= 100000, sums)))