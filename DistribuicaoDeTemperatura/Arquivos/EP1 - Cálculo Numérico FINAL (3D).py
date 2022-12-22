# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:36:40 2020

@author: Gabriel Valverde Zanata da Silva
"""
import IPython
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')





W = int(input("Qual tarefa deseja rodar (1 ou 2)? "))
W2 = int(input("Qual item deseja rodar (a=1, b=2 e c=3)? "))

# Inputs e parâmetros comuns a todos os itens
T = 1                                           #Intervalo de tempo (em segundos)
N = int(input("Digite um valor de N: "))        #Número de seções da barra a serem analisadas
Lbd = float(input("Digite um valor de Lbd: "))  #Relação de grandeza etre N e M
M = int((T*N**2)/Lbd)                           #Numero de instantes a serem analisados no intervalo
U = np.zeros((M+1,N+1),dtype=float)             #Matriz de temperatura para cada seção da barra em cada instante
e = np.zeros((M+1,N+1), dtype=float)            #Matriz de erro entre a solução numérica e a exata para cada seção da barra em cada instante
dt = T/M                                        #Tamanho do incremento temporal a cada instante   
dx = 1/N                                        #Distância entre cada seção da barra

#Verificação visual dos parâmetros de entrada
print("N =",N)
print("M =",M)
print("Lbd =",Lbd)


#Parâmetros gráficos
EixoX = np.linspace(0,1,M+1)                #Coordenadas do eixo X do gráfico
EixoY = np.linspace(0,1,N+1)                #Coordenadas do eixo Y do gráfico
np.shape(EixoY)                            #Verificação do tamanho do array
np.shape(EixoX)                            #Verificação do tamanho do array

X, Y = np.meshgrid(EixoY, EixoX)            #Criação do plano cartesiano base do gráfico 3D
np.shape(X)                                #Verificação do tamanho do array
np.shape(Y)                                #Verificação do tamanho do array
X = np.reshape(X,(M+1,N+1))                 #Matriz transposta de X (Xmxn => Xnxm) para que X seja uma matriz de tamanho (m+1)x(n+1), tal como a matriz U.
Y = np.reshape(Y,(M+1,N+1))                 #Matriz transposta de Y (Ymxn => Ynxm) para que Y seja uma matriz de tamanho (m+1)x(n+1), tal como a matriz U.
np.shape(X)                                #Verificação do tamanho do array
np.shape(Y)

################################### TAREFA 1 ##################################

if W == 1:
    if W2 == 1:
        
                               #### ITEM A ####

        for i in range(N+1):            #Laço para o instante inicial (t=0)
            x=i*dx                      #Local da barra a ser analisado
            U[0,i]=(x**2)*(1-x)**2      #temperatura inicial ao longo da barra
            
        for k in range(M+1): #Laço temporal
            t=k*dt  #Instante atual
        
            for i in range(N+1):        #Laço espacial
                x=i*dx                  #Local da barra a ser analisado
                Ftx = (10*np.cos(10*t)*(x**2)*(1-x)**2)-(1+np.sin(10*t))*(12*x**2-12*x+2)   #Equação da fonte de calor
                UtxExata = (1+np.sin(10*t))*(x**2)*(1-x)**2     #Solução exata do problema (Usado para cálculo do erro)
                    
                #FRONTEIRAS X=0 E X=N
                if i==0 or i==N:
                    U[k,i]=0
                          
                #TRECHOS INTERIORES DA BARRA
                elif k<M:
                    U[k+1,i]=U[k,i]+dt*(((U[k,i-1]-2*U[k,i]+U[k,i+1])/dx**2)+Ftx)
                e[k,i]=abs(U[k,i]-UtxExata)     
                    
                

        
    elif W2 == 2:

                                  #### ITEM B ####
        

        for i in range(N+1):        #Laço para o instante inicial (t=0)
            x=i*dx                  #Local da barra a ser analisado
            U[0,i]= np.exp(-x)      #Temperatura inicial ao longo da barra
        
        #Laço para incremento da temperatura a cada instante (deve ser feito antes, pois as temperaturas interiores dependem das temperaturas de fronteira)
        for k in range(M+1):        #Laço temporal
            t=k*dt                  #Instante atual            
            U[k,0] = np.exp(t)
            U[k,N] = np.exp(t-1)*np.cos(5*t)
            
        for k in range(M+1):        #Laço temporal
            t=k*dt                  #Instante atual
        
            for i in range(1,N):    #Laço espacial
                x=i*dx              #Local da barra a ser analisado
                Ftx = np.exp(t-x)*((np.cos(5*x*t)-5*x*np.sin(5*t*x))-((1-25*(t**2))*np.cos(5*x*t)+10*t*np.sin(5*x*t)))    #Equação da fonte de calor
                UtxExata = np.exp(t-x)*np.cos(5*t*x)  #Solução exata do problema (Usado para cálculo do erro)
                    
                #TRECHOS INTERIORES DA BARRA
                if k<M :
                    U[k+1,i]=U[k,i]+dt*(((U[k,i-1]-2*U[k,i]+U[k,i+1])/dx**2)+Ftx)
                e[k,i]=abs(U[k,i]-UtxExata)    
                    


          
            
    elif W2 == 3:

                                #### ITEM C ####
        

        for k in range(M+1):        #Laço temporal
            t=k*dt                  #Instante atual
        
            for i in range(N+1):    #Laço espacial
                x=i*dx              #Local da barra a ser analisado
            
                rt = 10000*(1-2*(t**2)) #Função rt que determina a intensidade da fonte pontual 
                # Definindo a função gh que delimita a ação da fonte pontual
                p = 0.25
                if x>=(p-(dx/2)) and x<=(p+(dx/2)):
                    gh = 1/dx
                else:
                    gh = 0                    
                Ftx = rt*gh  #Comportamento da fonte pontual
                  
                    
                #FRONTEIRAS X=0 E X=N
                if i==0 or i==N:
                    U[k,i] = 0
                

                #TRECHOS INTERIORES DA BARRA
                elif k<M:
                    U[k+1,i]=U[k,i]+dt*(((U[k,i-1]-2*U[k,i]+U[k,i+1])/dx**2)+Ftx)
                







############################### TAREFA 2 ######################################

if W == 2:
    
    F = np.zeros((M+1,N-1),dtype=float)        
   
    #Vetores auxiliares e de output
    D = np.zeros(N-1,dtype=float)   # Vetor representante da matriz diagonal
    L = np.zeros(N-1,dtype=float)   # Vetor representante da matriz subdiagonal 
    Raux = np.zeros(N-1,dtype=float) # Vetor resultante auxiliar, usado para calcular o vetor x 
    xsol = np.zeros(N-1,dtype=float) # Vetor solução do sistema        
    b = np.zeros(N-1,dtype=float)   # Vetor do lado direito do sistema 
    
    
    
    if W2 == 1:
        
                           #### ITEM A ####

        #Vetores de Input
        ad = np.full(N-1,1+2*Lbd)       # Vetor com os valores da diagonal da matriz a ser decomposta
        asd = np.full(N-1,-Lbd)         # Vetor com os valores da subdiagonal da matriz a ser decomposta
        asd[0]=0                        # Adequando N-2 termos num vetor de tamnho N-1
        #a = np.zeros((N-1,N-1),dtype=float) # Matriz A a ser decomposta (apenas para verificação visual).     
        
        for i in range(N-1):
            b[i] = int(input("Digite um valor para o termo do vetor do lado direito do sistema: "))
            
               
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

        xsol[N-2]=Raux[N-2]/D[N-2]   
        for i in range(N-3,-1,-1):
            xsol[i]=(Raux[i]-(xsol[i+1]*asd[i+1]))/D[i]
            
        print ("Vetor D: ", D)
        print ("Vetor L: ", L)
        #print (Raux)
        print ("Vetor X (solução): ", xsol)
        
        
        
        
        
        
    if W2 == 2:
        
                               #### ITEM B ####
        

        W3 = int(input("Qual situação do item 1 deseja rodar (a=1, b=2 e c=3)? "))
        
        #Vetores de Input
        ad = np.full(N-1,1+2*Lbd)       # Vetor com os valores da diagonal da matriz a ser decomposta
        asd = np.full(N-1,-Lbd)         # Vetor com os valores da subdiagonal da matriz a ser decomposta
        asd[0]=0                        # Adequando N-2 termos num vetor de tamnho N-1            
        
        
        # Laço para decomposição de A em LDLt
                
        D[0]=ad[0]                      # Primeiro termo da diagonal D é igual ao primeiro termo da original A
        for i in range(1,N-1):
            L[i]=asd[i]/D[i-1]          # Termos de L em função dos termos da subdiagonal de A e da matriz diagonal D
            D[i]=ad[i]-(L[i]*asd[i])    # Termos de D em função dos termos da diagonal de A e das subdiagonais de A e L
                                
            
            
                               ## Item B-a ##

        if W3 == 1:
            
             #Laço para definição das condições de fronteira e construção da matriz da fonte Ftx
             for p in range(M+1):
                t=p*dt
                for q in range(N-1):
                    x=(q+1)*dx
                    F[p,q]=(10*np.cos(10*t)*(x**2)*(1-x)**2)-(1+np.sin(10*t))*(12*x**2-12*x+2)
             #print (F)                 #Verificação visual da matriz da fonte Ftx
             
             for i in range(N+1):       #Laço para o instante inicial (T=0)
                x=i*dx                  #Local da barra
                U[0,i]=(x**2)*(1-x)**2  # temperatura incial ao longo da barra
                if i == 0 or i == N:
                    U[0,i]=0
                
             for k in range(M+1):       #Laço temporal
                t=k*dt                  #Instante atual
            
                for i in range(N-1):    #Laço espacial
                    x=(i+1)*dx          #Local da barra a ser analisado
                    UtxExata = (1+np.sin(10*t))*(x**2)*(1-x)**2
                              
                    #TRECHOS INTERIORES DA BARRA
                    if k<M:
                        b[i]=U[k,i+1]+dt*F[k+1,i]
                    e[k,i]=abs(U[k,i+1]-UtxExata)    
                    
                # Laço para o vetor que auxiliará nos calculos dos termos do vetor x em função dos termos do lado direito do sistema
                
                Raux[0]=b[0]   
                for i in range(1,N-1):
                    Raux[i]=b[i]-(L[i]*Raux[i-1])
        
                # Laço para cálculo do vetor x que é solução do sistema em função dos termos da matriz A decomposta e do lado direito do sistema
                if k<M:
                    U[k+1,N-1]=Raux[N-2]/D[N-2]   
                    for i in range(N-3,-1,-1):
                        U[k+1,i+1]=(Raux[i]-(U[k+1,i+2]*asd[i+1]))/D[i]                        
                    

                
                
        
                               ## Item B-b ##
            
        elif W3 == 2:
            
            #Laço para definição das condições de fronteira e construção da matriz da fonte Ftx
            for p in range(M+1):
                t=p*dt
                
                #Condições de fronteira
                U[p,0] = np.exp(t)
                U[p,N] = np.exp(t-1)*np.cos(5*t)               
                
                for q in range(N-1):
                    x=(q+1)*dx            
                    F[p,q] = np.exp(t-x)*((np.cos(5*x*t)-5*x*np.sin(5*t*x))-((1-25*(t**2))*np.cos(5*x*t)+10*t*np.sin(5*x*t)))
            #print(F)
            
            for i in range(N+1):        #Laço para o instante inicial (T=0)
                x=i*dx                  #Local da barra
                U[0,i]= np.exp(-x)      # temperatura incial ao longo da barra (U0)
            
            for k in range(M+1):        #Laço temporal
                t=k*dt                  #Instante atual
            
                for i in range(N-1):    #Laço espacial
                    x=i*dx          #Local da barra a ser analisado          
                    UtxExata = np.exp(t-x)*np.cos(5*t*x)  

                    #TRECHOS INTERIORES DA BARRA
                    if k<M:
                        
                        if i == 0:
                            b[i]=U[k,i+1]+dt*F[k+1,i]+Lbd*np.exp(t+dt) #A situação na fronteira x=0 varia com o tempo, por isso é necessário adicionar tal variação a cada novo instante t.
                        
                        elif i == N-2:
                            b[i]=U[k,i+1]+dt*F[k+1,i]+Lbd*np.exp(t+dt-1)*np.cos(5*(t+dt)) #A situação na fronteira x=1 varia com o tempo, por isso é necessário adicionar tal variação a cada novo instante t.
                        
                        else:
                            b[i]=U[k,i+1]+dt*F[k+1,i]
                    e[k,i]=abs(U[k,i]-UtxExata) 
            
                # Laço para o vetor que auxiliará nos calculos dos termos do vetor x em função dos termos do lado direito do sistema
                
                Raux[0]=b[0]   
                for i in range(1,N-1):
                    Raux[i]=b[i]-(L[i]*Raux[i-1])
        
                # Laço para cálculo do vetor x que é solução do sistema em função dos termos da matriz A decomposta e do lado direito do sistema
                if k<M:
                    U[k+1,N-1]=Raux[N-2]/D[N-2]   
                    for i in range(N-3,-1,-1):
                        U[k+1,i+1]=(Raux[i]-(U[k+1,i+2]*asd[i+1]))/D[i] 
                           
                    

            
            
                                 ## Item B-c ##
            
        elif W3 == 3:    
            
            #Laço para definição das condições de fronteira e construção da matriz da fonte Ftx
            for p in range(M+1):        #Laço temporal
                t=p*dt
                U[p,0] = 0
                U[p,N] = 0                
                
                for q in range(N-1):    #Laço espacial
                    x=(q+1)*dx          #Usa-se q+1 para que se construa uma matriz n-1 com apenas o valores de posições interiores da barra
                    
                    rt = 10000*(1-2*(t**2)) #Função rt que determina a intensidade da fonte pontual
                    # Definindo a função gh que delimita a ação da fonte pontual
                    s = 0.25
                    if x>=(s-(dx/2)) and x<=(s+(dx/2)):
                        gh = 1/dx
                    else:
                        gh = 0
                
                    F[p,q] = rt*gh      #Comportamento da fonte pontual        
            
            for k in range(M+1):        #Laço temporal
                t=k*dt                  #Instante atual
            
                for i in range(1,N):    #Laço espacial
                    x=i*dx              #Local da barra a ser analisado

                    #TRECHOS INTERIORES DA BARRA
                    if k<M:
                        b[i-1]=U[k,i]+dt*F[k+1,i-1]
                        
                # Laço para o vetor que auxiliará nos calculos dos termos do vetor x em função dos termos do lado direito do sistema   
                Raux[0]=b[0]   
                for i in range(1,N-1):
                    Raux[i]=b[i]-(L[i]*Raux[i-1])
        
                # Laço para cálculo do vetor x que é solução do sistema em função dos termos da matriz A decomposta e do lado direito do sistema
                if k<M:
                    U[k+1,N-1]=Raux[N-2]/D[N-2]   
                    for i in range(N-3,-1,-1):
                        U[k+1,i+1]=(Raux[i]-(U[k+1,i+2]*asd[i+1]))/D[i]                         





    if W2 == 3:
        
                               #### ITEM C ####
        

        W3 = int(input("Qual situação do item 1 deseja rodar (a=1, b=2 e c=3)? "))

        ad = np.full(N-1,1+Lbd)       # Vetor com os valores da diagonal da matriz a ser decomposta
        asd = np.full(N-1,-Lbd/2)         # Vetor com os valores da subdiagonal da matriz a ser decomposta
        asd[0]=0                        # Adequando N-2 termos num vetor de tamnho N-1
        
                
        
        # Laço para decomposição de A em LDLt
        D[0]=ad[0]                      # Primeiro termo da diagonal D é igual ao primeiro termo da original A        
        for i in range(1,N-1):
            L[i]=asd[i]/D[i-1]          # Termos de L em função dos termos da subdiagonal de A e da matriz diagonal D
            D[i]=ad[i]-(L[i]*asd[i])    # Termos de D em função dos termos da diagonal de A e das subdiagonais de A e L
                                
            
            
                               ## Item C-a ##

        if W3 == 1:
            
             #Laço para definição das condições de fronteira e construção da matriz da fonte Ftx
             for p in range(M+1):
                t=p*dt
                for q in range(N-1):
                    x=(q+1)*dx
                    F[p,q]=(10*np.cos(10*t)*(x**2)*(1-x)**2)-(1+np.sin(10*t))*(12*x**2-12*x+2)
             #print (F)                 #Verificação visual da matriz da fonte Ftx
             
             for i in range(N+1):       #Laço para o instante inicial (T=0)
                x=i*dx                  #Local da barra
                U[0,i]=(x**2)*(1-x)**2  # temperatura incial ao longo da barra
                if i == 0 or i == N:
                    U[0,i]=0
                
             for k in range(M+1):       #Laço temporal
                t=k*dt                  #Instante atual
            
                for i in range(N-1):    #Laço espacial
                    x=(i+1)*dx          #Local da barra a ser analisado
                    UtxExata = (1+np.sin(10*t))*(x**2)*(1-x)**2
                              
                    #TRECHOS INTERIORES DA BARRA
                    if k<M:
                        b[i]=U[k,i+1]+(dt/2)*(F[k,i]+F[k+1,i])+(Lbd/2)*(U[k,i]-2*U[k,i+1]+U[k,i+2])
                    e[k,i]=abs(U[k,i+1]-UtxExata)    
                    
                # Laço para o vetor que auxiliará nos calculos dos termos do vetor x em função dos termos do lado direito do sistema
                
                Raux[0]=b[0]   
                for i in range(1,N-1):
                    Raux[i]=b[i]-(L[i]*Raux[i-1])
        
                # Laço para cálculo do vetor x que é solução do sistema em função dos termos da matriz A decomposta e do lado direito do sistema
                if k<M:
                    U[k+1,N-1]=Raux[N-2]/D[N-2]   
                    for i in range(N-3,-1,-1):
                        U[k+1,i+1]=(Raux[i]-(U[k+1,i+2]*asd[i+1]))/D[i]                        
                    

                
                
        
                               ## Item C-b ##
            
        elif W3 == 2:
            
            #Laço para definição das condições de fronteira e construção da matriz da fonte Ftx
            for p in range(M+1):
                t=p*dt
                
                #Condições de fronteira
                U[p,0] = np.exp(t)
                U[p,N] = np.exp(t-1)*np.cos(5*t)               
                
                for q in range(N-1):
                    x=(q+1)*dx            
                    F[p,q] = np.exp(t-x)*((np.cos(5*x*t)-5*x*np.sin(5*t*x))-((1-25*(t**2))*np.cos(5*x*t)+10*t*np.sin(5*x*t)))
            #print(F)
            
            for i in range(N+1):        #Laço para o instante inicial (T=0)
                x=i*dx                  #Local da barra
                U[0,i]= np.exp(-x)      # temperatura incial ao longo da barra (U0)
            
            for k in range(M+1):        #Laço temporal
                t=k*dt                  #Instante atual
            
                for i in range(N-1):    #Laço espacial
                    x=i*dx          #Local da barra a ser analisado          
                    UtxExata = np.exp(t-x)*np.cos(5*t*x)  
                    
                   
                        
                    #TRECHOS INTERIORES DA BARRA
                    if k<M:
                        
                        if i == 0:
                            b[i]=U[k,i+1]+(dt/2)*(F[k,i]+F[k+1,i])+(Lbd/2)*(U[k,i]-2*U[k,i+1]+U[k,i+2])+(Lbd/2)*np.exp(t+dt) #A situação na fronteira x=0 varia com o tempo, por isso é necessário adicionar tal variação a cada novo instante t.
                        
                        elif i == N-2:
                            b[i]=b[i]=U[k,i+1]+(dt/2)*(F[k,i]+F[k+1,i])+(Lbd/2)*(U[k,i]-2*U[k,i+1]+U[k,i+2])+(Lbd/2)*np.exp(t+dt-1)*np.cos(5*(t+dt)) #A situação na fronteira x=1 varia com o tempo, por isso é necessário adicionar tal variação a cada novo instante t.
                        
                        else:
                            b[i]=U[k,i+1]+(dt/2)*(F[k,i]+F[k+1,i])+(Lbd/2)*(U[k,i]-2*U[k,i+1]+U[k,i+2])
                    e[k,i]=abs(U[k,i]-UtxExata)               
            
                # Laço para o vetor que auxiliará nos calculos dos termos do vetor x em função dos termos do lado direito do sistema
                
                Raux[0]=b[0]   
                for i in range(1,N-1):
                    Raux[i]=b[i]-(L[i]*Raux[i-1])
        
                # Laço para cálculo do vetor x que é solução do sistema em função dos termos da matriz A decomposta e do lado direito do sistema
                if k<M:
                    U[k+1,N-1]=Raux[N-2]/D[N-2]   
                    for i in range(N-3,-1,-1):
                        U[k+1,i+1]=(Raux[i]-(U[k+1,i+2]*asd[i+1]))/D[i] 
                           
        
            
            
                                 ## Item C-c ##
            
        elif W3 == 3:    
            
            #Laço para definição das condições de fronteira e construção da matriz da fonte Ftx
            for p in range(M+1):        #Laço temporal
                t=p*dt
                U[p,0] = 0
                U[p,N] = 0                
                
                for q in range(N-1):    #Laço espacial
                    x=(q+1)*dx          #Usa-se q+1 para que se construa uma matriz n-1 com apenas o valores de posições interiores da barra
                    
                    rt = 10000*(1-2*(t**2)) #Função rt que determina a intensidade da fonte pontual
                    # Definindo a função gh que delimita a ação da fonte pontual
                    s = 0.25
                    if x>=(s-(dx/2)) and x<=(s+(dx/2)):
                        gh = 1/dx
                    else:
                        gh = 0
                
                    F[p,q] = rt*gh      #Comportamento da fonte pontual        
            
            for k in range(M+1):        #Laço temporal
                t=k*dt                  #Instante atual
            
                for i in range(1,N):    #Laço espacial
                    x=i*dx              #Local da barra a ser analisado

                    #TRECHOS INTERIORES DA BARRA
                    if k<M:
                        b[i-1]=U[k,i]+(dt/2)*(F[k,i-1]+F[k+1,i-1])+(Lbd/2)*(U[k,i-1]-2*U[k,i]+U[k,i+1])
                        
                # Laço para o vetor que auxiliará nos calculos dos termos do vetor x em função dos termos do lado direito do sistema   
                Raux[0]=b[0]   
                for i in range(1,N-1):
                    Raux[i]=b[i]-(L[i]*Raux[i-1])
        
                # Laço para cálculo do vetor x que é solução do sistema em função dos termos da matriz A decomposta e do lado direito do sistema
                if k<M:
                    U[k+1,N-1]=Raux[N-2]/D[N-2]   
                    for i in range(N-3,-1,-1):
                        U[k+1,i+1]=(Raux[i]-(U[k+1,i+2]*asd[i+1]))/D[i]  
                        
                        
 
emax = np.max(e)                        #Maior erro obtido em relação a solução exata
print ("Erro: ", emax)
print("Matriz de temperaturas (U):")
print(U)

surf = ax.plot_surface(Y, X, U, cmap=cm.coolwarm, linewidth=1, antialiased=False)
plt.title("Distribuição de temperatura da barra")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel('Tempo')
ax.set_ylabel('Local da barra')
ax.set_zlabel('Temperatura')
fig.colorbar(surf, shrink=0.7, aspect=10)
plt.show()
        
        