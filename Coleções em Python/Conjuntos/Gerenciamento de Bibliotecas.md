Aqui está o código completo que implementa o exemplo do sistema de gerenciamento de biblioteca usando conjuntos em Python. Este código inclui todas as etapas mencionadas na explicação anterior:

### 1. Contextualização do Problema

```python
# Criação de conjuntos de livros usando chaves {}
ficcao = {'1984', 'Brave New World', 'Fahrenheit 451'}
historia = {'Sapiens', '1984', 'Guns, Germs, and Steel'}

# Usando a função set() para criar um conjunto a partir de uma lista
ciencia = set(['A Brief History of Time', 'The Selfish Gene', 'Sapiens'])

# Set comprehension para criar um conjunto com base em uma condição
livros_literatura_inglesa = {livro for livro in ficcao if ' ' in livro}

print("Ficção:", ficcao)
print("História:", historia)
print("Ciência:", ciencia)
print("Livros de literatura inglesa:", livros_literatura_inglesa)
```

### 2. Operações Básicas

```python
# Adicionando um livro à seção de ficção
ficcao.add('The Handmaid\'s Tale')

# Removendo um livro da seção de história
historia.remove('1984')  # Este livro é removido da coleção de história

# Verificando se um livro está na seção de ciência
print('Sapiens' in ciencia)  # Saída: True
print('1984' in ciencia)     # Saída: False

# Utilizando discard para evitar erro ao remover elemento inexistente
ficcao.discard('Animal Farm')  # Nenhum erro, mesmo que o livro não esteja na coleção
```

### 3. Operações de Conjunto

```python
# União: Todos os livros nas seções de ficção e história
todos_livros_ficcao_historia = ficcao | historia
print("União (ficção e história):", todos_livros_ficcao_historia)

# Interseção: Livros comuns entre as seções de ciência e história
livros_comuns = ciencia & historia
print("Interseção (ciência e história):", livros_comuns)

# Diferença: Livros que estão em ficção, mas não em ciência
livros_exclusivos_ficcao = ficcao - ciencia
print("Diferença (ficção menos ciência):", livros_exclusivos_ficcao)

# Diferença Simétrica: Livros que estão em ficção ou ciência, mas não em ambos
livros_diferentes = ficcao ^ ciencia
print("Diferença Simétrica (ficção e ciência):", livros_diferentes)
```

### 4. Conjuntos Imutáveis

```python
# Transformando a coleção de ficção em um frozenset para evitar modificações
ficcao_protegida = frozenset(ficcao)

# Tentando adicionar ou remover elementos resultaria em erro:
# ficcao_protegida.add('Oryx and Crake')  # Isso geraria um erro, pois frozensets são imutáveis

print("Ficção protegida (frozenset):", ficcao_protegida)
```

### 5. Iteração e Compreensão

```python
# Iteração sobre a coleção de ficção
print("Iteração sobre ficção:")
for livro in ficcao:
    print(livro)

# Set comprehension para criar um novo conjunto de livros com títulos de mais de uma palavra
livros_multiplas_palavras = {livro for livro in ficcao if ' ' in livro}
print("Livros com mais de uma palavra:", livros_multiplas_palavras)
```

### 6. Manipulação Avançada

```python
# Livros exclusivos de ficção e ciência
exclusivos_ficcao = ficcao - (historia | ciencia)
exclusivos_ciencia = ciencia - (ficcao | historia)

# Criando uma coleção de raridades a partir dos livros exclusivos de cada seção
raridades = exclusivos_ficcao | exclusivos_ciencia
print("Livros raros (exclusivos de ficção ou ciência):", raridades)
```

### 7. Tratamento de Erros

```python
# Tentativa de remover elemento inexistente
try:
    historia.remove('The Art of War')  # Gera erro se o livro não estiver presente
except KeyError:
    print("O livro 'The Art of War' não está na coleção de história.")

# Tentativa de adicionar um elemento não hashable (como uma lista)
try:
    ficcao.add(['The Road'])  # Gera um TypeError
except TypeError:
    print("Não é possível adicionar elementos mutáveis ao conjunto (por exemplo, listas).")
```

### 8. Boas Práticas

Esse código mostra como conjuntos podem ser usados de maneira eficiente e robusta para gerenciar coleções de livros em uma biblioteca. O uso de `frozenset` garante que algumas coleções permaneçam inalteradas, e as operações de conjunto simplificam comparações e combinações entre diferentes seções da biblioteca. Além disso, o tratamento de exceções ajuda a prevenir erros ao manipular conjuntos.

### Saída Esperada:

```
Ficção: {'Fahrenheit 451', '1984', 'Brave New World'}
História: {'1984', 'Sapiens', 'Guns, Germs, and Steel'}
Ciência: {'Sapiens', 'The Selfish Gene', 'A Brief History of Time'}
Livros de literatura inglesa: {'Brave New World', 'Fahrenheit 451'}
Sapiens True
1984 False
União (ficção e história): {'The Handmaid's Tale', 'Guns, Germs, and Steel', 'Fahrenheit 451', 'Sapiens', 'Brave New World'}
Interseção (ciência e história): {'Sapiens'}
Diferença (ficção menos ciência): {'Fahrenheit 451', 'The Handmaid's Tale', 'Brave New World'}
Diferença Simétrica (ficção e ciência): {'Fahrenheit 451', 'Brave New World', 'A Brief History of Time', 'The Selfish Gene', 'The Handmaid's Tale'}
Ficção protegida (frozenset): frozenset({'Fahrenheit 451', 'The Handmaid's Tale', 'Brave New World'})
Iteração sobre ficção:
Fahrenheit 451
The Handmaid's Tale
Brave New World
Livros com mais de uma palavra: {'Brave New World', 'Fahrenheit 451', 'The Handmaid's Tale'}
Livros raros (exclusivos de ficção ou ciência): {'A Brief History of Time', 'The Selfish Gene', 'Fahrenheit 451', 'The Handmaid's Tale', 'Brave New World'}
O livro 'The Art of War' não está na coleção de história.
Não é possível adicionar elementos mutáveis ao conjunto (por exemplo, listas).
```

Este exemplo ilustra bem as funcionalidades e a flexibilidade dos conjuntos em Python, sendo uma excelente solução para cenários que requerem manipulação eficiente de coleções sem duplicatas.