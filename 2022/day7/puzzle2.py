from sys import stdin
import json

total_space = 70000000
needed_space = 30000000

cwd = []
filetree = {}
sums = []

def handleCommand(cmd, arg):
    if cmd == "cd":
        if arg == '..':
            cwd.pop()
        else:
            cwd.append(arg)
    # print(cwd)

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
    available_space = total_space - sums[-1]
    more_needed = needed_space - available_space
    for s in sorted(sums):
        if s >= more_needed:
            print(s)
            break