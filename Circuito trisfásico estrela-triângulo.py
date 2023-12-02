## 1. Dado um circuito trifásico estrela-triângulo equilibrado de sequência positiva com tensão de 220V e referência  na tensão de linha “$V_{ab}$” com ângulo zero (peso total: 4,0):

#Impedância da em cada linha  (2+3j)Ω 
#Corrente na linha “ a “  10A  com ângulo  30. 

#Cálculos
import sympy as sp
import numpy as np
from IPython.display import Math

# dados de entrada
V,Vabphi,Zl,Iam,Iaphi=220,0,2+3j,10,30

# Tensões de linha
Vab = V*np.exp(1j*Vabphi*np.pi/180)
Vbc = Vab*np.exp(-2j*np.pi/3)
Vca = Vab*np.exp(2j*np.pi/3)

# Corrente de linha (Corrente de fase na fonte)
Ia = Iam*np.exp(1j*Iaphi*np.pi/180)
Ib = Ia*np.exp(-2j*np.pi/3)
Ic = Ia*np.exp(2j*np.pi/3)

# Corrente de fase na carga
IAB = Ia/np.sqrt(3)*np.exp(1j*np.pi/6)
IBC = IAB*np.exp(-2j*np.pi/3)
ICA = IAB*np.exp(2j*np.pi/3)

# Impedância da carga
ZAB = ZBC = ZCA = Vab/IAB-3*Zl
display(Math(r'$Z_\mathrm{AB} = %s \Omega$' %(ZAB)))

# Tensão de fase na fonte
Va = Vab/np.sqrt(3)*np.exp(-1j*np.pi/6)
Vb = Va*np.exp(-2j*np.pi/3)
Vc = Va*np.exp(2j*np.pi/3)

# Tensão de fase na Carga (Tensão de linha na carga)
VAB = ZAB*IAB
VBC = VAB*np.exp(-2j*np.pi/3)
VCA = VAB*np.exp(2j*np.pi/3)

# fonte
V_fonte_fase,I_fonte_fase,V_fonte_linha,I_linha = Va,Ia,Vab,Ia
# carga
V_carga_fase,I_carga_fase,V_carga_linha = VAB,IAB,VAB

display(Math(r'$ \begin{matrix}  & \text{Fonte} &  & \text{Carga} &  \\  & \text{Tensão} & \text{Corrente} & \text{Tensão} & \text{Corrente} \\ \text{Fase} ~~~ & V_\mathrm{a}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{V} & I_\mathrm{a}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{A} & V_\mathrm{AB}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{V} & I_\mathrm{AB}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{A} \\  & V_\mathrm{b}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{V} & I_\mathrm{b}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{A} & V_\mathrm{BC}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{V} & I_\mathrm{BC}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{A} \\  & V_\mathrm{c}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{V} & I_\mathrm{c}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{A} & V_\mathrm{CA}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{V} & I_\mathrm{CA}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{A} \\ \text{Linha} ~~~ & V_\mathrm{ab}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{V} & I_\mathrm{a}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{A} & V_\mathrm{AB}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{V} & I_\mathrm{a}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{A} \\  & V_\mathrm{bc}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{V} & I_\mathrm{b}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{A} & V_\mathrm{BC}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{V} & I_\mathrm{b}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{A} \\  & V_\mathrm{ca}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{V} & I_\mathrm{c}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{A} & V_\mathrm{CA}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{V} & I_\mathrm{c}= %.2f ~ \angle %.1f ^\mathrm{o} \mathrm{A} \end{matrix} $' %(abs(V_fonte_fase),np.angle(V_fonte_fase,deg=True),abs(I_fonte_fase),np.angle(I_fonte_fase,deg=True),abs(V_carga_fase),np.angle(V_carga_fase,deg=True),abs(I_carga_fase),np.angle(I_carga_fase,deg=True),abs(V_fonte_fase),np.angle(V_fonte_fase,deg=True)-120,abs(I_fonte_fase),np.angle(I_fonte_fase,deg=True)-120,abs(V_carga_fase),np.angle(V_carga_fase,deg=True)-120,abs(I_carga_fase),np.angle(I_carga_fase,deg=True)-120,abs(V_fonte_fase),np.angle(V_fonte_fase,deg=True)+120,abs(I_fonte_fase),np.angle(I_fonte_fase,deg=True)+120,abs(V_carga_fase),np.angle(V_carga_fase,deg=True)+120,abs(I_carga_fase),np.angle(I_carga_fase,deg=True)+120,abs(Vab),np.angle(Vab,deg=True),abs(Ia),np.angle(Ia,deg=True),abs(VAB),np.angle(VAB,deg=True),abs(Ia),np.angle(Ia,deg=True),abs(Vbc),np.angle(Vbc,deg=True),abs(Ib),np.angle(Ib,deg=True),abs(VBC),np.angle(VBC,deg=True),abs(Ib),np.angle(Ib,deg=True),abs(Vca),np.angle(Vca,deg=True),abs(Ic),np.angle(Ic,deg=True),abs(VCA),np.angle(VCA,deg=True),abs(Ic),np.angle(Ic,deg=True))))