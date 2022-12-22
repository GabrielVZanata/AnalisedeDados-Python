# -*- coding: latin-1 -*-
'''
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  https://pt.wikipedia.org/wiki/Quicksort
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html
'''

#################################### DEFININDO AS FUNCOES ##############################################

def calcula_id(matriz):
    """ Retorna o valor de identifica��o de uma matriz computada pelo
    algoritmo adler32

    A fun��o :func:'calcula_id' computa um identificador para uma matriz
    usando a seguinte vers�o adaptada do algoritmo de espalhamento Adler32:

        - A = 1 + matriz[0][0] + matriz[0][1] +...+ matriz[m-1][n-1] MOD 65521,
            onde m � o n�mero de linhas e n � o n�mero de colunas da matriz
        - B = (1 + matriz[0][0]) + (1 + matriz[0][0]+matriz[0][1]) + ... +
          (1 + matriz[0][0] + matriz[0][1] + ... + matriz[m-1][n-1]) MOD 65521
        - retorna B * (2**16) + A


    :param matriz: Uma matriz de inteiros
    :type matriz: <class 'list'>
    :return identificador: O identificador inteiro da matriz computado segundo
        a nossa vers�o adaptada do Adler32
    :rtype: <class 'int'>

    :Examples:

    >>> matriz_A = [[0,1,2], [3,4,5]]
    >>> matriz_B = [[3,4,5], [0,1,2]]
    >>> matriz_C = [[0,1], [1,0]]
    >>> matriz_D = [[1,0,2], [3,4,5]]
    >>> calcula_id(matriz_A)
    2686992
    >>> calcula_id(matriz_B)
    4456464
    >>> calcula_id(matriz_C)
    589827
    >>> calcula_id(matriz_D)
    2752528
    """

    A2=1 #Vari�vel auxiliar de grava��o de valor
    i=0
    for i in range(0,len(matriz)): #Varredura de matriz
        j=0
        for j in range(0,len(matriz[0])):
            A2+=matriz[i][j]
    A = A2%65521 

    B2=0 #Vari�vel auxiliar de grava��o de valor
    B3=1 #Vari�vel auxiliar de grava��o de valor
    i=0
    for i in range(0,len(matriz)): #Varredura de matriz
        j=0
        for j in range(0,len(matriz[0])):
            B3+=matriz[i][j]
            B2+=B3
    B=B2%65521

    M=B*(2**16)+A #Cria��o do inteiro baseado na f�rmula 
    return M
            


def carrega_identificador(nome_arquivo):
    
    """ Carrega o identificador de uma imagem presente em um arquivo.

    A fun��o :func:'carrega_identificador' abre um arquivo de nome
    'nome_arquivo' presente na mesma pasta que o programa, l� sua
    primeira linha e retorna o inteiro representando o identificador  
    presente nessa linha.

    :param nome_arquivo: String com o nome do arquivo com o identificador
    :type nome_arquivo: <class 'str'>
    :return identificador: Inteiro contendo identificador 
    :rtype: <class 'int'>

    :Example:

    >>> identificador = carrega_identificador('img01.adler32')
    >>> print(identificador)
    297286
    """
    arquivo=open(nome_arquivo,'r') #Abre arquivo
    identificador=int(arquivo.read()) #L� e escreve o conte�do do arquivo em str, por isso o int()
    arquivo.close() #Fecha arquivo
    return identificador


def carrega_imagem(nome_imagem):
    """ Carrega do arquivo 'nome_imagem' uma imagem em formato PGM do tipo P2 e
    retorna � imagem em formato de matriz de pixels.

    A fun��o :func:'carrega_imagem' l� uma imagem em formato PGM do tipo P2
    presente em um arquivo na mesma pasta do programa e retorna uma
    matriz de inteiros de tamanho N-por-M, onde N � a altura da imagem, e M �
    largura da imagem, ambos medidos em pixels e obtidos atrav�s do cabe�alho
    da imagem.

    :param nome_imagem: String com o nome de imagem na mesma pasta de ep3.py
    :type nome_imagem: <class 'str'>
    :return matriz: Matriz de inteiros representando os pixels da imagem
    :rtype: <class 'list'>

    :Example:

    >>> A = carrega_imagem('imagem.pgm')
    >>> print(A)
    [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    """
    imagem=open(nome_imagem,'r')
    matriz=[] #Matriz final apenas com os termos interessantes
    matriz_aux=[] #Matriz auxiliar para a forma��o da matriz inicial
    for linha in imagem:
        l=linha.strip()
        if len(l)>0:
            termos=l.split(" ") #Cria��o de termos separados por " "
            matriz_aux.append(termos)
    for i in range(3,len(matriz_aux)): #Elimina��o das 3 primeiras linhas
        matriz.append(matriz_aux[i])
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            matriz[i][j]=int(matriz[i][j]) #Transforma��o dos termos em inteiros
    imagem.close()
    return matriz
    


