# f1 = open('.gitignore', 'r')
f1=open('erofflps.txt', 'r')
x = f1.read()
f2 = open('output_t3.txt', 'w')
y = x.split(' ')
y.sort()

# for index, el in enumerate(y):
#     count = 1
#     if el == y [index -1]:
#         count += 1
#     print(y.pop(index), count, file=f2, sep='\n')
for el in y:
    print(el, ' ', x.count(el), ' \n', file=f2)

f1.close()
f2.close()