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

l_o = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}

big = {'A':[],'B':[],'C':[],'D':[],'E':[],'F':[],'G':[],'H':[],'I':[],'J':[],'K':[],'L':[],'M':[],'N':[],'O':[],'P':[],'Q':[],'R':[],'S':[],'T':[],'U':[],'V':[],'W':[],'X':[],'Y':[],'Z':[]}

for i in names_1:
    big[i[0]].append(i)

for i1 in names_2:
    for i2 in big[i1[0]]:
        if i1 == i2:
            duplicates.append(i1)

# def midpoint(x):
#     return l_o[x[len(x) // 2][0]]

# def check(val, r):
#     if l_o[val[0]] < midpoint(r):
#         return check(val, r[:len(r)//2])
#     elif l_o[val[0]] > midpoint(r):
#         check(val, r[len(r)//2:])
#     elif l_o[val[0]] == midpoint(r):
#         for i in r[len(r)//2:]:
#             if i == val:
#                 duplicates.append(i)


# for i in names_1:
#     check(i, names_2)




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# original alphabetized
# Abel Newman,Addison Clarke,Ahmad Watts,Aleah Valentine,Ali Collier,Alvaro Robbins,Amiah Hobbs,Andre Carrillo,Ashlee Randall,Aydan Calderon,Camryn Doyle,Carley Gallegos,Carsen Tyler,Clay Wilkinson,Cloe Norris,Daphne Hamilton,Dashawn Green,Davion Arias,Devyn Aguirre,Diego Chaney,Dulce Hines,Eden Howe,Franklin Cooper,Giancarlo Warren,Grace Bridges,Hallie Vazquez,Hayley Morgan,Irvin Krause,Jaden Hawkins,Jadyn Mays,Jaydin Sawyer,Jordin Schneider,Josie Cole,Josie Dawson,Justine Soto,Kale Sawyer,Kameron Osborne,Leia Foley,Lennon Hunt,Leon Cochran,Logan Morrow,Luciana Ford,Malcolm Nelson,Malcolm Tucker,Maliyah Serrano,Marisol Morris,Marley Rivers,Megan Porter,Nathalie Little,Nelson Acevedo,Pablo Berg,Peyton Lloyd,Piper Hamilton,Ralph Roth,Raven Christensen,River Johnson,Salma Meza,Sanai Harrison,Selah Hansen,Trace Gates,Victoria Roach,William Maldonado,Winston Austin,Zara Suarez

# optimized alphabetized
# Abel Newman,Addison Clarke,Ahmad Watts,Aleah Valentine,Ali Collier,Alvaro Robbins,Amiah Hobbs,Andre Carrillo,Ashlee Randall,Aydan Calderon,Camryn Doyle,Carley Gallegos,Carsen Tyler,Clay Wilkinson,Cloe Norris,Daphne Hamilton,Dashawn Green,Davion Arias,Devyn Aguirre,Diego Chaney,Dulce Hines,Eden Howe,Franklin Cooper,Giancarlo Warren,Grace Bridges,Hallie Vazquez,Hayley Morgan,Irvin Krause,Jaden Hawkins,Jadyn Mays,Jaydin Sawyer,Jordin Schneider,Josie Cole,Josie Dawson,Justine Soto,Kale Sawyer,Kameron Osborne,Leia Foley,Lennon Hunt,Leon Cochran,Logan Morrow,Luciana Ford,Malcolm Nelson,Malcolm Tucker,Maliyah Serrano,Marisol Morris,Marley Rivers,Megan Porter,Nathalie Little,Nelson Acevedo,Pablo Berg,Peyton Lloyd,Piper Hamilton,Ralph Roth,Raven Christensen,River Johnson,Salma Meza,Sanai Harrison,Selah Hansen,Trace Gates,Victoria Roach,William Maldonado,Winston Austin,Zara Suarez