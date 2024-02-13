from function import *
from baca_input import *
from matrix_generator import*

print("Cyberpunk 2077 Breach Protocol Solver")
print("Pilih cara menginput")
print("1). File.txt")
print("2). Randomize")
cara_input = int(input("(1/2) : "))
while cara_input != 1 and cara_input != 2:
    print("maaf tidak ada pilihan tersebut, mohon untuk memilih dari pilihan dibawah ini")
    print("1). File.txt")
    print("2). Randomize")
    cara_input = input("(1/2) : ")

if cara_input == 1:
    file = input("Nama file input : ")
    buffer_size,matrix,row,col,seq,seq_reward = baca_file(file)
else:
    buffer_size,matrix,row,col,seq,seq_reward = generate()

max = 0
max_cords = []
max_token = ""
max_possible = get_max_reward(seq_reward)

start = time.time()

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
        movement_sequence = next_move_seq(movement_sequence,row,col,0)

output(max,max_token,max_cords,col)

end = time.time()
timer = (end-start)*1000
print("")
print("")
print(timer,"ms")

save(max,max_token,max_cords,col,timer)
