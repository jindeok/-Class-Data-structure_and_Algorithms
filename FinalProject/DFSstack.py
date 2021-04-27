import numpy as np
import networkx as nx
import time
import copy



class Stack(list):
    push = list.append    # Push to Stack
                          # Delete - python internal pop method
        
    def is_empty(self):   # check whether it is empty or not
        if not self:
            return True
        else:
            return False

    def peek(self):        # very last data checking
        return self[-1]
    
    def clear(self): # clear stack
        list.clear()
    
#initiallize graphs
G = nx.triangular_lattice_graph(10,20)
A = nx.to_numpy_array(G)
nodenum = len(A[0])
print(' # of node for G is:', nodenum)
#initiallize stack
s = Stack()


start = time.time()  # Time check start point

#main algorithm using DFS & Stack
tri_trace = []
for i in range(nodenum):
    s.push(i)
    for j in range(nodenum):
        if A[i][j] == 1:
            s.push(j)
            for k in range(nodenum):
                if A[j][k] == 1:
                    s.push(k)
                    if A[k][i] == 1:
                        #print("Stack is full:", s)
                        s_to_append = copy.deepcopy(s)
                        tri_trace.append(s_to_append)                                       
                    s.pop()
            s.pop()
    s.pop()       
    
tri_num = len(tri_trace)/6

print("Completed time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

print('total number of triangles in a graph is:', tri_num)