def salva_imagem(nome_arquivo, matriz):
    """ Cria (se n�o existir) e escreve a imagem representada pela matriz no
    arquivo de nome nome_arquivo no formato PGM (tipo 2).

    A fun��o :func:'salva_imagem' recebe uma matriz de inteiros (0-255)
    representando uma imagem em tons de cinza e salva essa imagem no arquivo
    'nome_arquivo' no formato Portable GrayMap (PGM) do tipo P2 na mesma pasta.


    :param nome_arquivo: String contendo o nome de um arquivo (ex.'imagem.ppm')
    :param matriz: Matriz de inteiros representando uma imagem em tons de cinza
    :type nome_arquivo: <class 'str'>
    :type matriz: <class 'list'>

    :Example:

    >>> M = carrega_imagem('imagem.pgm')
    >>> print(M)
    [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    >>> M[0][0] = 255
    >>> print(M)
    [[255, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    >>> salva_imagem('nova_imagem.pgm', M)
    """

    arquivo=open(nome_arquivo,'w')
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            matriz[i][j]=str(matriz[i][j]) #Transforma��o dos termos em string para serem salvos em texto
            
    n=len(matriz)
    m=len(matriz[0])
    
    arquivo.write("P2\n")
    arquivo.write("%d %d\n"%(m,n))
    arquivo.write("255\n")          #Cabe�alho padr�o
    
    for i in range(n):
        for j in range(m-1):
            arquivo.write(matriz[i][j])
            arquivo.write(" ")
        arquivo.write(matriz[i][m-1])
        arquivo.write("\n")         #Escrita dos termos separados por " " no arquivo 
    arquivo.close()


