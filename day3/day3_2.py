lines = []
sum_of_priorities = 0

def setPriority(letter):
    if ord('a') <= ord(letter) <= ord('z'):
        return ord(letter)-ord('a')+1
    return ord(letter)-ord('A')+27

def firstSharedLetter(str1, str2, str3):
    for i in range(len(str1)):
        for j in range(len(str2)):
            for k in range(len(str3)):
                if str1[i] == str2[j] and str2[j] == str3[k]:
                    return str1[i]

f = open('data.txt', 'r')
for line in f:
    lines.append(line[0:-1])
    if len(lines) == 3:
        sum_of_priorities += setPriority(firstSharedLetter(lines[0], lines[1], lines[2]))
        lines.clear()

f.close()

print(f'Sum of priorities = {sum_of_priorities}.')