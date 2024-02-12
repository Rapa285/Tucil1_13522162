import random

def generate_matrix(token,row,col):
    matrix = []
    for i in range(row):
        r = random.choices(token,k=col)
        matrix.append(r)
    return matrix

def display_matrix(matrix):
    print("Matrix : ")
    print("")
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col-1):
            print(matrix[i][j],end=" ")
        print(matrix[i][j+1])

def generate_seq(token,N,max):
    seq = []
    for i in range(N):
        r = random.randint(2,max)
        #print(r)
        sq = random.choices(token,k=r)
        seq.append(sq)
    return seq

def generate_seq_reward(N):
    seq_reward = []
    for i in range (N):
        reward = random.randrange(-50,50,5)
        seq_reward.append(reward)
    return seq_reward

def display_seq(seq,seq_reward):
    print("Sequence : ")
    print("")
    for i in range(len(seq)):
        for j in range(len(seq[i])-1):
            print(seq[i][j],end=" ")
        print(seq[i][j+1])
        print(seq_reward[i])

def generate():
    jumlah_token_unik = int(input(""))
    token = ["" for i in range(jumlah_token_unik)]
    token = input("").split(" ")
    ukuran_buffer = int(input(""))
    row_matriks, collumn_matriks = map(int, input("").split())
    jumlah_sekuens = int(input(""))
    ukuran_maksimal_sekuens = int(input(""))

    '''
    print("data : ")
    print(jumlah_token_unik)
    for i in range(jumlah_token_unik):
        print(token[i], end=" ")
    print("")
    print(ukuran_buffer)
    print(row_matriks)
    print(collumn_matriks)
    print(jumlah_sekuens)
    print(ukuran_minimal_sekuens)
    print(ukuran_maksimal_sekuens)'''

    matrix = generate_matrix(token,row_matriks,collumn_matriks)
    seq = generate_seq(token,jumlah_sekuens,ukuran_maksimal_sekuens)
    seq_reward = generate_seq_reward(jumlah_sekuens)
    print("")
    display_matrix(matrix)
    print("")
    display_seq(seq,seq_reward)
    print("")
    print("")
    return ukuran_buffer,matrix,row_matriks,collumn_matriks,seq,seq_reward

