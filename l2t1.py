import math
import numpy as np
print("Enter rows and cols") #count = cols*rows, count x = count y
rows = int(input())
cols = int(input())
x = np.random.uniform(-1,1,(rows,cols))
y = np.random.uniform(-1,1,(rows,cols))
countp = 0 #the number of points hit
countf = 0 #the number of missed points
try:
    for i,f in enumerate(x):
        for j,ff in enumerate(y):
            if(math.sqrt(f[i]**2+ff[j]**2))<=1:
                countp += 1
            else:
                countf +=1
    print(countp, " | ",countf)
except IndexError:
    print("Rows must be equals cols")
