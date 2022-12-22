# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:36:40 2020

@author: T-Gamer
"""


import numpy as np
import matplotlib as plt


T = 1
N = int(input("Digite um valor de N: "))
Lbd = float(input("Digite um valor de Lbd: "))
M = int((T*N**2)/Lbd)
print("N =",N)
print("M =",M)
print("Lbd =",Lbd)


Gi = np.zeros((M+1),dtype=float)
Gf = np.zeros((M+1),dtype=float)
U = np.zeros((M+1,N+1),dtype=int)
e = np.zeros(N+1, dtype=int)
emax = np.zeros(M+1, dtype=int)

dt = T/M
dx = 1/N

for k in range(M+1): #Laço temporal
    t=k*dt  #Instante atual
    

    
    for i in range(N+1): #Laço espacial
        x=i*dx    #Local da barra
        Ftx = (10*(x**2)*(x-1))-(60*x*t)-(20*t)       
        UtxExata = 10*t*x**2*(x-1)
        #INSTANTE T=0
        if k==0:
            U[k,i]=0 # para t=0 a temperatura é 0 em toda a barra
            
        #FRONTEIRAS X=0 E X=N
        elif i==0 or i==N:

            U[k,i]=Ftx
                  
        #TRECHOS INTERIORES DA BARRA
        elif k<M:
            U[k+1,i]=U[k,i]+dt*(((U[k,i-1]-2*U[k,i]+U[k,i+1])/dx**2)+Ftx)
            e[i]= abs(U[k+1,i]-UtxExata)
 
        
        
    emax[k]=np.max(e)

print (U)
print (e)   

   
         
            
        
    