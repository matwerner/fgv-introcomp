# NumPy

## 1. Introdução ao NumPy

### O que é o NumPy?
O NumPy é uma biblioteca poderosa para computação numérica em Python.
Ele fornece suporte para arrays, matrizes e muitas funções matemáticas para operar nessas estruturas de dados.
O NumPy é essencial para ciência de dados, aprendizado de máquina e computação científica devido à sua eficiência e desempenho.

### Importância e Aplicações
- **Ciência de Dados**: Manipulação e análise de dados eficientes.
- **Aprendizado de Máquina**: Manipulação de grandes conjuntos de dados e execução de operações matriciais.
- **Computação Científica**: Resolução de problemas matemáticos complexos.

## 2. Instalação e Configuração

### Instalando o NumPy
Você pode instalar o NumPy usando o `pip`:
```bash
pip install numpy
```

Ou usando o conda:
```bash
conda install numpy
```

### Importando o NumPy
É uma convenção comum importar o NumPy com o alias np:
```python
import numpy as np
```

## 3. Conceitos Básicos dos Arrays do NumPy

### Criação de Arrays

```python
# A partir de listas ou tuplas:
array = np.array([1, 2, 3])

# Usando funções
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
full = np.full((2, 3), 7)
arange = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)
```

### Atributos do Array

```python
array.shape    # Forma (Shape): Número de dimensões e tamanho de cada dimensão
array.size     # Tamanho (Size): Número total de elementos
array.ndim     # Número de Dimensões
array.dtype    # Tipo de Dados (Data Type)
array.itemsize # Tamanho do Item: Tamanho de cada elemento em bytes
array.nbytes   # Total de Bytes Consumidos
```

## 4. Indexação e Fatiamento de Arrays

```python
# Indexação e Fatiamento Básico
element = array[0, 1]             # Acessando elementos
slice = array[0:2, 1:3]           # Fatiando arrays

# Indexação Avançada
bool_idx = array[array > 0]       # Indexação booleana
fancy_idx = array[[0, 1], [1, 0]] # Indexação avançada usando arrays de inteiros
```

## 5. Manipulação de Arrays

```python
# Remodelando Arrays
reshaped = array.reshape((3, 2))
flattened = array.flatten()
raveled = array.ravel()

# Unindo Arrays
concatenated = np.concatenate((array1, array2), axis=0)
vstacked = np.vstack((array1, array2))
hstacked = np.hstack((array1, array2))

# Dividindo Arrays
split = np.split(array, 2, axis=0)
hsplit = np.hsplit(array, 2)
vsplit = np.vsplit(array, 2)
```

## 6. Funções Universais (ufuncs)

```python
# Operações aritméticas básicas:
sum_array = np.add(array1, array2)
diff_array = np.subtract(array1, array2)
prod_array = np.multiply(array1, array2)
quot_array = np.divide(array1, array2)

# Funções trigonométricas:
sine = np.sin(array)
cosine = np.cos(array)
tangent = np.tan(array)

# Funções exponenciais e logarítmicas:
exp = np.exp(array)
log = np.log(array)

# Funções de Agregação
total = np.sum(array)
mean_value = np.mean(array)
minimum = np.min(array)
maximum = np.max(array)
min_index = np.argmin(array)
max_index = np.argmax(array)
```

### Exercícios

Criação de Arrays:

* Crie um array unidimensional com números de 1 a 10.
* Crie uma matriz 3x3 com todos os elementos sendo 0.
* Crie uma matriz identidade 4x4.

Indexação e Fatiamento:

* A partir do array unidimensional criado no exercício 1, selecione apenas os elementos pares.
* Crie uma matriz 5x5 com números de 1 a 25 e, em seguida, selecione a diagonal principal.
* A partir da matriz identidade criada no exercício 1, altere os elementos da segunda linha para 1.

Sudoku

* Refaça a questão 5 da lista 2 (Aula 10)