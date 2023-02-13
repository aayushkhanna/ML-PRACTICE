#1
X = [[12,7,3],[4,5,6],[7,8,9]]
Y = [[5,8,1],[6,7,3],[4,5,9]]
result =[[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)

#2
X = [[12,7,3],[4,5,6],[7,8,9]]
Y = [[5,8,1],[6,7,3],[4,5,9]]
result =[[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(X)):
   for j in range(len(X[0])):
        result[i][j] = X[i][j] - Y[i][j]

for r in result:
    print(r)

 #3
X = [[12,7],[4,5]]
Y = [[5,8],[6,7]]
k = [[0,0],[0,0]]
result =[[0,0],
         [0,0]]
for i in range(len(X)):
   for j in range(len(X[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)

#4
A = [[1,2,3,4],
     [1,2,3,4]]
c = [[0,0],[0,0],[0,0],[0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        c[j][i] = A[i][j]

for r in c:
    print(r)

#5
R = int(input("Enter no. of rows in first matrix"))
C = int(input("Enter no. of columns in first matrix"))
M =[[0 for i in range(C)] for j in range(R)]
print("All Zeroe matrix:")
for k in range(R):
    for x in range(C):
        print(M[k][x],end=" ")
    print()

#6
R = int(input("Enter no. of rows in first matrix"))
C = int(input("Enter no. of columns in first matrix"))
M =[[1 for i in range(C)] for j in range(R)]
print("All One's matrix:")
for k in range(R):
    for x in range(C):
        print(M[k][x],end=" ")
    print()

#7
def sum_diagnol():
    sum = 0
    import random
    r1=int(input("row"))
    c1=int(input("col"))
    a=[[random.random()for col in range(c1)]for row in range(r1)]
    print("enter elements")
    for i in range(r1):
        for j in range(c1):
            a[i][j]=int(input("enter elements"))
    r2=int(input("row"))
    c2=int(input("col"))
    b=[[random.random()for col in range(c2)]for row in range(r2)]
    print("enter elements")
    for i in range(r2):
        for j in range(c2):
            b[i][j]=int(input("enter elements"))
    c=[[random.random()for col in range(c2)]for row in range(r1)]
    if(c1==r2):
        for i in range(r1):
            for j in range(c2):
                c[i][j]=0
                for k in range(c2):
                    c[i][j]=a[j][k]*b[k][j]
    else:
        print("multiplication not possible")
    for i in range(r1):
        for j in range(c2):
           print(c[i][j],end=" ")
        print()
sum_diagnol()
