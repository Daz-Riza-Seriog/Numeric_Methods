import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.optimize import fsolve # fsolve allow us to do the code more quickly
import sympy as sp
sns.set()

#e define the Variable "x" how a symbolic
x = sp.Symbol('x')

def f(x):
    y = 1-((x**2)/4)
    return y

def bisection(a,b,tol):
    xl = a
    xr = b
    while(np.abs(xl-xr)>=tol):
        c = (xl+xr)/2.0
        prod = f(xl)*f(c)
        if prod > tol:
            xl =c
        else:
            if prod < tol :
                xr = c
    return c

answer = bisection(-5,5,1e-10)
print("Bisection Method Gives Root At x=", answer)

## Shorcut Way Super Eassy

shortcut = fsolve(f,[-1.5,1.5]) #In the array yuo define the Range to find the Zero
print("Bisection Method 'fsolve' Gives Root At x=", shortcut)

print('\nFirst Derivate of f(x):\t', sp.diff(f(x),x,1))
print('\nFirst Derivate of f(x):\t', sp.diff(f(x),x,2))
print('\nFirst Derivate of f(x):\t', sp.diff(f(x),x,3))
print('\nEvaluate:\t',f(-0.3))
print('\nEvaluate:\t',f(f(-0.3)))
print('\nEvaluate:\t',f(f(f(-0.3))))
print('\nEvaluate:\t',f(f(f(f(-0.3)))))
print('\nEvaluate:\t',f(f(f(f(f(-0.3))))))

x = np.linspace(-2,2,100)
plt.plot(x,f(x))
plt.show()