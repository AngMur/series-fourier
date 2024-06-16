from sympy.parsing.sympy_parser import split_symbols_custom
#Importamos el módulo simpy
from sympy import *
#Además importamos las variables simbólicas 'n' y 't'
from sympy.abc import t, n
import sys
from decimal import *
import math 

getcontext().prec = 100
p1 = Decimal(3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117070)

#Cambiamos el limite máximo de iteración en python
sys.setrecursionlimit(10000)

#Ingresamos los armónicos
armonicos = int(input('Ingresa el número de armónicos: '))
'''
Generamos las fórmulas para los coeficientes con la función
     | 1 Sí  0 < t <= π/2
f(t) |
     | 0 Sí  π/2 < t <= π
'''
ao = integrate(2.0 / pi, (t, 0, pi / 2.0))

#Comenzamos a formar la serie de Fourier con los armónicos proporcionados
serie = ao/2.0
for n in range(1, armonicos+1):
  #an = integrate((2 / pi) * cos(2 * n * t), (t, 0, pi / 2))
  #pprint(an)
  bn = integrate((2 / p1) * sin(2 * n * t), (t, 0, p1 / 2))
  #print(bn)
  #serie += (an* cos(2 * n * t))
  serie += (bn* sin(2.0 * n * t))

#Finalmente, mostramos la gráfica de ésta
plotting.plot(serie, ylim=(-1, 2), xlim=(-1,5))
