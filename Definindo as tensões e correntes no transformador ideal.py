# bibliotecas
import numpy as np
import sympy as sp
from IPython.display import Math

# Cálculos

# Dados de entrada
Vin=50;R1=5;N1=5;N2=10;ZL1=4j;ZC1=-5j;Ro=10;n=N2/N1;

# Relação de transformação
print('n='+str(n))

#Variáveis
I1,I2,Io,Vp,Vs,Ip,Is = sp.symbols('I1,I2,Io,Vp,Vs,Ip,Is')

# Malhas 1
X = sp.solve([-Vin + R1*I1 + Vp,
              -Vp+ZC1*I2+ZL1*(I2-Io)-Vs,
              Vs+ZL1*(Io-I2)+Ro*Io,
              Vs-n*Vp,
              Ip-n*Is,
              -Ip+I1-I2,
              -Is+I2-Io],[I1,I2,Io,Vp,Vs,Ip,Is])
display(X)

I1 = complex(X[I1])
I2 = complex(X[I2])
Io = complex(X[Io])

display(Math(r'I_1= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{A}' %(abs(I1),np.angle(I1,deg=True))))
display(Math(r'I_2= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{A}' %(abs(I2),np.angle(I2,deg=True))))
display(Math(r'I_\mathrm{o}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{A}' %(abs(Io),np.angle(Io,deg=True))))