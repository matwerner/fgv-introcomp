# LaTeX

## Introdução

LaTeX é um sistema de preparação de documentos de alta qualidade, amplamente utilizado para a produção de documentos técnicos e científicos, como artigos acadêmicos, relatórios, teses, livros, apresentações e cartas. Em vez de se concentrar na formatação visual do documento, como em editores de texto convencionais, o LaTeX permite que os autores se concentrem no conteúdo, enquanto o sistema cuida da formatação e da apresentação.

Basicamente, LaTeX é um conjunto de macros baseado no sistema de formatação de documentos TeX, desenvolvido por Leslie Lamport na década de 1980. Ele oferece uma maneira poderosa e flexível de criar documentos com alta qualidade tipográfica e suporte completo para fórmulas matemáticas complexas, referências cruzadas, índices, bibliografias automatizadas e muito mais.

<!-- LaTeX é um sistema de preparação de documentos desenvolvido na década de 1980 por Leslie Lamport.
Reconhecido pela sua capacidade de gerar documentos de alta qualidade, ele é amplamente utilizado na produção de textos técnicos e científicos, como artigos acadêmicos, relatórios, teses, livros, apresentações e correspondências.
Ao contrário dos editores de texto convencionais, que se concentram na formatação visual do documento, o LaTeX permite que os autores se concentrem no conteúdo, enquanto o sistema cuida da formatação e apresentação. -->

## Razões para se utilizar LaTeX

Embora Microsoft Word e Google Docs possam atender satisfatoriamente a necessidades de documentos com poucas páginas, como relatórios simples, sua eficácia diminui consideravelmente ao lidar com documentos extensos, contendo dezenas ou centenas de páginas.

Ao optar pelo LaTeX, usufruímos de uma série de vantagens:

* **Eliminação de Distrações com Formatação**: A preocupação com a formatação é minimizada, permitindo que os autores se concentrem exclusivamente no conteúdo do documento.
* **Numeração Automática de Elementos**: Seções, tabelas, figuras e outros elementos são numerados automaticamente, facilitando a organização e referência dentro do documento.
* **Facilidade de Formatação**: A sintaxe do LaTeX simplifica o processo de formatação, proporcionando controle preciso sobre a apresentação do texto.
* **Portabilidade**: Os documentos LaTeX podem ser facilmente compartilhados e visualizados em diferentes sistemas operacionais e dispositivos.
* **Comunidade Ativa**: Uma vasta comunidade de usuários e desenvolvedores contribui para o suporte e aprimoramento contínuo do LaTeX, fornecendo recursos, dicas e soluções para os usuários.
* **Suporte a Equações**: O LaTeX oferece recursos poderosos para a composição de equações matemáticas complexas, tornando-o uma escolha preferida para documentos científicos e técnicos.
* **Gestão de Referências**: O LaTeX facilita a criação e formatação de listas de referências bibliográficas de maneira automatizada e organizada.
* **Templates Pré-Definidos**: Uma ampla variedade de templates pré-configurados está disponível para diversos tipos de documentos, agilizando o processo de criação e garantindo uma aparência profissional.


## Como instalar?

Instalar principais pacotes relacionados ao LaTex:
```bash
sudo apt-get install texlive-full
```

Instalar um editor de Latex como TexMaker ou TexStudio:
```bash
sudo apt-get install texmaker
sudo apt-get install texstudio
```

... ou simplesmente usar [Overleaf](https://pt.overleaf.com/).

## Estrutura básica de um documento LaTeX

Um documento LaTeX é composto por uma série de comandos, que são utilizados para definir a formatação e o conteúdo do documento.
Abaixo está um exemplo de um documento LaTeX básico.

```tex
\documentclass{article}
\begin{document}
    Primeiro documento.  Este é um exemplo simples,
    sem parâmetros extras ou pacotes incluídos.
\end{document}
```

### Estrutura básica

```tex
\documentclass[12pt,a4paper]{article}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[portuguese]{babel}

\title{Minha Aula de Introdução ao LaTeX}
\author{Seu Nome}
\date{\today}

\begin{document}

\maketitle

% Conteúdo do documento aqui

\end{document}
```

### Texto e Formatação

#### Parágrafos, Quebras de Linha e Espaçamento:

```tex
Este é o primeiro parágrafo.

Este é o segundo parágrafo, com uma quebra de linha forçada. \\
E aqui está outra linha no segundo parágrafo.

\vspace{\baselineskip} % Adiciona um espaçamento de uma linha em branco
Este é o terceiro parágrafo, com espaçamento adicional.
```

#### Negrito, Itálico e Sublinhado:

```tex
\textbf{Texto em negrito} \\
\textit{Texto em itálico} \\
\underline{Texto sublinhado}
```

#### Tamanhos de Fonte

```tex
{\tiny Texto em tamanho tiny} \\
{\Large Texto em tamanho Large} \\
{\Huge Texto em tamanho Huge}
```

#### Listas

```tex
\begin{itemize}
    \item Item 1
    \item Item 2
    \item Item 3
\end{itemize}

\begin{enumerate}
    \item Primeiro item
    \item Segundo item
    \item Terceiro item
\end{enumerate}
```


### Imagens

```tex
\includegraphics{imagem.png}
\includegraphics[width=0.5\textwidth]{imagem.png} % Escala para 50% da largura do texto
```


### Tabelas

```tex
\begin{tabular}{|c|c|c|}
    \hline
    Coluna 1 & Coluna 2 & Coluna 3 \\
    \hline
    Dado 1 & Dado 2 & Dado 3 \\
    Dado 4 & Dado 5 & Dado 6 \\
    \hline
\end{tabular}

\begin{tabular}{|c||c|c|}
    \hline
    \multicolumn{3}{|c|}{Título da Tabela} \\
    \hline
    Coluna 1 & Coluna 2 & Coluna 3 \\
    \hline
    Dado 1 & Dado 2 & Dado 3 \\
    \hline
    Dado 4 & Dado 5 & Dado 6 \\
    \hline
\end{tabular}
```

### Matemática

## Exercícios

1. Crie um documento LaTeX com um título e um parágrafo.
2. Crie um documento LaTeX com uma lista não ordenada e uma lista ordenada.
3. Crie um documento LaTeX com uma tabela.
4. Crie um documento LaTeX com uma imagem.
5. Crie um documento LaTeX com a equação da média de uma sequeẽncia de números $X = {x_0, \dots, x_n}$:
$$ x_\mu = \frac{\sum_{i=0}^{n} x_i}{n} $$


