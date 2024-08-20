import numpy as np

lo =np.logspace( 0,2,4)

la2 = np.linspace(0,2,4)

print(lo)

print(la2)

for i in la2:
    print(np.power(10, i))

