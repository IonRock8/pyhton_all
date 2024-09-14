msg = "Hello world"
print (msg)
a = 10
b = 20
print(a+b)
for x in range(1,10) :
    print(x)

import numpy as np
y = np.array(range(1,10))
z = np.array(range(11,20))
print(y)
print(z)
print(y+z)

import matplotlib.pyplot as plt
plt.plot(y,z)
plt.show()