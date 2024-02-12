from src.function import *
from src.baca_input import *
from src.matrix_generator import*

#buffer_size,matrix,row,col,seq,seq_reward = baca_file("test.txt")
buffer_size,matrix,row,col,seq,seq_reward = generate()
movement_sequence,last_mov_seq = mov_seq(buffer_size,row,col)
#print(movement_sequence)
cords,token = get_cords_token(matrix,0,movement_sequence) 
#print(cords)
#print(token)
#print(seq)
#print(seq_reward)


start = time.time()

max = 0
max_cords = []
max_token = ""
max_possible = get_max_reward(seq_reward)
for i in range(len(matrix[0])):
    movement_sequence,last_mov_seq = mov_seq(buffer_size,row,col)
    while movement_sequence != last_mov_seq and max != max_possible:
        cords,token = get_cords_token(matrix,i,movement_sequence)
        if is_unique(cords):
            tk = token.split()
            reward = rewarding(seq,seq_reward,tk)
            if reward > max:
                max = reward
                max_token = token
                max_cords = cords
        movement_sequence = next_move_seq(movement_sequence,row,col,len(movement_sequence)-1)

output(max,max_token,max_cords,col)

end = time.time()
print("")
print("")
print((end-start)*1000,"ms")


