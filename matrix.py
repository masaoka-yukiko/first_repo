def create_matrix (A, B):
    k=int(input()) #размерности матрицы А
    m=int(input()) #размерности матрицы А
    a=int(input()) #размерности матрицы Б
    b=int(input()) #размерности матрицы Б
    n=input ('Would you like to fill the matrix yourself or use randomizer to fill it? Print 1 if you want to to do it yourself, 0 if you want to have it done randomly', ())
    for i in range (k):
        A.append([0]*m)
    import random
    for i in range (k):
        for j in range (m):
            if n==1:
                A[i][j]=int(input())
            elif n==0:
                A[i][j]=randint (1,100)
            elif n!=1 and n!=0:
                print ('Please choose the way of filling the matrix correctly and start again')
                return False
    for i in range (a):
        for j in range (b):
            if n==1:
                A[i][j]=int(input())
            elif n==0:
                a[i][j]=randint(1,100)
    if k==b:
        return True
    else:
        return False
        
   
def multiply_matrix(A, B):
    import numpy as np
    C=A.dot(B)
    return C
def main_program():
    A=[]
    B=[]
    x=create_matrix(A,B)
    if x==1:
        y=multiply_matrix(A,B)
        print (y)
    elif x==0:
        main_program()

main_program()
    
    
    