#Este programa implemanta o funcionamento do algoritmo selection sort
import random

def sort(lista_base, dir = 'up'):
    lista = lista_base.copy()
    for i in range (0,len(lista)):
        for j in range(i, len(lista)):
            lis_i = lista[i]
            lis_j = lista[j]
            if dir == 'up':
                if lis_j < lis_i:
                    lista[i] = lis_j
                    lista[j] = lis_i
            if dir == 'down':
                if lis_j > lis_i:
                    lista[i] = lis_j
                    lista[j] = lis_i                 
    return lista
            
def rand_list(size=20, qt=100):
    lista = []
    for i in range(0,size):
        x = random.randint(0,qt)
        lista.append(x)
    return lista

#lista = rand_list(50)
#lista_sort = sort(lista)   
#print(lista)        
#print(lista_sort)       
