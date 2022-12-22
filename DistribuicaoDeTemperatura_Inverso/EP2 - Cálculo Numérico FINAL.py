# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:36:40 2020

@author: Gabriel Valverde Zanata da Silva and Renata Cristina Pétta
"""

import numpy as np
import matplotlib.pyplot as plt
import random as random




W = int(input("Qual item deseja rodar (a=1, b=2, c=3 ou d=4)? ")) #Definidor de item

# Inputs e parâmetros comuns a todos os itens
T = 1                                           #Intervalo de tempo (em segundos)

if W == 1:
    nf = 1
    N = 128

elif W == 2:
    nf = 4
    N = 128    


elif W == 3 or W == 4:
    nf = 10
    N = int(input("Digite o valor de N: "))        #Número de seções da barra a serem analisadas


M = N                                           #Numero de instantes a serem analisados no intervalo

U = np.zeros((11,N+1),dtype=float)              #Matriz para cálculo das funções Uk através do métodos de Crank-Nicholson
Unew = np.zeros(N+1,dtype=float)                #Vetor auxiliar para evolução temporal
Uold = np.zeros(N+1,dtype=float)                #Vetor auxiliar para evolução temporal
Uk = np.zeros((nf,N-1),dtype=float)             #Matriz para armazenamento dos vetores Uk(T,x)
UT = np.ones(N-1,dtype=float)                   #Vetor de temperaturas no instante T ao longo da barra
UTx = np.ones(N-1,dtype=float)                  #Vetor de temperaturas no instante T ao longo da barra


A =  np.zeros((nf,nf),dtype=float)              #Matriz de produtos internos entre os vetores Uk para o MMQ
Xa = np.zeros(nf,dtype=float)                   #Vetor solução do MMQ que armazenará os valores das intensidades ak
B =  np.zeros(nf,dtype=float)                   #Vetor de produtos internos entre os vetores Uk e os valores de UT(x) para o MMQ
E2 = 0                                          #Vetor de erros quadráticos em cada ponto x da barra

Di = np.zeros(nf,dtype=float)                   #Vetor que representa a matriz Diagonal da decomposição LDLt
Li = np.zeros((nf,nf),dtype=float)              #Matriz triangular inferior da decomposição LDLt
Lit = np.zeros((nf,nf),dtype=float)             #Matriz triangular superior da decomposição LDLt (transposta da inferior, devido à simetria)
Zaux = np.zeros(nf,dtype=float)                 #Vetor auxiliar para resolução do sistema LDLtx=b
Caux = np.zeros(nf,dtype=float)                 #Vetor auxiliar para resolução do sistema LDLtx=b
 
dt = T/M                                        #Tamanho do incremento temporal a cada instante   
dx = 1/N                                        #Distância entre cada seção da barra

#Verificação visual dos parâmetros de entrada
print("N =",N)
print("M =",M)


####### PARÂMETROS PARA RESOLUÇÃO DO SISTEMA LDLt PARA CRANK-NICHOLSON ########

Fa = np.zeros(N-1,dtype=float)
Fb = np.zeros(N-1,dtype=float)        
   
#Vetores auxiliares e de output
D = np.zeros(N-1,dtype=float)   # Vetor representante da matriz diagonal
L = np.zeros(N-1,dtype=float)   # Vetor representante da matriz subdiagonal 
Raux = np.zeros(N-1,dtype=float) # Vetor resultante auxiliar, usado para calcular o vetor x 
xsol = np.zeros(N-1,dtype=float) # Vetor solução do sistema        
b = np.zeros(N-1,dtype=float)   # Vetor do lado direito do sistema 
ad = np.full(N-1,1+N)         # Vetor com os valores da diagonal da matriz a ser decomposta
asd = np.full(N-1,-N/2)       # Vetor com os valores da subdiagonal da matriz a ser decomposta
asd[0]=0                        # Adequando N-2 termos num vetor de tamnho N-1

# Laço para decomposição de A em LDLt
D[0]=ad[0]                      # Primeiro termo da diagonal D é igual ao primeiro termo da original A        
for i in range(1,N-1):
    L[i]=asd[i]/D[i-1]          # Termos de L em função dos termos da subdiagonal de A e da matriz diagonal D
    D[i]=ad[i]-(L[i]*asd[i])    # Termos de D em função dos termos da diagonal de A e das subdiagonais de A e L



############## FUNÇÃO PARA CÁLCULO DE PRODUTOS INTERNOS #######################
def produtointerno (X,Y):
    PInt = 0
    PIntFin = 0
    
    for i in range (N-1):
        PInt = X[i]*Y[i]
        PIntFin = PIntFin + PInt
    
    return (PIntFin)
 
        ################ INÍCIO DOS TESTES ################
           
if W == 1:                              #TESTE A
    pk = [0.35]

elif W == 2:                            #TESTE B
    pk = [0.15,0.3,0.7,0.8] #Vetor de valores das posições p1,p2,...,pnf.

elif W == 3 or W == 4:                  #TESTES C E D
    pk = [0.14999999999999999,0.20000000000000001,0.29999999999999999,0.34999999999999998,0.50000000000000000,0.59999999999999998,0.69999999999999996,0.72999999999999998,0.84999999999999998,0.90000000000000002]    
    


    ##### Definindo os vetores Uk através de Crank-Nicholson #####

for p in range (nf):
    
    if pk[p] != 0:
        
        for k in range(M+1):        #Laço temporal
            t=k*dt                  #Instante atual
            tf = t+dt                
            
            if k==0:
                Uold = U[0,:].copy()    #Definindo o vetor auxiliar inicial 
                              
            for q in range(N-1):    #Laço espacial
                x=q*dx          #Usa-se q+1 para que se construa uma matriz n-1 com apenas o valores de posições interiores da barra
                
                rta = 10*(1+np.cos(5*t)) #Função rt que determina o comportamento temporal da fonte pontual
                rtb = 10*(1+np.cos(5*tf)) #Função rt que determina o comportamento temporal da fonte pontual
                
                # Definindo a função gh que delimita a ação da fonte pontual
                if x>=(pk[p]-(dx/2)) and x<=(pk[p]+(dx/2)):
                    gh = 1/dx
                else:
                    gh = 0
                    
                Fa[q-1] = rta*gh      #Comportamento da fonte pontual
                Fb[q-1] = rtb*gh      #Comportamento da fonte pontual             
        
            for i in range(1,N):    #Laço espacial
                x=i*dx              #Local da barra a ser analisado

                #TRECHOS INTERIORES DA BARRA
                if k<M:
                    b[i-1]=Uold[i]+(dt/2)*(Fa[i-1]+Fb[i-1])+(N/2)*(Uold[i-1]-2*Uold[i]+Uold[i+1])
                    
            # Laço para o vetor que auxiliará nos calculos dos termos do vetor x em função dos termos do lado direito do sistema
            Raux[0]=b[0]   
            for i in range(1,N-1):
                Raux[i]=b[i]-(L[i]*Raux[i-1])
    
            # Laço para cálculo do vetor x que é solução do sistema em função dos termos da matriz A decomposta e do lado direito do sistema
            if k<M:
                Unew[N-1]=Raux[N-2]/D[N-2]   
                for i in range(N-3,-1,-1):
                    Unew[i+1]=(Raux[i]-(Unew[i+2]*asd[i+1]))/D[i]   

            Uold = Unew.copy()          #Substituição do vetor velho pelo novo
        
        for w in range (N-1):
            
            Uk[p,w] = Uold[w+1]

             

            
if W == 1:      
    for i in range (N-1):                  #TESTE A
        UT[i]=7*Uk[0,i]

elif W == 2:
    for i in range (N-1):                  #TESTE B
        UT[i]=2.3*Uk[0,i]+3.7*Uk[1,i]+0.3*Uk[2,i]+4.2*Uk[3,i]
            
elif W == 3 or W == 4:                      #TESTES C E D
    diretorio = str(input("Diretorio do arquivo 'TesteC.txt':")) + "\TesteC.txt"
    UTAux = np.loadtxt(diretorio, dtype=float)
    #print (UTAux)
    tamanho = np.size(UTAux)-1 
    passo = int(tamanho/N)

    for i in range (passo,tamanho,passo):
        indice = int(i/passo)-1
        UT[indice]=UTAux[i]
    
    if W == 4:                              #TESTE D
        eps = 0.01

        for i in range (N-1):
            r = (random.random()-0.5)*2
            ruido = 1+eps*r
            UT[i] = UT[i]*ruido

        
    
        ######### Montando o sistema normal do MMQ ###########

for k in range (nf):
    UkAuxK = np.copy(Uk [k,:])
    B[k] = produtointerno(UT, UkAuxK)
    A[k,k] = produtointerno(UkAuxK,UkAuxK)
    
    for i in range (k):
        UkAuxI = np.copy(Uk [i,:])
        A[k,i] = produtointerno(UkAuxK,UkAuxI)
        A[i,k] = A[k,i]
        
#print (A)       
        
        #### Decomposição da matriz A (simétrica) em LDLt ####
         
for k in range (nf):
   Li[k,k] = 1           #Transformando os valores da diagonal das matriz L em 1
   Di[k] = A[k,k]        #Construindo o vetor que representa a matriz diagonal D
   
   for i in range (k+1,nf): #Laço para definição dos demais valores da matriz L (multiplicadores da eliminação de Gauss)
       
       if Di[k] != 0:
           mult = A[i,k]/Di[k]
       else:
           mult = 0
       Li[i,k] = mult
       A[i,k] = 0
       
       for j in range(k+1,nf):      #Laço para multiplicação das linhas de A pelo multiplicador da elimanção de gauss
           A[i,j]=A[i,j]-A[k,j]*mult
         
for k in range (nf):                #Laço para constração de Li transposto (Lit)
    for i in range (nf):
        Lit[k,i] = Li[i,k]



    ############## Resolução do sistema Li*Di*Lit*Xa = B ##################
           
for k in range (nf):                #Laço para resolução do sistema com a substituição Li*Zaux = B, onde Zaux = Di*Caux e Caux=Lit*Xa.
    Zaux[k] = B[k]
    for i in range(k):
        Zaux[k] = Zaux[k] - Li[k,i]*Zaux[i]
    if Di[k] == 0:
        Caux[k] = 0
    else:
        Caux[k] = Zaux[k]/Di[k]
#print(Caux)
        
for k in range(nf-1,-1,-1):            #Laço para resolução do sistema retornado ao original onde Lit*Xa = Caux
    Xa[k] = Caux[k]
    for i in range (k+1,nf):
        Xa[k] = Xa[k] - Lit[k,i]*Xa[i]
        
#Comandos de verificação dos componentes de cálculo        
#print ("A",A)
#print ("Di",Di)
#print ("Li",Li)
#print ("Lit",Lit)
#print ("B",B)
#print ("Uk",Uk)
#print ("UT",UT)
    
    ################ Cálculo do erro quadrático ####################
        
Eaux2 = np.zeros(N-1,dtype=float)   #Vetor auxiliar para cálculo do erro

for i in range (N-1):
    Eaux1 = 0
    for k in range (nf):         
        Eaux1 = Eaux1 + Xa[k]*Uk[k,i]

    Eaux2[i] = (UT[i]-Eaux1)**2

    E2 = (dx*np.sum(Eaux2[i]))**0.5
    
        

    ################# Apresentação dos dados numéricos ####################
print ("Vetor solução Xa de intensidades pontuais:")
print (Xa)
print ("Erro quadrático: ", E2)            


EixoX = np.arange(0,1+dx,dx)                    #Distância entre cada seção da barra

for i in range (N-1):
    soma = 0
    
    for k in range (nf):
        soma = soma + Uk[k,i]*Xa[k] 
    
    UTx[i] = soma

Ux = np.zeros((nf,N+1),dtype=float)
for k in range (nf):
    for i in range (N-1):
        Ux[k,i+1] = Uk[k,i]*Xa[k]
    plt.plot(EixoX,Ux[k,:],"--", label="U%d(x)" %k)


#plt.plot(U0,U1,U2,U3,U4,U5,U6,U7,U8,U9,UT)

UTaux = np.zeros(N+1,dtype=float)

for i in range (N-1):
    UTaux[i+1] = UT[i]
plt.plot(EixoX,UTaux, linewidth=2.5,  label = "UT(x) dado", color='red')

for i in range (N-1):
    UTaux[i+1] = UTx[i]
plt.plot(EixoX,UTaux, linewidth=1, label = "UT(x) obtido", color='blue')
#plt.plot(U0)
#plt.plot(U0)  
plt.title("Temperatura por seção e componentes de intensidade") 
plt.xlabel("Local da barral")
plt.ylabel("Temperatura")
plt.legend()
plt.show()
        
        