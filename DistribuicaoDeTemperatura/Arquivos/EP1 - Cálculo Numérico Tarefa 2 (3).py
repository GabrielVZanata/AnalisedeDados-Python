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
        
        N = int(input("Digite um valor de N: "))
        Lbd = float(input("Digite um valor de Lbd: "))
        
        #Vetores de Input
        ad = np.full(N-1,1+2*Lbd)       # Vetor com os valores da diagonal da matriz a ser decomposta
        asd = np.full(N-1,-Lbd)         # Vetor com os valores da subdiagonal da matriz a ser decomposta
        asd[0]=0                        # Adequando N-2 termos num vetor de tamnho N-1
        a = np.zeros((N-1,N-1),dtype=float) # Matriz A a ser decomposta (apenas para verificação visual).     
        b = np.zeros(N-1,dtype=float)   # Vetor do lado direito do sistema (aleatório, apenas para teste do algorítmo do item a)
        for i in range(N-1):
            b[i] = int(input("Digite um valor para o termo do vetor do lado direito do sistema: "))
            
            
        #Vetores auxiliares e de output
        D = np.zeros(N-1,dtype=float)   # Vetor representante da matriz diagonal
        L = np.zeros(N-1,dtype=float)   # Vetor representante da matriz subdiagonal 
        Raux = np.zeros(N-1,dtype=float) # Vetor resultante auxiliar, usado para calcular o vetor x 
        x = np.zeros(N-1,dtype=float)   # Vetor solução do sistema
        
        # Laço para construção visual da matriz A a ser decomposta
        #for i in range (N-1):
        #    for z in range (N-1):
        #        if z==i:
        #           a[i,z]=ad[i]
        #        elif z==i+1:
        #           a[i,z]=asd[i+1]
        #           a[i+1,z-1]=asd[i+1]



        
        # Verificação visual dos Inputs
        print("N =",N)
        print("M =",M)
        print("Lbd =",Lbd)
        # print(ad)
        # print(asd)
        # print(a)
        
        # Laço para decomposição de A em LDLt
        
        D[0]=ad[0]                  # Primeiro termo da diagonal D é igual ao primeiro termo da original A
        for i in range(1,N-1):
            L[i]=asd[i]/D[i-1]      # Termos de L em função dos termos da subdiagonal de A e da matriz diagonal D
            D[i]=ad[i]-(L[i]*asd[i]) # Termos de D em função dos termos da diagonal de A e das subdiagonais de A e L
        
        # Laço para o vetor que auxiliará nos calculos dos termos do vetor x em função dos termos do lado direito do sistema
        
        Raux[0]=b[0]   
        for i in range(1,N-1):
            Raux[i]=b[i]-(L[i]*Raux[i-1])

        # Laço para cálculo do vetor x que é solução do sistema em função dos termos da matriz A decomposta e do lado direito do sistema

        x[N-2]=Raux[N-2]/D[N-2]   
        for i in range(N-3,-1,-1):
            x[i]=(Raux[i]-(x[i+1]*asd[i+1]))/D[i]
            
        print (D)
        print (L)
        #print (Raux)
        print (x)