from sys import stdin

def is_safe(report):
    if report == sorted(report):
        diffs = [b - a for a, b in zip(report, report[1:])]
        if all(1 <= diff <= 3 for diff in diffs):
            return True
    
    if report == sorted(report, reverse=True):
        diffs = [a - b for a, b in zip(report, report[1:])]
        if all(1 <= diff <= 3 for diff in diffs):
            return True
    
    return False

if __name__ == '__main__':
    safe = 0
    for line in stdin:
        if line.strip() == '':
            break
        rep = [int(i) for i in line.strip().split(' ')]
        
        if is_safe(rep):
            safe += 1
            continue

        for i in range(len(rep)):
            modified_rep = rep[:i]  + rep[i+1:]
            if is_safe(modified_rep):
                safe += 1
                break

    print(safe)