# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:36:40 2020

@author: T-Gamer
"""


import numpy as np
import matplotlib.pyplot as plt

W = int(input("Qual tarefa deseja rodar (1 ou 2)? "))
W2 = int(input("Qual item deseja rodar (a=1, b=2 e c=3? "))


if W == 1:
    if W2 == 1:
        
    ## ITEM A ##
        
        T = 1
        N = int(input("Digite um valor de N: "))
        Lbd = float(input("Digite um valor de Lbd: "))
        M = int((T*N**2)/Lbd)
        print("N =",N)
        print("M =",M)
        print("Lbd =",Lbd)
        
        U = np.zeros((M+1,N+1),dtype=float)
        e = np.zeros((M+1,N+1), dtype=float)
        
        
        dt = T/M
        dx = 1/N

        for i in range(N+1): #Laço para t=0
            x=i*dx   #Local da barra
            U[0,i]=(x**2)*(1-x)**2 # temperatura incial ao longo da barra
            
        for k in range(M+1): #Laço temporal
            t=k*dt  #Instante atual
        
            for i in range(N+1): #Laço espacial
                x=i*dx    #Local da barra
                Ftx = (10*np.cos(10*t)*(x**2)*(1-x)**2)-(1+np.sin(10*t))*(12*x**2-12*x+2)      
                UtxExata = (1+np.sin(10*t))*(x**2)*(1-x)**2
                    
                #FRONTEIRAS X=0 E X=N
                if i==0 or i==N:
                    U[k,i]=0
                          
                #TRECHOS INTERIORES DA BARRA
                elif k<M:
                    U[k+1,i]=U[k,i]+dt*(((U[k,i-1]-2*U[k,i]+U[k,i+1])/dx**2)+Ftx)
                e[k,i]=U[k,i]-UtxExata    
                    
                
        emax = np.max(e)
        plt.plot(U)        
                
        
        print (U)
        print (emax)   

        
    elif W2 == 2:

        ## ITEM B ##
        
        T = 1
        N = int(input("Digite um valor de N: "))
        Lbd = float(input("Digite um valor de Lbd: "))
        M = int((T*N**2)/Lbd)
        print("N =",N)
        print("M =",M)
        print("Lbd =",Lbd)
        
        U = np.zeros((M+1,N+1),dtype=float)
        e = np.zeros((M+1,N+1), dtype=float)
        
        
        dt = T/M
        dx = 1/N        
        
        for i in range(N+1): #Laço para t=0
            x=i*dx   #Local da barra
            U[0,i]= np.exp(-x) # temperatura incial ao longo da barra (U0)
            
        for k in range(M+1): #Laço temporal
            t=k*dt  #Instante atual
        
            for i in range(N+1): #Laço espacial
                x=i*dx    #Local da barra
                Ftx = -np.exp(t-x)*(np.cos(5+x)*(x+t**2-25*t**2)+np.sin(5+t)*(5*x-10*t**2))    
                UtxExata = np.exp(t-x)*np.cos(5*t*x)  
                    
                #FRONTEIRAS X=0 E X=N
                if i==0:
                    U[k,i] = np.exp(t)
                
                elif i==N:
                     U[k,i] = np.exp(t-1)*np.cos(5*t)
                #TRECHOS INTERIORES DA BARRA
                elif k<M:
                    U[k+1,i]=U[k,i]+dt*(((U[k,i-1]-2*U[k,i]+U[k,i+1])/dx**2)+Ftx)
                e[k,i]=U[k,i]-UtxExata    
                    
                
        emax = np.max(e)
        plt.plot(U)        
                
        
        print (U)
        print (emax)           
            
        
    