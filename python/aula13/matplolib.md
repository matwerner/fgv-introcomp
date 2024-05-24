# Matplotlib

## 1. Introdução ao Matplotlib

O Matplotlib é uma biblioteca popular em Python utilizada para criação de visualizações de dados.
Ele oferece uma vasta gama de funcionalidades para criar gráficos estáticos, interativos e animados.

## 2. Conceitos básicos

### 2.1. Criação de Gráficos Básicos

* O Matplotlib funciona em uma abordagem de "Figura e Eixos".
* Uma Figura é a área na qual os gráficos são desenhados.
* Os Eixos são os eixos coordenados onde os dados são plotados.

### 2.2. Estrutura Geral de um Gráfico

```python
import matplotlib.pyplot as plt

# Criando dados
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Criando uma figura e eixos
fig, ax = plt.subplots()

# Plotando dados nos eixos
ax.plot(x, y)

# Exibindo o gráfico
plt.show()
```

## 3. Trabalhando com Figuras e Eixos

### 3.1. Criação de Figuras e Eixos

* Podemos criar figuras e eixos no Matplotlib de várias maneiras.
* Uma maneira comum é usar o método `plt.subplots()`, que retorna uma tupla contendo a figura e uma matriz de eixos.
* Ao criar figuras e eixos usando `plt.subplots()`, podemos especificar o número de linhas e colunas de eixos desejados.
* Os eixos criados podem ser personalizados e manipulados individualmente para adicionar dados, alterar propriedades, etc.
* Outra maneira é criar diretamente um plot usando métodos como `plt.plot()`, `plt.bar()`, `plt.scatter()`, entre outros. Quando usamos esses métodos diretamente, o Matplotlib cria automaticamente uma figura e um conjunto de eixos para o plot.

Exemplo de criação de figuras e eixos com plt.plot():

```python
import matplotlib.pyplot as plt

# Dados
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Criando um gráfico de linha diretamente
plt.plot(x, y)

# Exibindo o gráfico
plt.show()
```

Neste exemplo, o método plt.plot() é usado para criar um gráfico de linha diretamente,
sem a necessidade de criar explicitamente uma figura ou eixos.
O Matplotlib cria automaticamente uma figura e um conjunto de eixos para o plot e adiciona os dados especificados.

### 3.2. Personalização dos Gráficos

* Ao criar gráficos com o Matplotlib, podemos personalizá-los de várias maneiras,
incluindo adição de título, rótulos de eixos, legendas, cores, estilos de linha, etc.
* Para adicionar título ao gráfico, usamos o método `plt.title()`, onde passamos o título desejado como argumento.
* Os rótulos dos eixos x e y podem ser adicionados com os métodos `plt.xlabel()` e `plt.ylabel()`, respectivamente, onde passamos os rótulos desejados como argumentos.
* Para adicionar uma legenda ao gráfico, usamos o método `plt.legend()`, onde passamos uma lista de strings representando os rótulos de cada série de dados.
* A cor da linha ou das barras pode ser personalizada usando o argumento color nos métodos de plotagem, onde podemos especificar uma cor nomeada (por exemplo, `'red'`, `'blue'`, `'green'`) ou um código hexadecimal (por exemplo, `'#FF5733'`) para a cor desejada.

```python
import matplotlib.pyplot as plt

# Dados
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 9, 16, 25]

# Criando o gráfico de linha
plt.plot(x, y1, label='Série 1', color='blue')  # Definindo cor azul para a série 1
plt.plot(x, y2, label='Série 2', color='red')   # Definindo cor vermelha para a série 2

# Adicionando título e rótulos de eixos
plt.title('Gráfico com Rótulos e Cores Personalizadas')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adicionando legenda
plt.legend()

# Exibindo o gráfico
plt.show()
```

Neste exemplo, cada série de dados tem um rótulo associado e uma cor personalizada atribuída.
A legenda é adicionada automaticamente com base nos rótulos fornecidos.

### 3.3. Manipulação dos Eixos

* Podemos definir os limites dos eixos usando `ax.set_xlim()` e `ax.set_ylim()`.
* Podemos alterar os ticks e rótulos dos eixos usando `ax.set_xticks()`, `ax.set_yticks()`, `ax.set_xticklabels()` e `ax.set_yticklabels()`.

3.4. Salvando o Gráfico:

* Além de exibir o gráfico na tela, o Matplotlib oferece a capacidade de salvar os gráficos criados em diferentes formatos de arquivo, como PNG, PDF, SVG, etc.
* Podemos usar o método `plt.savefig()` para salvar o gráfico atual em um arquivo. Este método aceita um argumento `filename` para especificar o nome do arquivo.
* Além disso, podemos usar o argumento opcional format para especificar o formato do arquivo (por exemplo, `'png'`, `'pdf'`, `'svg'`, etc.).
* Podemos também especificar a resolução da imagem salva usando o argumento opcional dpi (dots per inch, pontos por polegada). Quanto maior o valor de DPI, maior será a resolução da imagem e maior será o tamanho do arquivo.

Exemplo de salvar o gráfico em formato PNG com DPI 300:

```python
import matplotlib.pyplot as plt

# Dados
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Criando o gráfico
plt.plot(x, y)

# Personalizando o gráfico
plt.title('Gráfico de Exemplo')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Salvando o gráfico em formato PNG com DPI 300
plt.savefig('grafico_exemplo.png', format='png', dpi=300)

# Exibindo o gráfico
plt.show()
```

## 4. Exemplos de Gráficos

### 4.1. Linha
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure()
plt.plot(x, y)
plt.title('Gráfico de Linha')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()
```

### 4.2. Barra
```python
import matplotlib.pyplot as plt

x = ['A', 'B', 'C', 'D', 'E']
y = [10, 20, 15, 25, 30]

plt.figure()
plt.bar(x, y)
plt.title('Gráfico de Barra')
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.show()
```

### 4.3. Dispersão
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(100)
y = np.random.randn(100)

plt.figure()
plt.scatter(x, y)
plt.title('Gráfico de Dispersão')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()
```

## 5. Configurando Limites nos Eixos:

Podemos configurar os limites nos eixos x e y usando `ax.set_xlim()` e `ax.set_ylim()`:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure()
plt.plot(x, y)
plt.xlim(0, 6)
plt.ylim(0, 12)
plt.title('Gráfico com Limites nos Eixos')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()
```

## 6. Adicionando Vários Gráficos com Subplots

Podemos adicionar vários gráficos em uma única figura usando subplots:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 9, 16, 25]

fig, axs = plt.subplots(2)

axs[0].plot(x, y1)
axs[0].set_title('Gráfico 1')
axs[1].plot(x, y2)
axs[1].set_title('Gráfico 2')

plt.show()
```

## Exercícios

### 1. Criar um Gráfico de Seno:

* Escreva um código Python utilizando o Matplotlib para criar um gráfico de linha representando a função seno no intervalo de 0 a 2π.
* Personalize o gráfico adicionando título, rótulos de eixos e uma legenda, se necessário.
* Exiba o gráfico na tela.

### 2. Criar um Gráfico de Barras:

* Escreva um código Python utilizando o Matplotlib para criar um gráfico de barras representando a quantidade de vendas de diferentes produtos em um determinado mês.
* Utilize uma lista de produtos como eixo x e suas respectivas quantidades vendidas como eixo y.
* Personalize o gráfico adicionando título, rótulos de eixos e cores distintas para as barras.
* Exiba o gráfico na tela.