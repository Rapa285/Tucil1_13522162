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
        for j in range(col):
            if j < col-1:
                print(matrix[i][j],end=" ")
            else:
                print(matrix[i][col-1])

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
    while jumlah_token_unik < 1:
        print("jumlah token unik minimal 1, mohon untuk menginput ulang")
        jumlah_token_unik = int(input(""))

    token = input("").split(" ")
    while check_token_validity(token) == False:
        print("Maaf token hanya dapat berupa 2 karakter alfanumerical")
        print("Dimohon untuk menginput token ulang")
        token = input("").split(" ")

    ukuran_buffer = int(input(""))
    while ukuran_buffer < 1:
        print("ukuran buffer minimal 1, mohon untuk menginput ulang")
        ukuran_buffer = int(input(""))

    row_matriks, col_matriks = map(int, input("").split())
    while row_matriks < 2 and col_matriks < 2:
        print("ukuran baris dan kolom matriks minimal 2, mohon untuk menginput ulang")
        row_matriks, col_matriks = map(int, input("").split())

    jumlah_sekuens = int(input(""))
    while jumlah_sekuens < 1:
        print("jumlah sekuens minimal 1, mohon untuk menginput ulang")
        jumlah_sekuens = int(input(""))

    ukuran_max_seq = int(input(""))
    while ukuran_max_seq < 2:
        print("ukuran maximum sekuens minimal 2, mohon untuk menginput ulang")
        ukuran_max_seq = int(input(""))

    matrix = generate_matrix(token,row_matriks,col_matriks)
    seq = generate_seq(token,jumlah_sekuens,ukuran_max_seq)
    seq_reward = generate_seq_reward(jumlah_sekuens)
    print("")
    display_matrix(matrix)
    print("")
    display_seq(seq,seq_reward)
    print("")
    print("")
    return ukuran_buffer,matrix,row_matriks,col_matriks,seq,seq_reward

def check_token_validity(token):
    test = True
    for i in range(len(token)):
        if len(token[i]) != 2:
            test = False
        else:
            if isAlfaNum(token[i]) == False:
                test = False
    return test
            

def isAlfaNum(x):
    test = True
    for i in range (len(x)):
        if isAlfa(x[i]) == False and isNum(x[i]) == False:
            test = False
    return test

def isAlfa(x):
    test = False
    Alfa = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(Alfa)):
        if x == Alfa[i]:
            test = True
    return test

def isNum(x):
    test = False
    Num = "1234567890"
    for i in range(len(Num)):
        if x == Num[i]:
            test = True
    return test

