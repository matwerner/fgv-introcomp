# Bibliotecas

Além de módulos e pacotes, também temos o conceito de bibliotecas.
Uma biblioteca em Python é um conjunto de módulos e pacotes que são distribuídos e instalados em conjunto para resolver problemas específicos ou oferecer funcionalidades adicionais.

## Instalando

Existem várias maneiras de instalar bibliotecas.
A maneira mais comum é usar o gerenciador de pacotes `pip` (Pip Install Packages).

Por exemplo, para instalar a biblioteca `requests`, que é comumente usada para fazer solicitações HTTP, você pode usar o seguinte comando no terminal:
```bash
pip install requests
```

Isso baixará e instalará a biblioteca `requests` juntamente com suas dependências no ambiente Python.

## Usando

Depois de instalar uma biblioteca, você pode usá-la em seus programas Python da mesma maneira que usa módulos e pacotes.
Por exemplo, para usar a biblioteca requests para fazer uma solicitação HTTP, você pode fazer o seguinte:

```python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # Saída: 200
```

Neste exemplo, importamos a biblioteca `requests` e usamos a função `get()` para fazer uma solicitação HTTP para a API do GitHub.

## Criando e Distribuindo Bibliotecas

Se você desenvolver uma funcionalidade que possa ser útil para outros programadores, você também pode criar sua própria biblioteca Python e distribuí-la para outros.
Para isso, você precisa criar um pacote Python e publicá-lo no PyPI (Python Package Index), que é o repositório oficial de pacotes Python.

Existem ferramentas como setuptools e twine que ajudam na criação e distribuição de pacotes Python.
Com essas ferramentas, você pode criar um arquivo `setup.py` que descreve sua biblioteca e seus requisitos de instalação, e então usar o `twine` para enviar sua biblioteca para o PyPI.

Uma vez que sua biblioteca esteja no PyPI, outros desenvolvedores podem instalá-la facilmente usando o `pip`.

## Licenças

Ao criar e distribuir uma biblioteca Python, é importante considerar a licença sob a qual você deseja disponibilizá-la. A licença define os termos de uso da sua biblioteca e pode afetar como outros desenvolvedores podem usá-la.

### Níveis de Restrição

As licenças  variam em seus níveis de restrição, desde permissivas até mais restritivas:

<p align="center">
  <img src="licenses.jpg" width="500"/>
</p>

#### Permissivas

* Permitem amplo uso, modificação e redistribuição do código, com poucas restrições.
* Podem ser usadas em projetos proprietários sem obrigar a adoção da mesma licença.
* Exemplos: MIT License, BSD License

#### Copyleft
    
* Exigem que qualquer trabalho derivado seja distribuído sob os mesmos termos de licença do trabalho original.
* Garantem que as modificações e melhorias feitas ao software permaneçam acessíveis à comunidade de código aberto.
* Exemplos: GNU General Public License (GPL), GNU Lesser General Public License (LGPL)

#### Domínio Público
    
* Não impõem quaisquer restrições ao uso, modificação ou redistribuição do código-fonte.
* O código é essencialmente de propriedade pública e pode ser usado de qualquer maneira sem restrições de direitos autorais.
* Exemplos: Creative Commons Zero (CC0), Unlicense

### Em construção...

* NumPy
* Pandas
* Matplotlib
* Seaborn
* SciPy
* Scikit-learn
* TensorFlow
* PyTorch
* NLTK
* pillow