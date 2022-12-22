# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:36:40 2020

@author: Gabriel Valverde Zanata da Silva and Renata Cristina Pétta
"""




import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

from mpl_toolkits.mplot3d import Axes3D


W = int(input("Qual tarefa deseja rodar (1 ou 2)? "))       #Definidor de tarefa
W2 = int(input("Qual item deseja rodar (a=1, b=2 e c=3)? ")) #Definidor de item

# Inputs e parâmetros comuns a todos os itens
T = 1                                           #Intervalo de tempo (em segundos)
N = int(input("Digite o valor de N: "))        #Número de seções da barra a serem analisadas
Lbd = float(input("Digite o valor de Lbd: "))  #Relação de grandeza etre N e M
M = int((T*N**2)/Lbd)                           #Numero de instantes a serem analisados no intervalo
U = np.zeros((11,N+1),dtype=float)              #Matriz para armazenamento e plotagem dos dados
Unew = np.zeros(N+1,dtype=float)                #Vetor auxiliar para evolução temporal
Uold = np.zeros(N+1,dtype=float)                #Vetor auxiliar para evolução temporal
e = np.zeros((11,N+1),dtype=float)              #Matriz de erro entre a solução numérica e a exata para cada seção da barra em cada instante
tr = np.zeros(N+1, dtype=float)                 #Vetor de erro de truncamento para o item 1a
dt = T/M                                        #Tamanho do incremento temporal a cada instante   
dx = 1/N                                        #Distância entre cada seção da barra

#Verificação visual dos parâmetros de entrada
print("N =",N)
print("M =",M)
print("Lbd =",Lbd)


#Parâmetros gráficos
EixoX = np.linspace(0,1,11)                #Coordenadas do eixo X do gráfico
EixoY = np.linspace(0,1,N+1)               #Coordenadas do eixo Y do gráfico
#np.shape(EixoY)                            #Verificação do tamanho do array
#np.shape(EixoX)                            #Verificação do tamanho do array

X, Y = np.meshgrid(EixoY, EixoX)           #Criação do plano cartesiano base do gráfico 3D
#np.shape(X)                                #Verificação do tamanho do array
#np.shape(Y)                                #Verificação do tamanho do array
X = np.reshape(X,(11,N+1))                 #Matriz transposta de X (Xmxn => Xnxm) para que X seja uma matriz de tamanho (m+1)x(n+1), tal como a matriz U.
Y = np.reshape(Y,(11,N+1))                 #Matriz transposta de Y (Ymxn => Ynxm) para que Y seja uma matriz de tamanho (m+1)x(n+1), tal como a matriz U.
#np.shape(X)                                #Verificação do tamanho do array
#np.shape(Y)

################################### TAREFA 1 ##################################

if W == 1:
    if W2 == 1:
        
                               #### ITEM A ####

        for i in range(N+1):            #Laço para o instante inicial (t=0)
            x=i*dx                      #Local da barra a ser analisado
            U[0,i]=(x**2)*(1-x)**2      #temperatura inicial ao longo da barra
        
        #FRONTEIRAS X=0 E X=N
        U[:,0]=0
        U[:,N]=0
            
        for k in range(M+1): #Laço temporal
            t=k*dt  #Instante atual
            
            if k==0:
                Uold = U[0,:].copy()    #Definindo o vetor auxiliar inicial
                 
            for i in range(1,N):        #Laço espacial
                x=i*dx                  #Local da barra a ser analisado
                Ftx = (10*np.cos(10*t)*(x**2)*(1-x)**2)-(1+np.sin(10*t))*(12*x**2-12*x+2)   #Equação da fonte de calor
               
                #TRECHOS INTERIORES DA BARRA
                if k<M:
                    Unew[i]=Uold[i]+dt*(((Uold[i-1]-2*Uold[i]+Uold[i+1])/dx**2)+Ftx)
            
            #Montagem da matriz de dados de 0.1 em 0.1 s
            pos = int(t*10)+1        
            if pos == 1 or pos == 2 or pos == 3 or pos == 4 or pos == 5 or pos == 6 or pos == 7 or pos == 8 or pos == 9 or pos == 10:
                U[pos,:] = Unew
                
                #Cálculo de erros
                for i in range(N+1):
                    x=i*dx
                    UtxExata = (1+np.sin(10*t))*(x**2)*(1-x)**2     #Solução exata do problema (Usado para cálculo do erro)
                    e[pos,i] = abs(U[pos,i]-UtxExata)   #Erro 
                    
            if t+dt == T:               #Para que o erro de truncamento seja dado no instante T
                #Erro de truncamento 
                for i in range(1,N):
                    x=i*dx
                    Ftx = (10*np.cos(10*t)*(x**2)*(1-x)**2)-(1+np.sin(10*t))*(12*x**2-12*x+2)
                    tr[i] = ((Unew[i]-Uold[i])/dt)-((Uold[i-1]-2*Uold[i]+Uold[i+1])/dx**2)-Ftx
                                    
            Uold = Unew.copy()          #Substituição do vetor velho pelo novo
            
 
                  
        trmax = max(abs(tr))            #Obtenção do erro máximo de truncamento em módulo
        print("Erro de truncamento: ", trmax)        

        
    elif W2 == 2:

                                  #### ITEM B ####
        

        for i in range(N+1):        #Laço para o instante inicial (t=0)
            x=i*dx                  #Local da barra a ser analisado
            U[0,i]= np.exp(-x)      #Temperatura inicial ao longo da barra
        
        for k in range(M+1):        #Laço temporal
            t=k*dt                  #Instante atual
            
            #FRONTEIRAS X=0 E X=N
            Unew[0] = np.exp(t)
            Unew[N] = np.exp(t-1)*np.cos(5*t)
            
            if k==0:
                Uold = U[0,:].copy()    #Definindo o vetor auxiliar inicial            
                       
            for i in range(1,N):    #Laço espacial
                x=i*dx              #Local da barra a ser analisado
                Ftx = np.exp(t-x)*((np.cos(5*x*t)-5*x*np.sin(5*t*x))-((1-25*(t**2))*np.cos(5*x*t)+10*t*np.sin(5*x*t)))    #Equação da fonte de calor
                                    
                #TRECHOS INTERIORES DA BARRA
                if k<M :
                    Unew[i]=Uold[i]+dt*(((Uold[i-1]-2*Uold[i]+Uold[i+1])/dx**2)+Ftx)
                             
            #Montagem da matriz de dados de 0.1 em 0.1 s
            pos = int(t*10)+1      
            if pos == 1 or pos == 2 or pos == 3 or pos == 4 or pos == 5 or pos == 6 or pos == 7 or pos == 8 or pos == 9 or pos == 10:
                U[pos,:] = Unew
                
                #Cálculo de erros
                for i in range(N+1):
                    x=i*dx
                    UtxExata = np.exp(t-x)*np.cos(5*t*x)  #Solução exata do problema (Usado para cálculo do erro)
                    e[pos,i] = abs(U[pos,i]-UtxExata)   #Erro        
            
            Uold = Unew.copy()          #Substituição do vetor velho pelo novo

          
            
    elif W2 == 3:

                                #### ITEM C ####
        
        
        #FRONTEIRAS X=0 E X=N
        U[:,0]=0
        U[:,N]=0
        for k in range(M+1):        #Laço temporal
            t=k*dt                  #Instante atual
        
            for i in range(1,N):    #Laço espacial
                x=i*dx              #Local da barra a ser analisado
            
                rt = 10000*(1-2*(t**2)) #Função rt que determina a intensidade da fonte pontual 
                # Definindo a função gh que delimita a ação da fonte pontual
                p = 0.25
                if x>=(p-(dx/2)) and x<=(p+(dx/2)):
                    gh = 1/dx
                else:
                    gh = 0                    
                Ftx = rt*gh  #Comportamento da fonte pontual

                #TRECHOS INTERIORES DA BARRA
                if k<M:
                    Unew[i]=Uold[i]+dt*(((Uold[i-1]-2*Uold[i]+Uold[i+1])/dx**2)+Ftx)
            
            #Montagem da matriz de dados de 0.1 em 0.1 s
            pos = int(t*10)+1        
            if pos == 1 or pos == 2 or pos == 3 or pos == 4 or pos == 5 or pos == 6 or pos == 7 or pos == 8 or pos == 9 or pos == 10:
                U[pos,:] = Unew
                            
            Uold = Unew.copy()          #Substituição do vetor velho pelo novo






############################### TAREFA 2 ######################################

if W == 2:
    
    Fa = np.zeros(N-1,dtype=float)
    Fb = np.zeros(N-1,dtype=float)        
   
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
             
             for i in range(N+1):       #Laço para o instante inicial (T=0)
                x=i*dx                  #Local da barra
                U[0,i]=(x**2)*(1-x)**2  # temperatura inicial ao longo da barra
                
             for k in range(M+1):       #Laço temporal
                t=k*dt                  #Instante atual
                tf = t+dt
                
                if k==0:
                    Uold = U[0,:].copy()    #Definindo o vetor auxiliar inicial 
                
                for q in range(1,N):
                    x=q*dx
                    Fb[q-1]=(10*np.cos(10*tf)*(x**2)*(1-x)**2)-(1+np.sin(10*tf))*(12*x**2-12*x+2)
  
                for i in range(N-1):    #Laço espacial
                    x=(i+1)*dx          #Local da barra a ser analisado
                              
                    #TRECHOS INTERIORES DA BARRA
                    if k<M:
                        b[i]=Uold[i+1]+dt*Fb[i]   
                    
                # Laço para o vetor que auxiliará nos calculos dos termos do vetor x em função dos termos do lado direito do sistema     
                Raux[0]=b[0]   
                for i in range(1,N-1):
                    Raux[i]=b[i]-(L[i]*Raux[i-1])
        
                # Laço para cálculo do vetor x que é solução do sistema em função dos termos da matriz A decomposta e do lado direito do sistema
                if k<M:
                    Unew[N-1]=Raux[N-2]/D[N-2]   
                    for i in range(N-3,-1,-1):
                        Unew[i+1]=(Raux[i]-(Unew[i+2]*asd[i+1]))/D[i]                        
                    
                #Montagem da matriz de dados de 0.1 em 0.1 s
                pos = int(t*10)+1        
                if pos == 1 or pos == 2 or pos == 3 or pos == 4 or pos == 5 or pos == 6 or pos == 7 or pos == 8 or pos == 9 or pos == 10:
                    U[pos,:] = Unew
                
                    #Cálculo de erros
                    for i in range(N+1):
                        x=i*dx
                        UtxExata =(1+np.sin(10*t))*(x**2)*(1-x)**2  #Solução exata do problema (Usado para cálculo do erro)
                        e[pos,i] = abs(U[pos,i]-UtxExata)   #Erro        
            
                Uold = Unew.copy()          #Substituição do vetor velho pelo novo


                
                
        
                               ## Item B-b ##
            
        elif W3 == 2:

            
            for i in range(N+1):        #Laço para o instante inicial (T=0)
                x=i*dx                  #Local da barra
                U[0,i]= np.exp(-x)      # temperatura incial ao longo da barra (U0)

            for k in range(M+1):        #Laço temporal
                t=k*dt                  #Instante atual
                tf = t+dt
                    
                #FRONTEIRAS X=0 E X=N
                Unew[0] = np.exp(t)
                Unew[N] = np.exp(t-1)*np.cos(5*t)
                
                if k==0:
                    Uold = U[0,:].copy()    #Definindo o vetor auxiliar inicial 
                
                for q in range(1,N):
                    x=q*dx            
                    Fb[q-1] = np.exp(tf-x)*((np.cos(5*x*tf)-5*x*np.sin(5*tf*x))-((1-25*(tf**2))*np.cos(5*x*tf)+10*tf*np.sin(5*x*tf)))
            
                for i in range(N-1):    #Laço espacial
                    x=i*dx          #Local da barra a ser analisado          

                    #TRECHOS INTERIORES DA BARRA
                    if k<M:
                        
                        if i == 0:
                            b[i]=Uold[i+1]+dt*Fb[i]+Lbd*np.exp(t+dt) #A situação na fronteira x=0 varia com o tempo, por isso é necessário adicionar tal variação a cada novo instante t.
                        
                        elif i == N-2:
                            b[i]=Uold[i+1]+dt*Fb[i]+Lbd*np.exp(t+dt-1)*np.cos(5*(t+dt)) #A situação na fronteira x=1 varia com o tempo, por isso é necessário adicionar tal variação a cada novo instante t.
                        
                        else:
                            b[i]=Uold[i+1]+dt*Fb[i]
            
                # Laço para o vetor que auxiliará nos calculos dos termos do vetor x em função dos termos do lado direito do sistema
                Raux[0]=b[0]   
                for i in range(1,N-1):
                    Raux[i]=b[i]-(L[i]*Raux[i-1])
        
                # Laço para cálculo do vetor x que é solução do sistema em função dos termos da matriz A decomposta e do lado direito do sistema
                if k<M:
                    Unew[N-1]=Raux[N-2]/D[N-2]   
                    for i in range(N-3,-1,-1):
                        Unew[i+1]=(Raux[i]-(Unew[i+2]*asd[i+1]))/D[i]   
                           
                #Montagem da matriz de dados de 0.1 em 0.1 s
                pos = int(t*10)+1        
                if pos == 1 or pos == 2 or pos == 3 or pos == 4 or pos == 5 or pos == 6 or pos == 7 or pos == 8 or pos == 9 or pos == 10:
                    U[pos,:] = Unew
                    #Cálculo de erros
                    for i in range(N+1):
                        x=i*dx
                        UtxExata = np.exp(t-x)*np.cos(5*t*x)   #Solução exata do problema (Usado para cálculo do erro)
                        e[pos,i] = abs(U[pos,i]-UtxExata)   #Erro                           
            
                Uold = Unew.copy()          #Substituição do vetor velho pelo novo
                   

            
            
                                 ## Item B-c ##
            
        elif W3 == 3:    
                            
            for k in range(M+1):        #Laço temporal
                t=k*dt                  #Instante atual
                tf = t+dt                
                
                if k==0:
                    Uold = U[0,:].copy()    #Definindo o vetor auxiliar inicial 
                                  
                for q in range(N-1):    #Laço espacial
                    x=q*dx          #Usa-se q+1 para que se construa uma matriz n-1 com apenas o valores de posições interiores da barra
                    
                    rt = 10000*(1-2*(tf**2)) #Função rt que determina a intensidade da fonte pontual
                    # Definindo a função gh que delimita a ação da fonte pontual
                    s = 0.25
                    if x>=(s-(dx/2)) and x<=(s+(dx/2)):
                        gh = 1/dx
                    else:
                        gh = 0
                
                    Fb[q-1] = rt*gh      #Comportamento da fonte pontual 
                
                for i in range(1,N):    #Laço espacial
                    x=i*dx              #Local da barra a ser analisado

                    #TRECHOS INTERIORES DA BARRA
                    if k<M:
                        b[i-1]=Uold[i]+dt*Fb[i-1]
                        
                # Laço para o vetor que auxiliará nos calculos dos termos do vetor x em função dos termos do lado direito do sistema
                Raux[0]=b[0]   
                for i in range(1,N-1):
                    Raux[i]=b[i]-(L[i]*Raux[i-1])
        
                # Laço para cálculo do vetor x que é solução do sistema em função dos termos da matriz A decomposta e do lado direito do sistema
                if k<M:
                    Unew[N-1]=Raux[N-2]/D[N-2]   
                    for i in range(N-3,-1,-1):
                        Unew[i+1]=(Raux[i]-(Unew[i+2]*asd[i+1]))/D[i]   
                           
                #Montagem da matriz de dados de 0.1 em 0.1 s
                pos = int(t*10)+1        
                if pos == 1 or pos == 2 or pos == 3 or pos == 4 or pos == 5 or pos == 6 or pos == 7 or pos == 8 or pos == 9 or pos == 10:
                    U[pos,:] = Unew   
            
                Uold = Unew.copy()          #Substituição do vetor velho pelo novo
 




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
                            
             for i in range(N+1):       #Laço para o instante inicial (T=0)
                x=i*dx                  #Local da barra
                U[0,i]=(x**2)*(1-x)**2  # temperatura inicial ao longo da barra
   
             for k in range(M+1):       #Laço temporal
                t=k*dt                  #Instante atual
                tf=t+dt 
            
                if k==0:
                    Uold = U[0,:].copy()    #Definindo o vetor auxiliar inicial 

                for q in range(1,N):
                    x=q*dx
                    Fa[q-1]=(10*np.cos(10*t)*(x**2)*(1-x)**2)-(1+np.sin(10*t))*(12*x**2-12*x+2)
                    Fb[q-1]=(10*np.cos(10*tf)*(x**2)*(1-x)**2)-(1+np.sin(10*tf))*(12*x**2-12*x+2)

                for i in range(N-1):    #Laço espacial
                    x=(i+1)*dx          #Local da barra a ser analisado
            
                    #TRECHOS INTERIORES DA BARRA
                    if k<M:
                        b[i]=Uold[i+1]+(dt/2)*(Fa[i]+Fb[i])+(Lbd/2)*(Uold[i]-2*Uold[i+1]+Uold[i+2])

                # Laço para o vetor que auxiliará nos calculos dos termos do vetor x em função dos termos do lado direito do sistema
                Raux[0]=b[0]   
                for i in range(1,N-1):
                    Raux[i]=b[i]-(L[i]*Raux[i-1])
        
                # Laço para cálculo do vetor x que é solução do sistema em função dos termos da matriz A decomposta e do lado direito do sistema
                if k<M:
                    Unew[N-1]=Raux[N-2]/D[N-2]   
                    for i in range(N-3,-1,-1):
                        Unew[i+1]=(Raux[i]-(Unew[i+2]*asd[i+1]))/D[i]   
                           
                #Montagem da matriz de dados de 0.1 em 0.1 s
                pos = int(t*10)+1        
                if pos == 1 or pos == 2 or pos == 3 or pos == 4 or pos == 5 or pos == 6 or pos == 7 or pos == 8 or pos == 9 or pos == 10:
                    U[pos,:] = Unew
                    #Cálculo de erros
                    for i in range(N+1):
                        x=i*dx
                        UtxExata = (1+np.sin(10*t))*(x**2)*(1-x)**2   #Solução exata do problema (Usado para cálculo do erro)
                        e[pos,i] = abs(U[pos,i]-UtxExata)   #Erro                           
            
                Uold = Unew.copy()          #Substituição do vetor velho pelo novo

                
                
        
                               ## Item C-b ##
            
        elif W3 == 2:
            
            for i in range(N+1):        #Laço para o instante inicial (T=0)
                x=i*dx                  #Local da barra
                U[0,i]= np.exp(-x)      # temperatura incial ao longo da barra (U0)
            
            
            for k in range(M+1):        #Laço temporal
                t=k*dt                  #Instante atual
                tf=t+dt
            
                #FRONTEIRAS X=0 E X=N
                Unew[0] = np.exp(t)
                Unew[N] = np.exp(t-1)*np.cos(5*t)            
            
                if k==0:
                    Uold = U[0,:].copy()    #Definindo o vetor auxiliar inicial 
                
                for q in range(1,N):
                    x=q*dx 
                    Fa[q-1] = np.exp(t-x)*((np.cos(5*x*t)-5*x*np.sin(5*t*x))-((1-25*(t**2))*np.cos(5*x*t)+10*t*np.sin(5*x*t)))
                    Fb[q-1] = np.exp(tf-x)*((np.cos(5*x*tf)-5*x*np.sin(5*tf*x))-((1-25*(tf**2))*np.cos(5*x*tf)+10*tf*np.sin(5*x*tf)))
                          
                for i in range(N-1):    #Laço espacial
                    x=i*dx          #Local da barra a ser analisado          
                    UtxExata = np.exp(t-x)*np.cos(5*t*x)  
      
                    #TRECHOS INTERIORES DA BARRA
                    if k<M:
                        
                        if i == 0:
                            b[i]=Uold[i+1]+(dt/2)*(Fa[i]+Fb[i])+(Lbd/2)*(Uold[i]-2*Uold[i+1]+Uold[i+2])+(Lbd/2)*np.exp(t+dt) #A situação na fronteira x=0 varia com o tempo, por isso é necessário adicionar tal variação a cada novo instante t.
                        
                        elif i == N-2:
                            b[i]=Uold[i+1]+(dt/2)*(Fa[i]+Fb[i])+(Lbd/2)*(Uold[i]-2*Uold[i+1]+Uold[i+2])+(Lbd/2)*np.exp(t+dt-1)*np.cos(5*(t+dt)) #A situação na fronteira x=1 varia com o tempo, por isso é necessário adicionar tal variação a cada novo instante t.
                        
                        else:
                            b[i]=Uold[i+1]+(dt/2)*(Fa[i]+Fb[i])+(Lbd/2)*(Uold[i]-2*Uold[i+1]+Uold[i+2])
                
                # Laço para o vetor que auxiliará nos calculos dos termos do vetor x em função dos termos do lado direito do sistema
                Raux[0]=b[0]   
                for i in range(1,N-1):
                    Raux[i]=b[i]-(L[i]*Raux[i-1])
        
                # Laço para cálculo do vetor x que é solução do sistema em função dos termos da matriz A decomposta e do lado direito do sistema
                if k<M:
                    Unew[N-1]=Raux[N-2]/D[N-2]   
                    for i in range(N-3,-1,-1):
                        Unew[i+1]=(Raux[i]-(Unew[i+2]*asd[i+1]))/D[i]   
                           
                #Montagem da matriz de dados de 0.1 em 0.1 s
                pos = int(t*10)+1        
                if pos == 1 or pos == 2 or pos == 3 or pos == 4 or pos == 5 or pos == 6 or pos == 7 or pos == 8 or pos == 9 or pos == 10:
                    U[pos,:] = Unew
                    #Cálculo de erros
                    for i in range(N+1):
                        x=i*dx
                        UtxExata = np.exp(t-x)*np.cos(5*t*x)   #Solução exata do problema (Usado para cálculo do erro)
                        e[pos,i] = abs(U[pos,i]-UtxExata)   #Erro                           
            
                Uold = Unew.copy()          #Substituição do vetor velho pelo novo
        
            
            
                                 ## Item C-c ##
            
        elif W3 == 3:    
            
       
            
            for k in range(M+1):        #Laço temporal
                t=k*dt                  #Instante atual
                tf = t+dt                
                
                if k==0:
                    Uold = U[0,:].copy()    #Definindo o vetor auxiliar inicial 
                                  
                for q in range(N-1):    #Laço espacial
                    x=q*dx          #Usa-se q+1 para que se construa uma matriz n-1 com apenas o valores de posições interiores da barra
                    
                    rta = 10000*(1-2*(t**2)) #Função rt que determina a intensidade da fonte pontual no instante atual
                    rtb = 10000*(1-2*(tf**2)) #Função rt que determina a intensidade da fonte pontual no instante posterior
                    # Definindo a função gh que delimita a ação da fonte pontual
                    s = 0.25
                    if x>=(s-(dx/2)) and x<=(s+(dx/2)):
                        gh = 1/dx
                    else:
                        gh = 0
                        
                    Fa[q-1] = rta*gh      #Comportamento da fonte pontual
                    Fb[q-1] = rtb*gh      #Comportamento da fonte pontual             
            
                for i in range(1,N):    #Laço espacial
                    x=i*dx              #Local da barra a ser analisado

                    #TRECHOS INTERIORES DA BARRA
                    if k<M:
                        b[i-1]=Uold[i]+(dt/2)*(Fa[i-1]+Fb[i-1])+(Lbd/2)*(Uold[i-1]-2*Uold[i]+Uold[i+1])
                        
                # Laço para o vetor que auxiliará nos calculos dos termos do vetor x em função dos termos do lado direito do sistema
                Raux[0]=b[0]   
                for i in range(1,N-1):
                    Raux[i]=b[i]-(L[i]*Raux[i-1])
        
                # Laço para cálculo do vetor x que é solução do sistema em função dos termos da matriz A decomposta e do lado direito do sistema
                if k<M:
                    Unew[N-1]=Raux[N-2]/D[N-2]   
                    for i in range(N-3,-1,-1):
                        Unew[i+1]=(Raux[i]-(Unew[i+2]*asd[i+1]))/D[i]   
                           
                #Montagem da matriz de dados de 0.1 em 0.1 s
                pos = int(t*10)+1        
                if pos == 1 or pos == 2 or pos == 3 or pos == 4 or pos == 5 or pos == 6 or pos == 7 or pos == 8 or pos == 9 or pos == 10:
                    U[pos,:] = Unew   
            
                Uold = Unew.copy()          #Substituição do vetor velho pelo novo
 
                       

#Apresentação dos dados numéricos 
if W == 1 and W2 != 3:
    emax = np.max(e)                        #Maior erro obtido em relação a solução exata
    print ("Erro máximo: ", emax)
    print ("Erros no instante T: ", e[10,:])
if W == 2 and W2 != 1 and W3 != 3:
    emax = np.max(e)                        #Maior erro obtido em relação a solução exata
    print ("Erro máximo: ", emax)
    print ("Erros no instante T: ", e[10,:])


if W == 1 or W == 2 and W2 != 1:
    print("Matriz de temperaturas (U):")
    print(U)
    
    
    #Plotagem de gráficos 3D
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    surf = ax.plot_surface(Y, X, U, cmap=cm.coolwarm, linewidth=1, antialiased=True)
    plt.title("Distribuição de temperatura (N = %d e λ = %.2f): " % (N,Lbd))
    ax.set_xlabel('Tempo')
    ax.set_ylabel('Local da barra')
    ax.set_zlabel('Temperatura')
    fig.colorbar(surf, shrink=0.7, aspect=10)
    plt.show()
        
        