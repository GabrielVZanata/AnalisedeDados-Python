

import pandas as pd
import numpy as np
import seaborn as sns
import warnings
import matplotlib.pyplot as plt


warnings.filterwarnings("ignore")

df = pd.read_json("C:/Users/Gabriel/Desktop/Profissional/DataScience/Projetos/Desafio_DSA/Comportamento_Compra_Consumidores/dados_compras.json", orient = "records")
#print(df.head())


############################ CONTAGEM DE CONSUMIDORES ##################################

#Número Total de Consumidores
info_consumidores = df.loc[:,['Login', 'Idade', 'Sexo']]
#print(info_consumidores.head())

# removendo duplicatas
info_consumidores = df.drop_duplicates('Login')




total_consumidores = info_consumidores.count()[0]
print("O total de consumidores é: ",total_consumidores)
print("")
pd.DataFrame({"Total de Consumidores":[total_consumidores]})



############################ ANÁLISE GERAL DE COMPRAS ##################################

# Número de Itens exclusivos
itens_exclusivos = len(df['Item ID'].unique())
#print (itens_exclusivos)

# Preço médio de compra
preco_medio = df['Valor'].mean()
#print(preco_medio)

# Número de compras 
total_compras = df['Valor'].count()
#print(total_compras)

#Rendimento total (Faturamento)
faturamento = df['Valor'].sum()
#print(faturamento)

#Criação do DataFrame com os dados obtidos

analise_compras = pd.DataFrame({"Número de Itens Únicos" : [itens_exclusivos],
                                "Preço Médio de Compra" : preco_medio,
                                "Número total de Compras" : total_compras,
                                "Faturamento" : faturamento})

#Formatação de Dados

analise_compras = analise_compras.round(2)
analise_compras['Preço Médio de Compra'] = analise_compras['Preço Médio de Compra'].map("${}".format)
analise_compras['Faturamento'] = analise_compras['Faturamento'].map("${}".format)
print("-------------- Análise de Compras --------------")
print(analise_compras)
print("")



################################### INFORMAÇÕES DEMOGRÁFICAS POR GÊNERO ###########################

# Porcentagem e contagem de consumidores masculinos, femininos e outros
qtd_sexo = info_consumidores["Sexo"].value_counts()
porcent_sexo = (qtd_sexo / total_consumidores) * 100 

analise_genero = pd.DataFrame ({"Quantidade por Sexo" : qtd_sexo,
                "Porcentagem por Sexo" : porcent_sexo})

# Formatação de Dados
analise_genero['Porcentagem por Sexo'] = analise_genero['Porcentagem por Sexo'].map("{:.2f} %".format)
print("-------------- Análise de Demografia por Gênero --------------")
print(analise_genero)
print("")

colors = ["#00e600", "#ff8c1a","#a180cc"]
g = sns.catplot(x="Sexo", palette="husl", kind="count", data=info_consumidores)
g.ax.set_title("Demografia dos Compradores",fontdict= {'size':12})
g.ax.xaxis.set_label_text("Gênero",fontdict= {'size':14})
g.ax.yaxis.set_label_text("Quantidade de Compradores",fontdict= {'size':14})

for p in g.ax.patches:
    g.ax.annotate((p.get_height()), (p.get_x()+0.3, p.get_height()+5))

plt.show()

################################## ANÁLISE DE COMPRAS POR GÊNERO ####################################

# número de compras por gênero
qtd_compras_sexo = df["Sexo"].value_counts()
#print(qtd_compras_sexo)
porcent_compras_sexo = (qtd_compras_sexo / total_compras) * 100
#print(porcent_compras_sexo)

# preço médio de compra por gênero
preco_medio_sexo = df.groupby(["Sexo"]).mean()["Valor"].rename("Valor Médio")
#print(preco_medio_sexo)

# faturamento por gênero
faturamento_sexo = df.groupby(["Sexo"]).sum()["Valor"].rename("Faturamento por Sexo")

# Faturamento médio por consumidor por sexo
faturamento_normalizado_sexo = faturamento_sexo/qtd_sexo
#print (faturamento_normalizado_sexo)

# Gerando DataFrame análise de compras por gênero
analise_compras_genero = pd.DataFrame({"Total de Compras por Gênero" : qtd_compras_sexo,
                                    "Preço Médio por Gênero" : preco_medio_sexo,
                                    "Faturamento por Gênero" : faturamento_sexo,
                                    "Faturamento por Consumidor" : faturamento_normalizado_sexo})
#print(analise_compras_genero)

# Formatação de Dados
analise_compras_genero["Preço Médio por Gênero"] = analise_compras_genero["Preço Médio por Gênero"].map("${:.2f}".format)
analise_compras_genero["Faturamento por Gênero"] = analise_compras_genero["Faturamento por Gênero"].map("${:.2f}".format)
analise_compras_genero["Faturamento por Consumidor"] = analise_compras_genero["Faturamento por Consumidor"].map("${:.2f}".format)

