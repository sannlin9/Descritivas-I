#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# ### 1) Alturas  
# i. No trecho de código abaixo, crie um ndarray chamado ```altura_em_centimetros``` transformando a lista ```lista_de_alturas``` em um ndarray do numpy com a função ```np.array()```  
# ii. Crie um outro objeto ```altura_em_metros```, com os valores de ```altura_em_centimetros``` convertidos para metros.

# In[2]:


lista_de_centimetros = list(range(170, 190, 5))
lista_de_centimetros


# In[3]:


altura_em_centimetros = np.array(lista_de_centimetros)
altura_em_centimetros


# In[4]:


altura_em_metros = altura_em_centimetros /100
altura_em_metros


# ### 2) IMC  
# i. Considere que pesos em Kg dessas pessoas, na mesma ortem, estão na lista pesos ```lista_pesos = [70, 75, 80, 85]```. Crie um **ndarray** chamado ```pesos``` com a função ```np.array()``` que contenha esses valores.  
# ii. Utilizando o objeto que contém as alturas em metros e esse objeto que contém os respectivos pesos em quilos, calcule o IMC desses indivíduos utilizando a aritmética de arrays e guarde os resultados em um objeto chamado ```imc```.

# In[5]:


lista_pesos = [70, 75, 80, 85]
lista_pesos
# seu código aqui
pesos = np.array(lista_pesos)
pesos


# In[6]:


# calcule o IMC dessas pessoas

imc = pesos / (altura_em_metros**2)
imc


# ### 3) Endividamento
# 
# Cálculos de novas variáveis como endividamento total e comprometimento de renda são essenciais para a construção de modelos financeiros em ciência de dados. Áreas não financeiras terão cálculos semelhantes também. Vamos praticar:
# 
# Considere que o seguinte ndarray contém os dados de 4 pessoas, total a ser pago a empréstimos mensalmente e renda familiar:
# 
# | custo fixo | dívida financeira | renda familiar |
# |:----:|:----:|:---|
# | 3000  | 1000 | 6000 |
# | 2500  | 2500 | 5500 |
# | 1000  | 3000 | 7000 |
# | 10000 | 5000 | 16000 |
# 
# i. Transforme a lista de listas ```dados_financeiros``` no ndarray ```nd_financeiros```.
# > ``` dados_financeiros[[3000, 2500, 1000, 10000],[1000, 2500, 3000, 5000],[6000, 5500, 7000, 16000]] ```
# 
# ii. Utilize o método ```.transpose ``` e certifique-se de que esse ndarray tenha uma linha por indivíduo e uma coluna por informação. Utilizando a indexação do numpy, imprima no output a segunda linha do array, depois a segunda coluna.
# 
# iii. Pratique aritmética com nearrays e calcule o endividamento total como:
# $$endividamento\hspace{.2cm}total = \frac{custo \hspace{.2cm}fixo + dívida\hspace{.2cm}financeira}{renda\hspace{.2cm}familiar}$$
# Guarde os resultados em uma variável chamada ```endividamento_total``` e verifique os resultados imprimindo o conteúdo dessa variável no output.
# 
# iv. Considere que há um erro de digitação que precisa ser corrigido: 3o indivíduo na verdade não possui renda familiar de R\\$7.000,00, mas sim R\\$ 10.000,00. Corrija esse valor e refaça os cálculos.

# In[7]:


# lista dados_financeiros
dados_financeiros = [[3000, 2500, 1000, 10000],[1000, 2500, 3000, 5000],[6000, 5500, 7000, 16000]]
dados_financeiros
#i) transforme essa lista em um ndarray

nd_financeiros = np.array(dados_financeiros)
nd_financeiros


# In[8]:


# ii) Utilize o método .transpose e certifique-se de que esse ndarray tenha uma linha por indivíduo e uma coluna por informação. 
# Utilizando a indexação do numpy, imprima no output a segunda linha do array, depois a segunda coluna.

trans_financeiros = nd_financeiros.transpose()
trans_financeiros


# In[9]:


trans_financeiros[1,:] #imprima no output a segunda linha do array


# In[10]:


trans_financeiros[:,1] #segunda coluna.


# In[11]:


# iii) Calcule o endividamento total
custo_fixo = trans_financeiros[:,0]
divida = trans_financeiros[:,1]
renda = trans_financeiros[:,2]
total = (custo_fixo + divida) / renda


# In[12]:


total


# In[13]:


# iv) corrigindo um valor específico
trans_financeiros[2,2] = 10000


# In[14]:


trans_financeiros


# ### 4) É muito comum precisarmos identificar valores especiais e darmos tratamento a eles quer seja alterando-os quer seja descartando-os. 
# 
# O trecho de código abaixo gera um ndarray com números pseudo aleatórios. Considere que para efeitos do estudo que virá, devemos desconsiderar valores iguais a zero. Sendo assim:
# 
# i) crie um objeto ```bool_zero``` que traga uma sequencia de booleanos do mesmo tamanho que o objeto poi, e que vale ```True``` quando o valor de ```poi``` é zero, e ```False``` caso contrário.
# 
# ii) Conte quantos valores zero existem. Lembre-se de que no final das contas, ```True``` vale 1 para o Python, e ```False``` vale zero, então uma boa dica seria usar a função ```sum()```.
# 
# iii) Utilize a indexação booleana que você aprendeu para criar uma variável ```poi_nao_zero``` que aponta para os elementos de ```poi``` diferentes de zero. Dica: você vai pode inverter os elementos do objeto que criou em *ii)* ou escrever a comparação adequada.

# In[15]:


# objeto poi - obs: o comando np.random.seed(1234) garante que o mesmo resultado será gerado sempre
np.random.seed(1234)
poi = np.random.poisson(3, 100)
poi


# In[16]:


# i) crie o objeto bool_zero através do operador == 
# True quando o valor de poi é zero, e False caso contrário.
bool_zero = poi == 0
bool_zero


# In[17]:


bool_zero == poi 


# In[18]:


# ii) Conte a quantidade de zeros (ou some os elementos de bool_zero)

sum (bool_zero)


# In[19]:


# iii) utilize a indexação booleana para criar uma seleção de não-zeros
# dica: inverta o objeto bool_zero

bool_nao_zero = poi != 0
bool_nao_zero


# In[20]:


poi[bool_nao_zero]

