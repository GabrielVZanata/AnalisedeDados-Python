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
U = np.zeros((M+1,N+1),dtype=float)
Unovo = np.zeros((N+1),dtype=float)
e = np.zeros((M+1,N+1), dtype=float)


dt = T/M
dx = 1/N

## ITEM A ##


for k in range(M+1): #Laço temporal
    t=k*dt  #Instante atual
    
    for i in range(N+1): #Laço espacial
        x=i*dx    #Local da barra
        Ftx = (10*np.cos(10*t)*(x**2)*(1-x)**2)-(1+np.sin(10*t))*(12*(x**2)-12*x+2)      
        UtxExata = (1+np.sin(10*t))*(x**2)*(1-x)**2
        
        #INSTANTE T=0
        if k==0:
            U[k,i]=(x**2)*(1-x)**2 # temperatura incial ao longo da barra
            if i>0 and i<N:
                U[k+1,i]=U[k,i]+dt*(((U[k,i-1]-2*U[k,i]+U[k,i+1])/dx**2)+Ftx)
                    
        #FRONTEIRAS X=0 E X=N
        if i==0 or i==N:

            U[k,i]=0
        
                  
        #TRECHOS INTERIORES DA BARRA
        elif k<M:
            U[k+1,i]=Unovo[i]
            e[k,i]=U[k+1,i]-UtxExata
        Unovo[i]=U[k,i]+dt*(((U[k,i-1]-2*U[k,i]+U[k,i+1])/dx**2)+Ftx)
        
emax = np.max(e[M+1,:])
        
        

print (U)
print (emax)   

   
         
            
        
    