def carrega_transformacoes(nome_arquivo='transformacoes.txt'):
    """Carrega transforma��es de um arquivo de texto.

    A fun��o :func:'carrega_transforma��es' recebe uma string com o nome de um
    arquivo presente na mesma pasta do programa que cont�m as matrizes
    de transforma��o.
    Neste arquivo:

        - A primeira linha representa o n�mero total de transforma��es
        - Todas as outras linhas trazem ou transforma��es ou coment�rios

    Uma linha come�ando com # indica um coment�rio e deve ser ignorada.
    Todas as outras linhas representam matrizes 2-por-3 de modo que a matriz
    inteira est� representada em uma �nica linhado arquivo e cada elemento da
    matriz � separado por um (ou mais) espa�os.
    O exemplo abaixo mostra o conte�do de um poss�vel arquivo de transforma��es

    **Exemplo de arquivo de transforma��es**:
    2
    # Meu conjunto de transforma��es
    # transforma��o identidade
    1 0 0 0 1 0
    # espelhamento
    -1 0 0 0 -1 0


    :param nome_arquivo: String com nome de um arquivo texto contendo as
        transforma��es
    :type nome_arquivo: <class 'str'>
    :return lista: Uma lista de matrizes de transforma��o
    :rtype: <class 'list'>

    :Example:

    >>> transforma��es = carrega_transforma��es('duas_transforma��es.txt')
    >>> print(transforma��es)
    [[[1, 0, -20], [0, 1, -20]], [[1, 0, 0], [0, 1, 0]]]

    """
    arq_trans=open(nome_arquivo,'r')
    matrizA=[] #Matriz para transforma��o do arquivo de texto em algo manipul�vel em python
    for linha in arq_trans:
        l=linha.strip()
        if len(l)>0:
            termos=l.split(" ")
            matrizA.append(termos) #Separa��o dos termos da matriz por " "


    matrizB=[] #Matriz auxiliar para elimina��o dos coment�rios do arquivo, presentes em matrizA
    for i in range(1,len(matrizA)):
        if matrizA[i][0] != "#":
            matrizB.append(matrizA[i])

    for i in range(0,len(matrizB)): #Transforma��o dos termos strings em termos inteiros
        for j in range(0,len(matrizB[0])):
            matrizB[i][j]=int(matrizB[i][j])

            
    matrizC=[]  #Matriz auxiliar para forma��o da linha 1 de uma matriz 2x3 (primeira metade dos termos de matrizB)
    matrizD=[]  #Matriz auxiliar para forma��o da linha 2 de uma matriz 2x3 (segunda metade dos termos de matrizB)
    matrizE=[]  #Matriz auxiliar para a unifica��o em uma matriz das linhas 1 e 2 criadas anteriormente
    matriz=[]   #Lista final cujos os termos s�o as matrizes 2x3 criadas anteriormente
    for i in range(0,len(matrizB)):
        for j in range(0,len(matrizB[i])//2): #Forma��o da linha 1
            matrizC.append(matrizB[i][j])
        for j in range(len(matrizB[i])//2,len(matrizB[i])): #forma��o da linha 2
            matrizD.append(matrizB[i][j])
        matrizE.append(matrizC)
        matrizE.append(matrizD) #Cria��o da matriz 2x3
        matriz.append(matrizE)  #Lista final de matrizes
        matrizC=[]
        matrizD=[]
        matrizE=[]

    return matriz
        


def transforma(matriz, transformacao):
    """ Devolve uma transforma��o geom�trica linear da matriz.

    A fun��o :func:'transforma' recebe uma matriz de pixels e uma transforma��o
    afim representada matricialmente e retorna a matriz transformada, **sem**
    modificar a matriz original.


    :param matriz: Matriz representando imagem em tons de cinza (0-255)
    :param transforma��o: Matriz 2-por-3 representando transforma��o linear
    :type matriz: <class 'list'>
    :type transforma��o: <class 'list'>
    :return matriz_transformada: Matriz resultado da transforma��o aplicada
        sobre todos os pontos
    :rtype: <class 'list'>

    :Example:

    >>> matriz1 = [[1, 2, 3], [4, 5, 6]]
    >>> print(matriz1)
    [[1, 2, 3], [4, 5, 6]]
    >>> transla��o_diagonal_por_1_pixel = [[1, 0, 1], [0, 1, 1], [0, 0, 1]]
    >>> matriz2 = transforma(matriz1, transla��o_diagonal_por_1_pixel)
    >>> print(matriz1)
    [[1, 2, 3], [4, 5, 6]]
    >>> print(matriz2)
    [[6, 4, 5], [3, 1, 2]]

    """
    A=len(matriz)
    L=len(matriz[0])
    T=transformacao
    M=matriz
    N=[]
    matriz_aux=[] #Matriz auxiliar para a forma��o de uma matriz de zeros com tamanho MxN igual ao da matriz recebida como par�metro
    for i in range(0,A): #Processo de forma��o da matriz de zeros citada acima
        for j in range(0,L):
            matriz_aux.append(0)
        N.append(matriz_aux)
        matriz_aux=[]
        
    for x1 in range(L-1,-1,-1): #aplica��o da f�rmula de tranforma��es
        for y1 in range(A-1,-1,-1):
            x2=(T[0][0]*x1)+(T[0][1]*y1)+(T[0][2])
            y2=(T[1][0]*x1)+(T[1][1]*y1)+(T[1][2])
            x2=x2%L
            y2=y2%A
            if N[y2][x2]==0:
                N[y2][x2]=M[y1][x1]

    return N
            


def busca(matriz, transformacoes, identificacao, max_transfs=10):
    """ Busca imagem com identifica��o dada usando no m�ximo um conjunto de
    max_transfs transforma��es.

    A fun��o :func:'busca' recebe uma matriz representando uma imagem
    monocrom�tica, uma lista de transforma��es poss�veis, um identificador
    correspondente � dispers�o criptogr�fica da imagem original e o valor do
    n�mero m�ximo de transforma��es em sequencia � serem realizadas sobre �
    matriz nessa busca e devolve:

        - A matriz da imagem original (caso encontrada) OU
        - None (caso contr�rio)

    :param matriz: Uma matriz de inteiros representando uma imagem
    :transforma��es: Uma lista de matrizes de transforma��o
    :identifica��o: Uma string com o identificador da imagem original
    :max_transfs: N�mero m�ximo de sequencias de transforma��es � testar
    :type matriz: <class 'list'>
    :type transforma��es: <class 'list'>
    :type identifica��o: <class 'str'>
    :type max_transfs: <class 'int'>
    :return resultado: Matriz com imagem restaurada ou None se ela n�o for
        encontrada.
    :rtype: <class 'list'> OU <class 'NoneType'>

    :Example:

    >>> original = [[1,2,3], [4,5,6], [7,8,9]]
    >>> identificador = calcula_id(imagem)
    >>> print(identificador)
    11403310
    >>> nova = transforma(imagem, [[1,0,1], [0,1,0]]) # Aplica desloc em eixo x
    >>> print(nova)
    [[3, 1, 2], [6, 4, 5], [9, 7, 8]]
    >>> nova2 = transforma(nova, [[1,0,1], [0,1,1]]) # Aplica Desloc x+1 e y+1
    >>> print(nova2)
    [[8, 9, 7], [2, 3, 1], [5, 6, 4]]
    >>> transfs = [[[1,0,-1], [0,1,0]], [[1,0,-1],[0,1,-1]], [[1,0,1],[0,1,1]]]
    >>> resultado = busca(nova2, transfs, identificador, 2)
    >>> print(resultado)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> resultado2 = busca(nova2, transfs, identificador, 1)
    >>> print(resultado2)
    None
    """
    if calcula_id(matriz) == identificacao:
        return matriz
    if max_transfs == 0:
        return None
    for i in transformacoes:
        N = transforma(matriz, i)
        R = busca(N, transformacoes, identificacao, max_transfs-1)
        if R != None:
            return R
    return None

###################################################### CORPO DO PROGRAMA #####################################################

def main():
    print ("*****************************")
    print ("*** Programa 'desfaz virus' ***")
    print ("*****************************")
    print ("\nAutor: Gabriel Valverde Zanata da Silva")

    diretorio = str(input("Digite o diretorio dos arquivos: "))

    modo = int(input("1 - Editar arquivo individual\n2 - Editar todos os arquivos de uma vez (loop)"))

    if modo == 1:

        nomearq=input ("\nEntre com o nome do arquivo contendo imagem transformada sem a extensão (pgm):")
        #img_trans=input ("\nEntre com o nome do arquivo contendo imagem transformada sem a extensão (pgm):") + ".pgm"
        #img_ident=input ("Entre com o nome do arquivo contendo o identificador da imagem original:")
        img_trans= diretorio + nomearq + ".pgm"
        img_ident= diretorio + nomearq + ".adler32"
        matriz_transfs= diretorio + input ("Entre com o nome do arquivo contendo as transformacoes disponiveis sem a extensao(.txt):") + ".txt"
        arqv_save= diretorio + input ("Entre com o nome do arquivo onde a imagem original deve ser salva sem a extensão (.pgm):") + ".pgm"
        max_transfs=int(input ("Entre com o numero maximo de transformacoes:"))

        print("Tentando restaurar imagem '%s'... "%(img_trans),end="")


        identificacao=carrega_identificador(img_ident)
        matriz_img=carrega_imagem(img_trans)
        transformacoes=carrega_transformacoes(matriz_transfs)
        resultado=busca(matriz_img,transformacoes,identificacao,max_transfs)

        if resultado == None:
            print("Falhou!")
            print("\nNao foi possivel encontrar uma imagem com o identificador %d utilizando uma sequencia de no maximo %d transformacoes em '%s'"%(identificacao,max_transfs,matriz_transfs))
            print("\nVoce pode tentar aumentar o numero maximo de transformacoes ou mudar o arquivo de transformacoes.")
        else:
            print("Pronto!")
            salva_imagem(arqv_save, resultado)
            print("Imagem com o identificador %d salva em '%s'!"%(identificacao, arqv_save))

    else:

        matriz_transfs= diretorio + input ("Entre com o nome do arquivo contendo as transformacoes disponiveis sem a extensao(.txt):") + ".txt"
       
        for i in range(11):
            if i != 10:
                nomearq = "img0" + str(i)
            else:
                nomearq = "img10" 
            img_trans= diretorio + nomearq + ".pgm"
            img_ident= diretorio + nomearq + ".adler32"
            arqv_save= diretorio + "resultado" + nomearq[3:] + ".pgm"
            max_transfs= 15
    
            print("Tentando restaurar imagem '%s'... "%(img_trans),end="")


            identificacao=carrega_identificador(img_ident)
            matriz_img=carrega_imagem(img_trans)
            transformacoes=carrega_transformacoes(matriz_transfs)
            resultado=busca(matriz_img,transformacoes,identificacao,max_transfs)

            if resultado == None:
                print("Falhou!")
                print("\nNao foi possivel encontrar uma imagem com o identificador %d utilizando uma sequencia de no maximo %d transformacoes em '%s'"%(identificacao,max_transfs,matriz_transfs))
                print("\nVoce pode tentar aumentar o numero maximo de transformacoes ou mudar o arquivo de transformacoes.")
            else:
                print("Pronto!")
                salva_imagem(arqv_save, resultado)
                print("Imagem com o identificador %d salva em '%s'!"%(identificacao, arqv_save))
    
    
if __name__ == "__main__":
    main()
