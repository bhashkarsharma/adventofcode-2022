from sys import stdin

if __name__ == '__main__':
    safe = 0
    for line in stdin:
        if line.strip() == '':
            break
        rep = [int(i) for i in line.strip().split(' ')]
        
        if rep == sorted(rep):
            diffs = [b - a for a, b in zip(rep, rep[1:])]
            if all(diff <= 3 and diff >=1 for diff in diffs):
                safe += 1
            
        if rep == sorted(rep, reverse=True):
            diffs = [a - b for a, b in zip(rep, rep[1:])]
            if all(diff <= 3 and diff >=1 for diff in diffs):
                safe += 1

    print(safe)