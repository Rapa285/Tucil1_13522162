from src.baca_input import baca_file

def get_token(matrix,Initial_point,movement_sequence):
    current_row = 0
    current_col = Initial_point
    token = str(matrix[current_row][current_col])
    for i in range (len(movement_sequence)):
        if (i%2 == 0):
            current_row = (current_row + movement_sequence[i])%len(matrix)
        else:
            current_col = (current_col + movement_sequence[i])%len(matrix[0])
        token += " " + matrix[current_row][current_col]
    print(token)
    return token

def isSubset(seq,array):
    found = False
    i = 0
    k = 0
    while (found == False and i < len(array)): 
        if (seq[k] == array[i] and found == False):
            k+=1
            i+=1
            #print("flag if")
        else:
            i+=1
            k = 0
            #print("flag else",end=" ")
            #print(i)
        if (k == len(seq)):
            found = True
            #print("flag found")
    #print("hasil:")
    #print(found)
    #print("")
    return found

def get_token_value(token,seq,seq_reward):
    value = 0
    for i in range (len(seq)):
        print(seq[i])
        print(seq_reward[i])
        if(isSubset(seq[i],token)):
            value += seq_reward[i]
    print(value)
    

def get_max_token_value(seq_reward):
    value = 0
    for i in range(len(seq_reward)):
        value += seq_reward[i]
    return value


buffer_size,matrix,seq,seq_reward = baca_file("test.txt")

def main():
    m_seq = [0 for i in range(buffer_size-1)]
    token_cordinates = [["",""] for i in range(buffer_size)]
    token_value = 0
    count = 0
    max_value = get_max_token_value(seq_reward)
    finished = False
    while (token_value < max_value and finished == False):
        for i in range (buffer_size):
            if (i%2 == 0):
                i+=0


def locate_sequence(matrix,seq):
    row = len(matrix)
    col = len(matrix[0])
    count = 0
    impossible = False
    seq_cords = []
    while(count <= len(seq) and impossible == False):
        for i in range(row):
            for j in range(col):
                if (matrix[i][j] == seq[count]):
                    seq_cords.append([i,j])
                    count+= 1

        if (count == 0):
            impossible = True

def locate_next(matrix,curr_pos,target,direction): # curr_pos [x,y] in the matrix
    row = len(matrix)
    col = len(matrix[0])
    target_cords = []
    if (direction == "Horizontal"):
        for i in range(col):
            if (matrix[curr_pos[0],(curr_pos[1]+i)%col] == target):
                target_cords.append([curr_pos[0],curr_pos[(1+i)%col]])
    else:
        for i in range(row):
            if (matrix[(curr_pos[0]+i)%row,curr_pos[1]] == target):
                target_cords.append([curr_pos[0],curr_pos[(1+i)%row]])
    return target_cords


curr_pos = [int(0),int(0)]
target = "7A"
direction = "Vertical"
target_cords = locate_next(matrix,curr_pos,target,direction)
print(target_cords)

    

    