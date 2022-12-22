Este código foi feito como um trabalho da disciplina de 
programação do curso de engenharia civil da Poli.

O Objetivo é desembaralhar os pixels de imagens .pgm por meio 
da aplicação da fórmula de transformação inversa à utilizada
no embaralhamento.

Para o funcionamento do programa, basta rodá-lo em qualquer 
diretório e fornecer as seguintes informações:

- Qual o diretório da imagem.pgm a ser tranformada, sempre
terminando em "\". Ex: "C:\Users\DataScience\DecodificadorImagens\"

- Qual o modo:  1 - Transformar apenas uma imagem específica.
		2 - transformar todas as imagens de img00 à img10
		presentes no diretório.

- No modo 1, você também deverá fornecer:
		- Nome do arquivo sem a extensão (.pgm)
		- Nome do arquivo contendo as tranformações sem
		  a extensão (.txt)
		- Nome do arquivo de resultado
		- Número de transformações (quanto maior mais tempo
		  de processamento, mas se for muito baixo pode dar 
		  erro, tente algo em torno de 10)

- No modo 2, você deverá fornecer apenas:
		- Nome do arquivo contendo as tranformações sem
		  a extensão (.txt)
		- Os nomes dos arquivos são padronizados em imgxx,
		  resultadoxx, e as transformações são fixadas em 15