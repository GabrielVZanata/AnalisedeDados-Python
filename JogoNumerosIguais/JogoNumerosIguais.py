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

  Nome : GABRIEL VALVERDE ZANATA DA SILVA
  NUSP : 10774799
  Turma: 05
  Prof.: FUJITA

  """

# FUNÇÕES PARA GERAÇÃO DO NÚMERO ALEATÓRIO:
def congr(x) :
    a=22695477
    b=1
    m=2**32
    res = (a*x+b)%(m)
    return res

def random(res):
    if res <= 2**31:
        rand = 0
    else:
        rand = 1
    return rand

#FUNÇÃO DE FUNCIONAMENTO DO JOGO        
def main():
    Lance00 = 0
    Lance01 = 0
    Lance10 = 0
    Lance11 = 0
    Lance_Ant = 0
    res = 3
    
   

    Ponto_Maq = 0
    Ponto_Jog = 0
    N_01 = 0
    Dificuldade = int(input("Escolha o tipo de jogo (1: Facil; 2: Dificil):"))
    JogTotal = int(input("Entre com o numero de jogadas:"))
    JogAtual = 1

    #MODO FÁCIL
    if Dificuldade <= 1 : 
        Dificuldade = 1

        while JogAtual <= JogTotal :
                N_01 = int(input("\nFaca sua %da jogada:"%(JogAtual)))
                res = congr(res)
                Num_Random = random(res)
                Num_Maq = Num_Random
                print ("jogador = ",N_01,end="")
                print (" maquina = ",Num_Maq,end="")
                JogAtual += 1

                #Placar
                if Num_Maq == N_01 :
                    Ponto_Maq += 1 
                    print (" Maquina ganha!")
                    
                    print ("JOGADOR: ", end="")
                    i = 0
                    while i < Ponto_Jog:
                        print ("*", end="")
                        i += 1
                    print ("\nMAQUINA: ", end="")
                    i = 0
                    while i < Ponto_Maq:
                        print ("*", end="")
                        i += 1

                else :
                    Ponto_Jog += 1
                    print (" Jogador ganha!")

                    print ("JOGADOR: ", end="")
                    i = 0
                    while i < Ponto_Jog:
                        print ("*", end="")
                        i += 1
                    print ("\nMAQUINA: ", end="")
                    i = 0
                    while i < Ponto_Maq:
                        print ("*", end="")
                        i += 1

        #Placar Final
        if Ponto_Maq > Ponto_Jog :
                print ("\nA maquina venceu!")
        elif Ponto_Maq == Ponto_Jog:
                print ("\nDeu empate!")
        else :
                print ("\nVoce venceu!")
        input("")

    #MODO DIFÍCIL
    else :
        Dificuldade = 2

        while JogAtual <= JogTotal :
                Lance_Ant = N_01
                N_01 = int(input("\nFaca sua %da jogada:"%(JogAtual)))
                res = congr(res)
                Num_Random = random(res)
                
                if JogAtual > 1:
                    
                #Tomada de atitude da maquina:
                    if Lance_Ant == 0:
                        if Lance10 > Lance00:
                            Num_Maq = 1
                        elif Lance10 < Lance00:
                            Num_Maq = 0
                        else:
                            Num_Maq = Num_Random
                            
                    else:
                        if Lance11 > Lance01:
                            Num_Maq = 1
                        elif Lance11 < Lance01:
                            Num_Maq = 0
                        else:
                            Num_Maq = Num_Random
                            
                #Contagem de jogadas do jogador:
                    if Lance_Ant == 0:
                        if N_01 == 0:
                            Lance00 += 1
                        else:
                            Lance10 += 1
                            
                    else:
                        if N_01 == 0:
                            Lance01 += 1
                        else:
                            Lance11 += 1
            
                else:
                    
                    Num_Maq = Num_Random
                
                print ("jogador: ",N_01,end="")
                print (" maquina: ",Num_Maq,end="")
                JogAtual += 1

                #Placar
                if Num_Maq == N_01 :
                    Ponto_Maq += 1 
                    print (" Maquina ganha!")

                    print ("JOGADOR: ", end="")
                    i = 0
                    while i < Ponto_Jog:
                        print ("*", end="")
                        i += 1
                    print ("\nMAQUINA: ", end="")
                    i = 0
                    while i < Ponto_Maq:
                        print ("*", end="")
                        i += 1
                    
                else :
                    Ponto_Jog += 1
                    print (" Jogador ganha!")

                    print ("JOGADOR: ", end="")
                    i = 0
                    while i < Ponto_Jog:
                        print ("*", end="")
                        i += 1
                    print ("\nMAQUINA: ", end="")
                    i = 0
                    while i < Ponto_Maq:
                        print ("*", end="")
                        i += 1
   

        #Placar Final
        if Ponto_Maq > Ponto_Jog :
                print ("\nA maquina venceu!")
        elif Ponto_Maq == Ponto_Jog:
                print ("\nDeu empate!")
        else :
                print ("\nVoce venceu!")
        input("")

main()
