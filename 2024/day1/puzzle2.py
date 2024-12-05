from sys import stdin

if __name__ == '__main__':
    left = []
    right = []
    for line in stdin:
        if line.strip() == '':
            break
        else:
            vals = line.split('   ')
            left.append(int(vals[0]))
            right.append(int(vals[1]))
    
    total = 0
    for i in left:
        total += i * (right.count(i))
    print(total)