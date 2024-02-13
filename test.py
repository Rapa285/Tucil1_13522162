import numpy as np
import random

def generate_matrix(token,row,col):
    matrix = []
    for i in range(row):
        r = random.choices(token,k=col)
        matrix.append(r)
    return matrix

token = ["AA","BB","CC","DD","EE"]
row = 2
col = 2

matrix = generate_matrix(token,row,col)
print(matrix)

m = [["DD"]]
print(len(m))
print(len(m[0]))
print(m[0][0])