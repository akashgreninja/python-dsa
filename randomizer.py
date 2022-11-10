
import random

list1 = [1, 2, 3, 4, 5, 6, 7, 8]

listz = []
asa = True
while asa:
    v = random.choice(list1)
    if v not in listz:
        listz.append(v)
    if len(listz) != len(list1):
        asa = True
    else:
        asa = False

groups = 3
print(listz)
iter = 0
tex = []
for i in listz:
    tex.append(i)
    iter += 1
    if iter % 3 == 0:
        print(tex)
        tex = []

final = []

for i in listz:
    if i in tex:
        final.append(i)


print(final)


