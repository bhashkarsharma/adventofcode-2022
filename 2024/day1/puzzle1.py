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
    left.sort()
    right.sort()

    total = 0

    for i in range(len(left)):
        total += abs(left[i] - right[i])

    print(total)