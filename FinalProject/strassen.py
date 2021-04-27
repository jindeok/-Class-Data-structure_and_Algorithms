import numpy as np
import networkx as nx
import time

def matrix_multiplication(M,N): 
    # List to store matrix multiplication result 
    l = len(M[0])
    R = np.zeros((l,l))
    for i in range(0, l):  
        for j in range(0, l): 
            for k in range(0, l):  
                R[i][j] += M[i][k] * N[k][j]  
    return R



#Strassen algorithm definition
def Strassen_Algorithm(A,B):
    n1,m1=A.shape; n2,m2=B.shape;
    result=np.zeros((n1,m2));
    
    # Zero paddings prerocessing for generalization sizes
    temp=0
    #for matrix A
    if n1>=m1:
        temp=0
        while 2**temp<n1:
            temp+=1
    else:
        while 2**temp<m1:
            temp+=1
    
    AP=np.pad(A,((0,2**temp-n1),(0,2**temp-m1)),'constant', constant_values=0);
    
    #for matrix B
    if n2>=m2:
        temp=0
        while 2**temp<n2:
            temp+=1
    else:
        while 2**temp<m2:
            temp+=1
    
    BP=np.pad(B,((0,2**temp-n2),(0,2**temp-m2)),'constant', constant_values=0);
     
    
    k=BP.shape[0]; # size of the matrix after padding
    
    if k==1:
        C=AP.dot(BP);
        result=C[0:n1,0:m2] # removing padding elements & n1*m1 matrix * n2*m2 matrix = n1*m2 matrix
        return result;
    
    else:  
        # D&C Recursive formula for Strassen's multiplication formula
        AP11=AP[0:int(k/2),0:int(k/2)]
        AP12=AP[0:int(k/2),int(k/2):]
        AP21=AP[int(k/2):,0:int(k/2)]
        AP22=AP[int(k/2):,int(k/2):]
        BP11=BP[0:int(k/2),0:int(k/2)]
        BP12=BP[0:int(k/2),int(k/2):]
        BP21=BP[int(k/2):,0:int(k/2)]
        BP22=BP[int(k/2):,int(k/2):]        
        
        # Strassen Recusive : Function calls function itself
        M1=Strassen_Algorithm(AP11+AP22,BP11+BP22);
        M2=Strassen_Algorithm(AP21+AP22,BP11)
        M3=Strassen_Algorithm(AP11,BP12-BP22)
        M4=Strassen_Algorithm(AP22,BP21-BP11)
        M5=Strassen_Algorithm(AP11+AP12,BP22)
        M6=Strassen_Algorithm(AP21-AP11,BP11+BP12)
        M7=Strassen_Algorithm(AP12-AP22,BP21+BP22)
        
        
        C11=M1+M4-M5+M7; C12=M3+M5; C21=M2+M4; C22=M1+M3-M2+M6;
        n=C11.shape[0]
        C=np.zeros((2*n,2*n))
        C[:n,:n]=C11; C[:n,n:]=C12; C[n:,:n]=C21; C[n:,n:]=C22
        result=C[:n1,:m2] # removing padding elements & n1*m1 matrix * n2*m2 matrix = n1*m2 matrix
        return result;
  
#initiallize graph G and extract adjacency matrix
G = nx.triangular_lattice_graph(5,5)
A = nx.to_numpy_array(G)
nodenum = len(A[0])
print(' # of node for G is:', nodenum)
      

start3 = time.time()  # Time check start point for algo#3
#main function for algorithm#3
B=Strassen_Algorithm(A,A)
C=Strassen_Algorithm(A,B)
tri_num = np.sum(np.diag(C))/6

print("Completed time for Strassen's :", time.time() - start3)  # 현재시각 - 시작시간 = 실행 시간
#main function for algorithm#2
start2 = time.time()  # Time check start point for algo#2

B2 = matrix_multiplication(A,A)
C2 = matrix_multiplication(B2,A)
tri_num = np.sum(np.diag(C))/6
print("Completed time for conventional multiplication :", time.time() - start2)  # 현재시각 - 시작시간 = 실행 시간

#print('sum of the diagonal elements divided by 3!: ',tri_num)
