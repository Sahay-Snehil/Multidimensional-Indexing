import numpy as np
array = np.array([[["A","B","C"],["D","E","F"],["G","H","I"]],
                 [["J","K","L"],["M","N","O"],["P","Q","R"]],
                 [["S","T","U"],["V","W","X"],["Y","Z","A"]]])

name = array[2,0,0]+ array[1,1,1] +array[0,1,1]+array[0,2,1]+array[0,2,2]+array[1,0,2]

print(name)