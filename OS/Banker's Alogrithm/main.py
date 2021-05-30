import bankers as bk

def main():
    #System status(processes& resoures) vectors: alloction, need, availble
    allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 3], [2, 1, 1], [0, 0, 2]]
    need = [[0, 0, 2], [2, 2, 2], [0, 0, 0], [1, 0, 0], [0, 0, 2]]
    available = [0, 0, 0]
    
    #Inputs into Banker's Algorithm: vectors, 5 processes, 3 kinds of resoures
    print(bk.bankers(allocation, need, available, 5, 3))
    
main()
