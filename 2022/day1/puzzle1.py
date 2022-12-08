from sys import stdin

if __name__=="__main__":
    current = 0
    highest = 0
    for line in stdin:
        stripped = line.strip()
        if len(stripped) > 0:
            val = int(stripped)
            current += val
        else:
            highest = max(highest, current)
            current = 0
    
    print(highest)