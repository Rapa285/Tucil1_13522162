from src.util import *
import time

def get_cords_token(matrix,Initial_point,movement_sequence):
    current_row = 0
    current_col = Initial_point
    cord = idx_to_digit(len(matrix[0]),current_row,current_col)
    cords = [cord]
    token = str(matrix[current_row][current_col])
    for i in range (len(movement_sequence)):
        if isOdd(i):
            current_col = (current_col + movement_sequence[i])%len(matrix[0])
        else:
            current_row = (current_row + movement_sequence[i])%len(matrix)
        token += " " + str(matrix[current_row][current_col])
        cord = idx_to_digit(len(matrix[0]),current_row,current_col)
        cords.append(cord)
    return cords,token

def get_token_value(token,seq,seq_reward):
    value = 0
    for i in range (len(seq)):
        print(seq[i])
        print(seq_reward[i])
        if(isSubset(seq[i],token)):
            value += seq_reward[i]
    print(value)
    

def get_max_reward(seq_reward):
    total = 0
    for i in range(0, len(seq_reward)):
        if seq_reward[i] > 0:
            total += seq_reward[i]
    return total

def next_move_seq(mov_seq,row,col,id):
    if isOdd(id):
        max = col-1
    else:
        max = row-1
    
    if mov_seq[id] == max and id != 0:
        next_move_seq(mov_seq,row,col,id-1)
        mov_seq[id] = 1
    else:
        mov_seq[id] +=1
    return mov_seq

def mov_seq(buffer_size,row,col):
    ms = [1 for i in range (buffer_size-1)]
    lms = [0 for i in range(buffer_size-1)]
    for i in range(len(lms)):
        if isOdd(i):
            lms[i] = col-1
        else:
            lms[i] = row -1
    return ms,lms

def rewarding(seq,seq_reward,token):
    reward = 0
    for i in range(len(seq)):
        if isSubset(seq[i],token):
            reward += seq_reward[i]
    return reward

def print_cords(cords,col):
    for i in range(len(cords)):
        a,b = dig_to_idx(cords[i],col)
        print(str(a+1)+",",b+1)

def output(value,buffer,cords,col):
    print(value)
    if value > 0:
        print(buffer)
        print_cords(cords,col)

def save(file,value,buffer,cords,col):
    print("")
    print("")
    Simpan = input("Apakah ingin menyimpan solusi?(y/n)")
    while Simpan != "y" and Simpan != "n":
        print("maaf tolong jawab dengan y atau n")
        Simpan = input("Apakah ingin menyimpan solusi?(y/n)")
    if Simpan == "y":
        clear_file(file)
        f = open(file,"a")
        f.write(str(value)+"\n")
        f.write(str(buffer)+"\n")
        for i in range (len(cords)):
            x,y = dig_to_idx(cords[i],col)
            f.write(str(x)+",",str(y)+"\n")
        