print("-------------- Análise de Compras por Gênero --------------")
print(analise_compras_genero)
print("")

# Compras por Faixa Etária
bins = [0, 9.99, 14.99, 19.99, 24.99, 29.99, 34.99, 45]
labels_bracket = ["Menos de 10", "10 à 15", "15 à 20", "20 à 25", "25 à 30", "30 à 35", "Maior que 35"]
df["Range de Idades"] = pd.cut(df['Idade'], bins, labels = labels_bracket)

# total de compras por idade
total_compras_idade = df.groupby(['Range de Idades']).count()['Valor']

# porcentagem de compras por idade
porcent_compras_idade = (total_compras_idade/total_consumidores) * 100

# média de preço por idade
preco_medio_idade = df.groupby(['Range de Idades']).mean()['Valor']

# faturamento por idade
faturamento_idade = df.groupby(['Range de Idades']).sum()['Valor']

# faturamento por idade normalizado
faturamento_normalizado_idade = faturamento_idade/total_compras_idade

# Criando o Data Frame de análise etária

analise_compras_idade = pd.DataFrame({"Total de Compras" : total_compras_idade,
                                    "Porcentagem de Compras" : porcent_compras_idade,
                                    "Preço Médio" : preco_medio_idade,
                                    "Faturamento" : faturamento_idade,
                                    "Faturamento por Consumiodor" : faturamento_normalizado_idade})


# Formatando os dados

analise_compras_idade ["Porcentagem de Compras"] = analise_compras_idade ["Porcentagem de Compras"].map("{:.2f} %".format)
analise_compras_idade ["Preço Médio"] = analise_compras_idade ["Preço Médio"].map("$ {:.2f}".format)
analise_compras_idade ["Faturamento"] = analise_compras_idade ["Faturamento"].map("$ {:.2f}".format)
analise_compras_idade ["Faturamento por Consumiodor"] = analise_compras_idade ["Faturamento por Consumiodor"].map("$ {:.2f}".format)

print("-------------- Análise de Compras por Idade --------------")
print(analise_compras_idade)
print("")

######################################## TOP 5 COMPRADORES #################################################

# Quantidade de compras por Login
total_compras_login = df.groupby(["Login"]).count()["Valor"]

# Média de Compras por Login 
preco_medio_login = df.groupby(["Login"]).mean()["Valor"]

#Quantidade de Compras por Login
faturamento_login = df.groupby(["Login"]).sum()["Valor"]

# Criando o DataFrame
analise_compras_login = pd.DataFrame({"Total de Compras" : total_compras_login,
                                    "Valor Médio" : preco_medio_login,
                                    "Faturamento" : faturamento_login})

#Formatando os Dados

analise_compras_login ["Valor Médio"] = analise_compras_login ["Valor Médio"].map("$ {:.2f}".format)
analise_compras_login ["Faturamento"] = analise_compras_login ["Faturamento"].map("$ {:.2f}".format)

#print(analise_compras_login)

analise_compras_login = analise_compras_login.sort_values(by=["Faturamento"],ascending=False)

print("-------------- Top 5 Compradores --------------")
print(analise_compras_login.head(5))
print("")

# Itens Mais populares 
total_compras_item = df.groupby(["Nome do Item"]).count()["Valor"]
porcent_compras_item = (total_compras_item / total_compras) * 100
faturamento_item = df.groupby(["Nome do Item"]).sum()["Valor"]

analise_compras_item = pd.DataFrame({"Número de Compras" : total_compras_item,
                                    "Porcentagem de Compras" : porcent_compras_item,
                                    "Faturamento" : faturamento_item})

analise_compras_item ["Porcentagem de Compras"] = analise_compras_item ["Porcentagem de Compras"].map("{:.2f} %".format)
analise_compras_item ["Faturamento"] = analise_compras_item ["Faturamento"].map("$ {:.2f}".format)

analise_compras_item = analise_compras_item.sort_values(by=["Número de Compras"], ascending = False)


print("-------------- Top 5 Produtos por Quantidade de Compras --------------")
print(analise_compras_item.head(5))
print("")

analise_faturamento_item = analise_compras_item
analise_faturamento_item ["Faturamento"] = analise_faturamento_item ["Faturamento"].apply(lambda x: x.strip("$ ")).apply(lambda x: float(x))
analise_faturamento_item = analise_faturamento_item.sort_values(by=["Faturamento"], ascending = False)
analise_faturamento_item ["Faturamento"] = analise_faturamento_item ["Faturamento"].apply(lambda x: "$ " + str(x))
analise_faturamento_item = analise_faturamento_item.iloc[:,[2,1,0]]

print("-------------- Top 5 Produtos Mais Lucrativos --------------")
print(analise_faturamento_item.head(5))
print("")
