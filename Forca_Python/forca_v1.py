# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.point = 0
		self.tentativas_erradas = []
		self.palavras_lista = [x for x in word]
		self.board_word = ['_' for x in word]

		
	# Método para adivinhar a letra
	def guess(self, letter):
		ponto = 0
		for i in range(0,len(self.palavras_lista)):
			if letter == self.palavras_lista[i]:
				self.board_word[i] = letter
				ponto += 1
		if ponto == 0:
			self.tentativas_erradas.append(letter)
			self.point += 1
			

		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		if self.point == 6:
			return True
		else:
			return False
		

	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if self.board_word == self.palavras_lista:
			return True
		
		else:
			return False

	# Método para não mostrar a letra no board
	#def hide_word(self):
		
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print (board[self.point])

		board_str = ''
		for i in self.board_word:
			board_str += i
		print ('Palavra: ', board_str)
		print ('\n')

		tenta_err = ''
		for i in self.tentativas_erradas:
			tenta_err += i
		print ('Tentativas erradas: ', tenta_err)
		#print ('Erros: ', self.point)

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("C:\\Users\Gabriel\Desktop\Profissional\DataScience\Projetos\Forca\Lab03\palavras.txt", "rt") as f:
            bank = f.readlines()
	    
			
        return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	play = True

	while play:
		game.print_game_status()

		if game.hangman_over() == True:
			play = False
		elif game.hangman_won() == True:
			play = False
		else:
			valid = False
			while not valid:
				letter = str (input ("Digite uma letra: "))
				if letter in game.board_word:
					print ('Você já tentou esta letra. Tente outra.')
				elif letter not in game.tentativas_erradas:
					valid = True
				else:
					print ('Você já tentou esta letra. Tente outra.')
			game.guess(letter)



	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	elif game.hangman_over():
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()

