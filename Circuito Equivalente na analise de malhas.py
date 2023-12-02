# bibliotecas
import numpy as np
import sympy as sp
from IPython.display import Math

# Cálculos

# Dados de entrada
Vin=50;R1=5;ZC1=-7j;ZL1=3j;ZL2=5j;ZM=.8*np.sqrt(ZL1*ZL2);Ro=6
print('ZM='+str(ZM))

#Variáveis
I1,I2 = sp.symbols('I1,I2')

# Malhas 1
X = sp.solve([-Vin + R1*I1 + ZC1*I1 + ZL1*(I1-I2) + ZM*(-I2),
              -ZM*(-I2) + ZL1*(I2-I1)+ ZL2*I2 - ZM*(I1-I2) + Ro*I2],[I1,I2])
display(X)

# Malhas 2
X = sp.solve([-Vin + R1*I1 + ZC1*I1 - ZM*I1 + (ZL1+ZM)*(I1-I2),
              (ZL1+ZM)*(I2-I1) + (ZL2+ZM)*I2 + Ro*I2],[I1,I2])
display(X)

I1 = complex(X[I1])
I2 = complex(X[I2])

display(Math(r'I_1= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{A}' %(abs(I1),np.angle(I1,deg=True))))
display(Math(r'I_2= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{A}' %(abs(I2),np.angle(I2,deg=True))))
