#Este programa retorna uma lista de números primos,
#com a quantidade de números estipulada pelo usuário.

def list_primo(qtd):
    lista = []
    i = 0
    while len(lista) < qtd:
        i += 1
        if is_primo(i) == True:
            lista.append(i)
    return lista

def is_primo(num):
    primo = True
    while primo == True:
        if num == 1 or num == 2: break
        for i in range(2,num): 
            if num % i == 0:
                primo = False
        break
    if not primo:
        return False
    else:
        return True

print ("---------------------------------------")
print ("Bem vindo ao programa de números primos")
print ("---------------------------------------")




sel = 3
loop = True

while loop:

    print ("\nGerar sequência de primos - Digite 1")
    print ("Verificar se é primo - Digite 2")
    print ("Para sair - Digite 0")
    
    while sel > 2:
        sel = int(input())

    if sel == 1:
        sel = 3
        qtd = int(input("Digite a quantidade de números primos desejada: "))

        lista = list_primo(qtd)

        print(lista)

    elif sel == 2:
        sel = 3
        cont = 1
        while cont == 1:
            num = int(input('\nDigite o número a ser verificado: '))
            if is_primo(num) == True:
                print("O número ", num, " é primo.")
            else:
                print("O número ", num, " não é primo.")
            cont = int(input("\nPara verificar outro número digite 1, para sair digite 0."))

    elif sel == 0:
        loop = False



