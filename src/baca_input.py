
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

def check_file_validity(file):
    valid = True
    f = open(file,"r")
    buffer_size = int(f.readline())
    if buffer_size < 1:
        print("Buffer size invalid")
        print("Buffer size minimum : 1")
        valid = False


    r2 = f.readline().split()
    row = int(r2[0])
    col = int(r2[1])

    if row < 1 or col < 1:
        print("Row or Column size invalid")
        print("Row and Column size minimum : 1")
        valid = False

    matrix = ["" for i in range(row)]
    for i in range(row):
        matrix[i] = f.readline().split()


    number_of_seq = int(f.readline())
    if number_of_seq < 1:
        print("Row or Column size invalid")
        print("Row and Column size minimum : 1")
        valid = False
        
    seq = ["" for i in range(number_of_seq)]
    seq_reward = [0 for i in range(number_of_seq)]
    for i in range(number_of_seq):
        seq[i] = f.readline().split()
        seq_reward[i] = int(f.readline())
    return valid

