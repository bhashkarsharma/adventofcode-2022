from sys import stdin

if __name__=="__main__":
    current = 0
    highest = [0, 0, 0, 0]
    for line in stdin:
        stripped = line.strip()
        if len(stripped) > 0:
            val = int(stripped)
            current += val
        else:
            highest[0] = current
            current = 0
            highest = sorted(highest)
    
    print(sum(highest[1:]))