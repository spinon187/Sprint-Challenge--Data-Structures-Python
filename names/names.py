import time
from bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
l_o = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}

# bst = BinarySearchTree(names_1[0], l_o[names_1[0][0]])

# for i in range(1, len(names_1)):
#     bst.insert(names_1[i], l_o[names_1[i][0]])

# for i in names_2:
#     if bst.contains(names_2[i], l_o[names_2[i][0]]):
#         duplicates.append(i)

names_2.sort()

def midpoint(x):
    return l_o[x[len(x) // 2][0]]


def check(val, r):
    if l_o[val[0]] < midpoint(r):
        return check(val, r[:len(r)//2])
    elif l_o[val[0]] > midpoint(r):
        check(val, r[len(r)//2:])
    elif l_o[val[0]] == midpoint(r):
        for i in r[len(r)//2:]:
            if i == val:
                duplicates.append(i)


for i in names_1:
    check(i, names_2)




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

