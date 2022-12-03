line_len_split = 0
sum_of_priorities = 0

def setPriority(letter):
    if ord('a') <= ord(letter) <= ord('z'):
        return ord(letter)-ord('a')+1
    return ord(letter)-ord('A')+27

def firstSharedLetter(str1, str2):
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                return str1[i]

f = open('data.txt', 'r')
for line in f:
    line_len_split = len(line) // 2
    sum_of_priorities += setPriority(firstSharedLetter(line[0:line_len_split], line[line_len_split:]))

f.close()

print(f'Sum of priorities = {sum_of_priorities}.')