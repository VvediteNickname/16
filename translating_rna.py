import argparse

text = '''
UUU F CUU L AUU I GUU V
UUC F CUC L AUC I GUC V
UUA L CUA L AUA I GUA V
UUG L CUG L AUG M GUG V
UCU S CCU P ACU T GCU A
UCC S CCC P ACC T GCC A
UCA S CCA P ACA T GCA A
UCG S CCG P ACG T GCG A
UAU Y CAU H AAU N GAU D
UAC Y CAC H AAC N GAC D
UAA Stop CAA Q AAA K GAA E
UAG Stop CAG Q AAG K GAG E
UGU C CGU R AGU S GGU G
UGC C CGC R AGC S GGC G
UGA Stop CGA R AGA R GGA G
UGG W CGG R AGG R GGG G
'''

parser = argparse.ArgumentParser(description = "Перевод нуклеотидной последовательности в белковую.")
parser.add_argument('-i','--input', help = "Файл с последовательностью РНК", required = True, type = str)
parser.add_argument('-o','--output', help = "Путь к выходному файлу", required = True, type = str)
args = parser.parse_args()

text = text.split()
codon_table = dict(zip(text[::2], text[1::2]))

ans = ''

with open(args.input) as f: 
    s = f.read().strip()
    for i in range(int(len(s)/3)):
        if codon_table[s[:3]] == 'Stop':
            break
        else:
            ans = ans + codon_table[s[:3]]
            s = s[3:]
    
with open (args.output, 'w') as f:
    f.write(ans)