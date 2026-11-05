import argparse

def counter(lines, pos):
    a = 0
    t = 0
    g = 0
    c = 0
    for i in range(len(lines)):
        line = lines[i] 
        if line[pos] in 'A':
            a += 1
        if line[pos] in 'T':
            t += 1
        if line[pos] in 'G':
            g += 1            
        else:
            c += 1
    return list(a, t, g, c)

with open() as f:
    for line in f:
        if line.startswith('>')