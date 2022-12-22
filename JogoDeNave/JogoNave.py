"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Gabriel Valverde Zanata da Silva
  NUSP : 10774799
  Turma: 05
  Prof.: Fujita

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://wiki.python.org.br/QuickSort

  """

# !!!!! NÃO APAGUE NEM ALTERE NENHUM import !!!!!!
import random

# !!!!! PARA TESTAR O JOGO, USE VALORES MENORES, COMO 10 E 5, MAS
# VOLTE PARA O ORIGINAL ANTES DE ENTREGAR !!!!
COLUNA_MAXIMA     = 56 #56
LINHA_MAXIMA      = 19 #19

# !!!!! NÃO APAGUE NEM ALTERE NENHUMA CONSTANTE !!!!!
# CONSTANTES DE IMPRESSÃO NA TELA
CANHAO            = 'A'
NAVE              = 'V'
LASER_CANHAO      = '^'
LASER_NAVE        = '.'
EXPLOSAO          = '*'

# !!!!! NÃO APAGUE NEM ALTERE NENHUMA CONSTANTE !!!!!
# CONSTANTES DE AÇÕES DE MOVIMENTAÇÃO DOS OBJETOS NO JOGO
ATIRA             = 3  # para tecla 'l' quando movimentar o canhão
ESQUERDA          = -1 # para tecla 'e' quando movimentar o canhão
DIREITA           = 1  # para tecla 'd' quando movimentar o canhão
BAIXO             = -2

# !!!!! NÃO APAGUE NEM ALTERE NENHUMA CONSTANTE !!!!!
# CONSTANTES DE RESULTADO DO JOGO
VENCEU            = True
PERDEU            = False

# !!!!! NÃO APAGUE NEM ALTERE NENHUMA CONSTANTE !!!!!
# CONSTANTES DOS PONTOS RELACIONADOS A LASERS OU NAVES DESTRUÍDAS
PONTOS_ACERTOU_LASER     = 1
PONTOS_ACERTOU_NAVE      = 3

# !!!!! NÃO APAGUE NEM ALTERE NENHUMA CONSTANTE !!!!!
# OUTRAS CONSTANTES: SEMENTE DO GERADOR DE NÚMEROS ALEATÓRIOS E
# VALORES USADOS NA FUNÇÃO QUE MOVIMENTA AS NAVES
SEMENTE           = 0
ATINGIU_ESQUERDA  = -1
ATINGIU_DIREITA   = 1
ATINGIU_EMBAIXO   = -2

# !!!!! NÃO MODIFIQUE NADA NO main() !!!!!
# FUNÇÃO PRINCIPAL QUE SÓ LÊ A QUANTIDADE DE INIMIGOS DO TECLADO,
# PASSA O CONTROLE PARA A FUNÇÃO REAL DO JOGO E RECEBE COMO RETORNO A
# PONTUAÇÃO DO JOGADOR PARA IMPRIMIR NA TELA COM O RESULTADO DO JOGO
def main():
    random.seed(SEMENTE)
    
    quantidadeNaves = int(input("Digite o numero de naves (inteiro maior que 1 e menor que %d): " %(COLUNA_MAXIMA-3)))
    
    resultado = joga(quantidadeNaves)
    
    if resultado[0] == VENCEU:
        print(">>> CONGRATULATIONS! Você venceu!")
    else:
        print(">>> GAME OVER! Você perdeu!")
    
    print(">>> Pontuação:",resultado[1])




# DEMAIS FUNÇÕES NECESSÁRIAS PARA O JOGO
# !!!!! SEU TRABALHO COMEÇA AQUI. COMPLETE TODAS AS FUNÇÕES !!!!!
# !!!!! MAS NÃO MODIFIQUE A ASSINATURA DE NENHUMA DELAS E NEM O QUE JÁ ESTÁ FEITO !!!!!

# Passo 0: função para imprimir a matriz do jogo. Ela precisa ser
# modificada para imprimir os '|' nas laterais direita e esquerda
def imprimeMatriz(matriz):
    ''' (matriz) -> None
    
          Imprime a matriz do jogo. Cada posição da matriz é um caracter e deve
          ser impresso exatamente com o valor dele.'''
    for linha in matriz:
        print ("|", end="")
        for posicao in linha:
            print(posicao, end = "")
        print("|")

# Passo 1: função que cria todos os elementos na matriz do jogo (Deve
# ser chamada só no início do jogo)
def criaElementos(quantidadeNaves, matriz):
    ''' int, (matriz) -> None
    
          Recebe um inteiro com a quantidade de naves a serem criadas
          e a matriz de caracteres vazia para colocar os elementos no início do
          jogo: o canhão do jogador na linha de baixo e na coluna do meio e as
          naves na parte superior. As naves devem sempre ficar em pares (um em
          cima do outro) e separados pelos outros pares por uma coluna vazia.
          Por exemplo, se a quantidade de naves for 4, a parte superior da
          matriz tem que ficar assim:
          
          V V
          V V
          
          Se for 6 tem que ficar assim:
          
          V V V
          V V V

          Se for 5 tem que ficar assim:

          V V V
          V V  
          '''
    navesLinha1 = ((int(quantidadeNaves/2) + quantidadeNaves%2)*2)
    navesLinha2 = (int(quantidadeNaves/2)*2)
    for i in range(0,navesLinha1,2):
        matriz[0][i] = NAVE
    for i in range(0,navesLinha2,2):
        matriz[1][i] = NAVE
    matriz[19][28] =  CANHAO

# Passo 2: primeira função para mover algum elemento que emite lasers.
# Nesse caso para mover o canhão do jogador.
def moveCanhao(direcao, matriz):
    ''' int, (matriz) -> bool
 
          Recebe um inteiro com a direção (valores definidos em ESQUERDA e
          DIREITA) para mover o canhão do jogador (caracter definido em CANHAO)
          e a matriz de caracteres do jogo, para mover o canhão nessa direção.
          Ao mover tem que observar se atingiu algum laser de alguma nave (caso
          no qual tem que imprimir um EXPLOSAO no lugar). Nesse caso precisará
          informar que o canhão foi atingido pois a função retorna esse valor.
          
          Retorna:
                   
          True se canhão do jogador foi atingido (False se não)
                   
          Obs.: o movimento do canhão é ciclíco quando ele se move além dos
          limites laterais da matriz do jogo.'''

    
    if direcao == DIREITA: #direita
        i = 0
        semcanhao = True
        while semcanhao:
            c = matriz[LINHA_MAXIMA][i]
            if c == CANHAO:
                semcanhao = False
            else:
                i += 1
        
        matriz[LINHA_MAXIMA][i] = ' '
        if i == COLUNA_MAXIMA:
            i = 0
        else:
            i += 1
        if matriz[LINHA_MAXIMA][i] == ' ':
            matriz[LINHA_MAXIMA][i] = CANHAO
            return False
        else:
            matriz[LINHA_MAXIMA][i] = EXPLOSAO
            return True

    if direcao == ESQUERDA: #esquerda
        i = 0
        semcanhao = True
        while semcanhao:
            c = matriz[LINHA_MAXIMA][i]
            if c == CANHAO:
                semcanhao = False
            else:
                i+=1
        matriz[LINHA_MAXIMA][i]= ' '
        if i == 0:
            i = COLUNA_MAXIMA
        else:
            i -= 1
        if matriz[LINHA_MAXIMA][i] == ' ':
            matriz[LINHA_MAXIMA][i] = CANHAO
            return False
        else:
            matriz[LINHA_MAXIMA][i]= EXPLOSAO
            return True



# Passo 2: segunda função para mover algum elemento que emite lasers.
# Nesse caso para mover as naves.
def moveNaves(direcao, matriz):
    ''' int, (matriz) -> [bool, int, int]
 
          Recebe um inteiro com a direcao (valores definidos em ESQUERDA,
          DIREITA e BAIXO) para mover as naves (caracter definido em NAVE) e a
          matriz de caracteres do jogo, para mover as naves nessa direção. Ao
          mover tem que observar se chegou em algum extremo da matriz, se
          atingiu o canhão do jogador e se atingiu algum laser do jogador. No
          primeiro e no segundo caso precisa informar que isso aconteceu e no
          terceiro caso precisa atualizar a quantidade de naves atingidas
          porque a função retorna esses valores numa lista. No segundo caso tem
          que colocar o caracter definido em EXPLOSAO e no terceiro caso a nave
          tem que sumir da matriz.
                   
          Retorna:
          
          [True se canhão do jogador foi atingido (False se não), limite atingido, quantidade de naves atingidas]
           
          Onde limite atingido tem os seguintes significados:
          
          - valor definido em ATINGIU_DIREITA se alguma nave após o movimento chegou em COLUNA_MAXIMA
          - valor definido em ATINGIU_ESQUERDA se alguma nave após o movimento chegou na coluna 0
          - valor definido em ATINGIU_EMBAIXO se alguma nave após o movimento chegou na linha LINHA_MAXIMA
          - 0 caso nenhuma das alternativas anteriores tenha acontecido
          
          Obs.: mesmo que a primeira nave verificada atinja o canhão ou atinja
          a linha mais baixa da matriz, tem que varrer a matriz **inteira** para
          atualizar a quantidade de naves atingidas antes de retornar'''
    canhaoVivo = True
    lim = 0
    qtdNavesDest = 0

    
    if direcao == DIREITA: #DIREITA
        i = 0
        j = COLUNA_MAXIMA
        semNave = True
        while i < LINHA_MAXIMA:
            j = COLUNA_MAXIMA
            while j >= 0:
                x = matriz[i][j]
                if x == NAVE:
                    z = matriz[i][j+1]
                    if j+1 == COLUNA_MAXIMA:
                        lim = ATINGIU_DIREITA
                    if z == CANHAO:
                        canhaoVivo = False
                        qtdNavesDest += 1
                        matriz[i][j] = ' '
                        matriz[i][j+1] = EXPLOSAO
                    elif z == ' ':
                        matriz[i][j] = ' '
                        matriz[i][j+1] = NAVE
                    elif z == LASER_CANHAO:
                        qtdNavesDest += 1
                        matriz[i][j] = ' '
                        matriz[i][j+1] = ' '
                j -= 1
            i += 1

    if direcao == ESQUERDA: #ESQUERDA
        i = 0
        j = 0
        semNave = True
        while i < LINHA_MAXIMA:
            j = 0
            while j <= COLUNA_MAXIMA:
                x = matriz[i][j]
                if x == NAVE:
                    y = matriz[i][j-1]
                    if j-1 == 0:
                        lim = ATINGIU_ESQUERDA
                    if y == CANHAO:
                        canhaoVivo = False
                        qtdNavesDest += 1
                        matriz[i][j] = ' '
                        matriz[i][j-1] = EXPLOSAO
                    elif y == ' ':
                        matriz[i][j] = ' '
                        matriz[i][j-1] = NAVE
                    elif y == LASER_CANHAO:
                        qtdNavesDest += 1
                        matriz[i][j] = ' '
                        matriz[i][j-1] = ' '
                j += 1
            i += 1

    if direcao == BAIXO: #BAIXO
        i = LINHA_MAXIMA
        j = 0
        semNave = True
        while i >= 0:
            j = 0
            while j <= COLUNA_MAXIMA:
                x = matriz[i][j]
                if x == NAVE:
                    k = matriz[i+1][j]
                    if i+1 == LINHA_MAXIMA:
                        lim = ATINGIU_EMBAIXO
                    if k == CANHAO:
                        canhaoVivo = False
                        lim = 0
                        qtdNavesDest += 1
                        matriz[i][j] = ' '
                        matriz[i+1][j] = EXPLOSAO
                    elif k == LASER_CANHAO:
                        lim = 0
                        qtdNavesDest += 1
                        matriz[i][j] = ' '
                        matriz[i+1][j] = ' '
                    else:
                        lim = 0
                        matriz[i][j] = ' '
                        matriz[i+1][j] = NAVE
                j += 1
            i -= 1

    if canhaoVivo:
        return [False,lim,qtdNavesDest]
    else:
        return [True,lim,qtdNavesDest]
        

# Passo 3: primeira função para emitir lasers. Nesse caso, para emitir
# um novo laser pelo canhão do jogador.
def emiteLaserCanhao(matriz):
    ''' (matriz) -> [int, int]
 
          Recebe a matriz do jogo e emite um novo laser atirado pelo jogador
          (caracter definido em LASER_CANHAO) uma posição acima da posição onde
          o canhão se encontra.  Ao emitir o laser já tem que observar: se
          atingiu alguma nave e se atingiu algum laser de alguma nave. Em todos
          esses casos o laser recém-emitido já tem que sumir da matriz (ele nem
          chega a ser impresso nesse caso) e tem que atualizar a quantidade de
          naves atingidas e de lasers atingidos pois a função retorna esses
          dois valores numa lista.
 
          Retorna:
 
          [quantidade de naves atingidas, quantidade de lasers atingidos]'''
    qtdNavesDest = 0
    qtdLaserDest = 0
    i = 0
    semcanhao = True
    while semcanhao:
        c = matriz[LINHA_MAXIMA][i]
        if c == CANHAO:
            semcanhao = False
        else:
            i += 1
    d = matriz[LINHA_MAXIMA-1][i]
    if d == NAVE:
        qtdNavesDest += 1
        matriz[LINHA_MAXIMA-1][i] = ' '
    if d == LASER_NAVE:
        qtdLaserDest += 1
        matriz[LINHA_MAXIMA-1][i] = ' '
    if d == ' ':
        matriz[LINHA_MAXIMA-1][i] = LASER_CANHAO
        
    return [qtdNavesDest,qtdLaserDest]
# Passo 3: segunda função para emitir lasers. Nesse caso para emitir
# novos lasers pelas naves.
def emiteLasersNaves(matriz):
    ''' (matriz) -> [bool, int]
 
          Recebe a matriz do jogo e emite lasers pelas naves (caracter definido
          em LASER_NAVE) uma posição abaixo da posição da nave que emitiu o
          laser. Ao emitir o laser já tem que observar: se atingiu o canhão do
          jogador (caso no qual tem que imprimir um EXPLOSAO no lugar) e se
          atingiu algum laser do jogador. Em todos esses casos, o laser
          recém-emitido já tem que sumir da matriz (ele nem chega a ser impresso
          nesse caso). No primeiro caso tem que informar que o canhão do jogador
          foi atingido e no segundo caso tem que atualizar a quantidade de
          lasers atingidos pois a função retorna esses dois valores numa lista.
 
          Para definir se uma nave deve ou não emitir laser, sorteie um
          número aleatório entre 0 e 1 (use a função random.randint para isso),
          inclusive. Se o resultado for 0, não emita o laser para aquela nave.
          Se o resultado for 1, emita. Essa verificação só deve ser feita para
          aquelas naves que não possuem nenhuma outra imediatamente abaixo e
          sempre na ordem da esquerda para a direita da matriz.
                
          Retorna:
          
          [True se canhão do jogador foi atingido (False se não), quantidade de lasers atingidos]
          
          Obs.1: mesmo que o primeiro laser emitido atinja o canhão, tem que
          varrer a matriz **inteira** para atualizar a quantidade de lasers
          atingidos antes de retornar'''
    
    qtdLasersDest = 0
    i = LINHA_MAXIMA
    j = 0
    semNave = True
    canhaoVivo = True
    while i >= 0:
        j = 0
        while j <= COLUNA_MAXIMA:
            x = matriz[i][j]
            if x == NAVE:
                k = matriz[i+1][j]
                if k != NAVE:
                    rand = random.randint(0,1)
                    if rand == 1:
                        if k == CANHAO:
                            canhaoVivo = False
                            matriz[i+1][j] = EXPLOSAO
                        elif k == ' ':
                            matriz[i+1][j] = LASER_NAVE
                        elif k == LASER_CANHAO:
                            qtdLasersDest += 1
                            matriz[i+1][j] = ' '
            j += 1
        i -= 1

    if canhaoVivo:
        return [False,qtdLasersDest]
    else:
        return [True,qtdLasersDest]   
# Passo 4: primeira função para mover lasers. Nesse caso, para mover
# os lasers do jogador.
def moveLasersCanhao(matriz):
    ''' (matriz) -> [int, int]
 
          Recebe a matriz do jogo e move todos os lasers atirados pelo jogador
          (caracter definido em LASER_CANHAO) uma posição para cima na matriz.
          Ao mover tem que observar: se saiu do limite da matriz, se atingiu
          alguma nave e se atingiu algum laser de alguma nave. Em todos esses 3
          casos o laser movido tem que sumir da matriz. Nos dois primeiros
          casos tem que atualizar a quantidade de naves atingidas e de lasers
          atingidos pois a função retorna esses dois valores numa lista.
 
          Retorna:
 
          [quantidade de naves atingidas, quantidade de lasers atingidos]'''
    
    qtdNavesDest = 0
    qtdLaserDest = 0
    i = 0
    j = 0
    semLaserCanhao = True
    while i <= LINHA_MAXIMA:
        j = 0
        while j <= COLUNA_MAXIMA:
            f = matriz[i][j]
            if f == LASER_CANHAO:
                if i != 0:
                    g = matriz[i-1][j]
                    if g == NAVE:
                        qtdNavesDest += 1
                        matriz[i][j] = ' '
                        matriz[i-1][j] = ' '
                    elif g == ' ':
                        matriz[i][j] = ' '
                        matriz[i-1][j] = LASER_CANHAO
                    elif g == LASER_NAVE:
                        qtdLaserDest += 1
                        matriz[i][j] = ' '
                        matriz[i-1][j] = ' '
                if i == 0:
                    matriz[i][j] = ' '                   
                
            j += 1
        i += 1

    return [qtdNavesDest,qtdLaserDest]

# Passo 4: segunda função para mover lasers. Nesse caso, para
# mover os lasers das naves.
def moveLasersNaves(matriz):
    ''' (matriz) -> [bool, int]
 
          Recebe a matriz do jogo e move todos os lasers atirados pelas naves
          (caracter definido em LASER_NAVE) uma posição para baixo na matriz.
          Ao mover tem que observar: se saiu do limite da matriz, se atingiu o
          canhão do jogador (caso no qual tem que imprimir um EXPLOSAO no lugar)
          e se atingiu algum laser do jogador. Em todos esses 3 casos, o laser
          movido tem que sumir da matriz. No segundo caso tem que informar que o
          canhão do jogador foi atingido e no terceiro caso tem que atualizar a
          quantidade de lasers atingidos pois a função retorna esses dois
          valores numa lista.
                
          Retorna:
          
          [True se canhão do jogador foi atingido (False se não), quantidade de lasers atingidos]
          
          Obs.: mesmo que o primeiro laser verificado atinja o canhão, tem que
          varrer a matriz **inteira** para atualizar a quantidade de lasers
          atingidos antes de retornar'''

    canhaoVivo = True
    qtdLaserDest = 0
    i = LINHA_MAXIMA
    j = 0
    semLaserNave = True
    while i >= 0:
        j = 0
        while j <= COLUNA_MAXIMA:
            f = matriz[i][j]
            if f == LASER_NAVE:
                if i != LINHA_MAXIMA:
                    g = matriz[i+1][j]
                    if g == CANHAO:
                        matriz[i][j] = ' '
                        matriz[i+1][j] = EXPLOSAO
                        canhaoVivo = False
                    elif g == ' ':
                        matriz[i][j] = ' '
                        matriz[i+1][j] = LASER_NAVE
                    elif g == LASER_CANHAO:
                        qtdLaserDest += 1
                        matriz[i][j] = ' '
                        matriz[i+1][j] = ' '
                if i == LINHA_MAXIMA:
                    matriz[i][j] = ' '                   
                
            j += 1
        i -= 1

        
    if canhaoVivo:
        return [False,qtdLaserDest]
    else:
        return [True,qtdLaserDest] 

# Passo 5: a função que de fato implementa o jogo segundo as regras do
# enunciado. Ela vai chamar toda as funções implementadas nos passos
# anteriores.
def joga(quantidadeNaves):
    ''' int -> [bool, int]
    
          Recebe um inteiro que representa a quantidade de naves, implementa de
          fato o jogo de acordo com as regras do enunciado e retorna uma lista
          com o resultado do jogo:
          
          [resultado, pontuacao]
          
          resultado é uma variável booleana que vale True se o jogador venceu ou
          False se o jogador perdeu.
    
          Para o jogador vencer:
          - O jogador precisa destruir todas as naves
          
          Para o jogador perder:
          - O jogador precisa ser atingido pelo tiro de alguma nave
          - Ou alguma nave precisa alcançar a linha LINHA_MAXIMA da matriz do jogo
          - Ou o jogador precisa ser atingido por alguma nave
    
          pontuacao é uma variável inteira que armazena a quantidade de pontos
          que o jogador fez. A pontuação é definida da seguinte forma:
    
          +PONTOS_ACERTOU_LASER pontos se o jogador consegue acertar 1 tiro em alguma nave
          +PONTOS_ACERTOU_NAVE  pontos se o jogador consegue acertar 1 tiro em algum tiro de alguma nave
    
          A ordem das ações no jogo é:
          - tiros anteriores do jogador se movem
          - imprime o estado do jogo na tela
          - usuário informa se quer atirar ou se mover e a ação escolhida é realizada
          - tiros anteriores das naves se movem
          - naves atiram (de acordo com o sorteio de números aleatórios)
          - naves se movem (de acordo com a rodada - se move apenas nas pares: direita, baixo, esquerda, baixo, direita, etc...
       
          Dentro de cada função de movimentação e de emissão de lasers é
          necessário verificar se houve colisões para aumentar a pontuação, para
          terminar o jogo ou para limpar a tela removendo os elementos que
          sumiram por terem passado do limite da tela (tiros que subiram demais
          e tiros que desceram demais)
    
          Sempre que o jogo terminar, deve imprimir o status final da
          matriz do jogo'''
    
    # Criação da matriz que manterá o estado do jogo.
    matriz = []
    for i in range(LINHA_MAXIMA+1):
        matriz.append([' ']*(COLUNA_MAXIMA+1))
        
    criaElementos(quantidadeNaves, matriz)
    
    # Loop do jogo
    resultado     = VENCEU
    fimDeJogo     = False
    pontos        = 0
    rodada        = 1
    direcaoNaves  = DIREITA
    while not fimDeJogo:

            a = moveLasersCanhao(matriz) #1
            quantidadeNaves -= a[0]
            pontos += PONTOS_ACERTOU_NAVE*a[0]
            pontos += PONTOS_ACERTOU_LASER*a[1]
            if quantidadeNaves == 0:
                fimDeJogo = True
                
            imprimeMatriz (matriz) #2

            if not fimDeJogo:
                açao=input("’e’ para esquerda, ’d’ para direita e ’l’ para emitir laser:") #3
                if açao == "d":
                    vida = moveCanhao(DIREITA,matriz)
                    if vida:
                        fimDeJogo = True
                        resultado: PERDEU
                elif açao == "e":
                    vida = moveCanhao(ESQUERDA,matriz)
                    if vida:
                        fimDeJogo = True
                        resultado: PERDEU
                elif açao == "l":
                    tiro = emiteLaserCanhao(matriz)
                    quantidadeNaves -= tiro[0]
                    pontos += PONTOS_ACERTOU_NAVE*tiro[0]
                    pontos += PONTOS_ACERTOU_LASER*tiro[1]

            if quantidadeNaves == 0:
                fimDeJogo = True

            if not fimDeJogo:   
                tiroNaves = moveLasersNaves(matriz)#4
                if tiroNaves[0]:
                    fimDeJogo = True
                    resultado = PERDEU
                pontos += PONTOS_ACERTOU_LASER*tiroNaves[1]
            
            if not fimDeJogo:
                tiroNaves = emiteLasersNaves(matriz) #5
                if tiroNaves[0]:
                    fimDeJogo = True
                    resultado = PERDEU
                pontos += PONTOS_ACERTOU_LASER*tiroNaves[1]

            if not fimDeJogo:
                if rodada%2 == 0: #6
                    if direcaoNaves == BAIXO:
                        if lim == "direita":
                            naves = moveNaves(direcaoNaves,matriz)
                            direcaoNaves = ESQUERDA
                        if lim == "esquerda":
                           naves = moveNaves(direcaoNaves,matriz)
                           direcaoNaves = DIREITA
                    else:
                        naves = moveNaves(direcaoNaves,matriz)
                    if naves[0]:
                        fimDeJogo = True
                        resultado = PERDEU

                    pontos += PONTOS_ACERTOU_NAVE*naves[2]
                    quantidadeNaves -= naves[2]
                    if naves[1] == ATINGIU_EMBAIXO:
                        fimDeJogo = True
                        resultado = PERDEU
                    elif naves[1] == ATINGIU_DIREITA:
                        direcaoNaves = BAIXO
                        lim = "direita"
                    elif naves[1] == ATINGIU_ESQUERDA:
                        direcaoNaves = BAIXO
                        lim = "esquerda"
                    if quantidadeNaves == 0:
                        fimDeJogo = True
            
            rodada+=1
    imprimeMatriz(matriz)
    return [resultado, pontos]


main()
input()

