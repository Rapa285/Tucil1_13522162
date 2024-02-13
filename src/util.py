import numpy as np

def isSubset(seq,array): # mencari apakah seq adalah subset dari array
    found = False
    i = 0
    k = 0
    while (found == False and i < len(array)): 
        if (seq[k] == array[i] and found == False):
            k+=1
            i+=1
        else:
            i+=1
            k = 0
        if (k == len(seq)):
            found = True
    return found

def isOdd(x):
    if x%2 == 1:
        return True
    else:
        return False

def is_unique(array):
    a = np.unique(array)
    if len(array) == len(a):
        return True
    else:
        return False
    
def idx_to_digit(col,a,b): 
    d = a*col + b
    return d

def dig_to_idx(d,col):
    y = d//col
    x = d%col
    return x,y

def clear_file(file):
    f = open(file,"w")
    f.write("")
    f.close()

