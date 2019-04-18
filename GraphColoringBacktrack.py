import numpy as np
from random import randint
import networkx as nx
import matplotlib.pyplot as plt

    
def draw_graph(hubungan,color): #untuk menampilkan graph
    G=nx.Graph()
    G.add_edges_from(hubungan)
    co = [color[i] for i in G.nodes()]
    nx.draw(G, node_size=1000/(len(hubungan)/10),node_color=co,
            with_labels=True,font_color='white')
    plt.show()

def generateRandomGraph(nodes,a,b): #membuat graf random
    L = np.zeros((node,node),dtype=int)
    for i in range(nodes):
        for j in range(nodes):
            if i != j and L[i][j] == 0:
                v = int(np.random.choice(2, 1,p=[a,b]))
                if v == 1 :
                    L[i][j] = v
                    L[j][i] = v
    return L
#-------------------------- inti program begin -------------------------    
def isSafe(co,list_color,n):
    for i in range(node-1): #untuk setiap node lain
        if adj_mtx[n][i] == 1 and list_color[i] == co: #jika bertetangga dan warnanya sama
            return False
    return True

def findSolution(list_color,n):
    if(n == node): #kalo udah semua node di warnai
        return True
    for co in range(1,mc+1): #coba setiap warna
        if(isSafe(co,list_color,n)): #if warna bisa di pakai
            list_color[n] = co #assign dengan warna co
            if findSolution(list_color,n+1): #pindah ke node lain
                return True
            list_color[n] = 0 #kalo gabisa, hapus warna sekarang
    return False

def graphColoring(mtx,mc):
    list_color = np.zeros(node,dtype=int)
    print('>> Maximum color :', mc)
    if not(findSolution(list_color,0)): #kalo ga ada solusi
        print('>> Solution not found')
        return False
    print('>> Solution Found :',list_color)
    print('>> Minimum color needed :', max(list_color))
    draw_graph(hubungan,list_color)
    
#-------------------------- inti program ends ------------------------------
    
node = int(input("Generate Random Graph, tentukan jumlah node : "))
#semakin besar probabilitas, semakin banyak koneksi
p = float(input("probabilitas terbentuk koneksi (0.1 - 0.9): ")) 
adj_mtx = generateRandomGraph(node,1-p,p)
print(adj_mtx)

#cari keterhubungan
hubungan = []
for i in range(len(adj_mtx)):
    for j in range(len(adj_mtx[i])):
        if adj_mtx[i][j] == 1 and (i,j) not in hubungan and (j,i) not in hubungan:
            hubungan.append((i,j))
            
mc = node #max color 
graphColoring(adj_mtx,mc)
