
def baca_file(x):
    file = open(x)
    buffer_size = int(file.readline())
    r2 = file.readline().split()
    row = int(r2[0])
    col = int(r2[1])
    matrix = ["" for i in range(row)]
    for i in range(row):
        matrix[i] = file.readline().split()
    number_of_seq = int(file.readline())
    seq = ["" for i in range(number_of_seq)]
    seq_reward = [0 for i in range(number_of_seq)]
    for i in range(number_of_seq):
        seq[i] = file.readline().split()
        seq_reward[i] = int(file.readline())
    return buffer_size,matrix,row,col,seq,seq_reward

