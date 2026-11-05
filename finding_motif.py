import argparse

parser = argparse.ArgumentParser(description = "Позиции начала мотива в нуклеотидной последовательности.")
parser.add_argument('-i','--input', help = "Путь к файлу с последовательностью и мотивом", required = True, type = str)
parser.add_argument('-o','--output', help = "Путь к выходному файлу", required = True, type = str)
args = parser.parse_args()

with open(args.input) as f:
    lines = f.readlines()
    s = lines[0].strip()
    t = lines[1].strip()
    pos = []
    start = 0
    while True:
        i = s.find(t, start)
        if i == -1:
            break
        pos.append(i + 1)
        start = i + 1

with open (args.output, 'w') as f:
    ans = ' '.join(map(str, pos))
    f.write(ans)