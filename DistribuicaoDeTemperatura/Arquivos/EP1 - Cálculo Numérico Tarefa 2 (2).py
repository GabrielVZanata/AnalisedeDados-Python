# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:36:40 2020

@author: T-Gamer
"""


import numpy as np
import matplotlib.pyplot as plt

W = int(input("Qual tarefa deseja rodar (1 ou 2)? "))
W2 = int(input("Qual item deseja rodar (a=1, b=2 e c=3)? "))

## TAREFA 1 ##

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
            
    elif W2 == 3:

        ## ITEM C ##
        
        T = 1
        N = int(input("Digite um valor de N: "))
        Lbd = float(input("Digite um valor de Lbd: "))
        M = int((T*N**2)/Lbd)
        print("N =",N)
        print("M =",M)
        print("Lbd =",Lbd)
        
        U = np.zeros((M+1,N+1),dtype=float)
        
        
        dt = T/M
        dx = 1/N        
        

            
        for k in range(1,M+1): #Laço temporal excluindo 0 instante inicial pois u0(x)=0
            t=k*dt  #Instante atual
        
            for i in range(N+1): #Laço espacial
                x=i*dx    #Local da barra
            
                rt = 10000*(1-2*(t**2)) #Função rt que determina a intensidade da fonte pontual
                
                # Definindo a função gh que delimita a ação da fonte pontual
                p = 0.25
                h = dx
                if x>=(p-(h/2)) and x<=(p+(h/2)):
                    gh = 1/h
                else:
                    gh = 0
                    
                Ftx = rt*gh  #Comportamento da fonte pontual
                  
                    
                #FRONTEIRAS X=0 E X=N
                if i==0 or i==N:
                    U[k,i] = 0
                

                #TRECHOS INTERIORES DA BARRA
                elif k<M:
                    U[k+1,i]=U[k,i]+dt*(((U[k,i-1]-2*U[k,i]+U[k,i+1])/dx**2)+Ftx)
                
        plt.plot(U)  
        print (U)

## TAREFA 2 ##

if W == 2:
    if W2 == 1:
        
        ## ITEM A ##
        
        T = 1
        N = int(input("Digite um valor de N: "))
        Lbd = float(input("Digite um valor de Lbd: "))
          
        M = int((T*N**2)/Lbd)
        ad = np.full(N-1,1+2*Lbd)
        asd = np.full(N-1,-Lbd)
        asd[0]=0
        a = np.zeros((N-1,N-1),dtype=float)
        D = np.zeros(N-1,dtype=float)
        L = np.zeros(N-1,dtype=float)
        v = np.zeros(N-1,dtype=float)
        
        for i in range (N-1):
            for z in range (N-1):
                if z==i:
                    a[i,z]=ad[i]
                elif z==i+1:
                    a[i,z]=asd[i+1]
                    a[i+1,z-1]=asd[i+1]



        
        
        print("N =",N)
        print("M =",M)
        print("Lbd =",Lbd)
        print(ad)
        print(asd)
        print(a)
        
        
        D[0]=ad[0]
        for i in range(1,N-1):
            L[i]=asd[i]/D[i-1]
            D[i]=ad[i]-(L[i]*asd[i])
print (D)
print (L)