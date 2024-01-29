word_input = str(input())
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia:
    word_input = word_input.replace(i, 'x')

print(len(word_input))