#https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

list = [2, 3, 4, 6, 7, 8, 9, 88, 48, 56, 22]
a = []
for b in list:
    if b <= 5:
        a.append(b)
print(f'list are {a}')
print(f'In one line {[c for c in list if c < 5]}')

newlist = []

num = int(input('Enter a number: '))
for b in list:
    if b < num:
        newlist.append(b)
print(f'Number less than {num} in list are {newlist}')
        



