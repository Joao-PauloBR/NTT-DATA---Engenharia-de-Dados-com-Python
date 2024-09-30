### Propriedades no Encapsulamento: `@property`, `@setter` e `@deleter`

No contexto de encapsulamento em Python, as **propriedades** são um recurso poderoso que permite controlar o acesso aos atributos de um objeto de maneira mais flexível e transparente. Elas permitem que você utilize métodos para acessar, modificar ou deletar atributos, mas de forma que, para quem usa a classe, pareça que está acessando diretamente o atributo, o que simplifica a interface da classe.

Os três decoradores principais relacionados às propriedades em Python são:
- **`@property`**: Define um método que pode ser acessado como um atributo de leitura (getter).
- **`@setter`**: Define um método que permite modificar o valor de um atributo (setter).
- **`@deleter`**: Define um método que permite deletar um atributo (deleter).

Vamos ver como cada um deles funciona e entender o conceito na prática.

---

### 1. **`@property`: Acessando atributos de forma controlada**

O decorador `@property` transforma um método em um **getter**, permitindo acessar um valor como se fosse um atributo, mas sem a necessidade de chamar explicitamente um método. Isso é útil quando você quer controlar o acesso à leitura de um atributo, como realizar alguma validação ou cálculo antes de retornar o valor.

#### Exemplo de `@property`:

```python
class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @property
    def preco(self):
        """Retorna o preço do produto."""
        return self._preco
```

#### Uso:

```python
produto = Produto("Notebook", 2500)
print(produto.preco)  # Acessa o método como se fosse um atributo: 2500
```

Aqui, `produto.preco` parece ser um atributo comum, mas na verdade é um método que retorna o valor de `_preco`. Isso é útil quando você quer esconder a implementação interna (neste caso, o atributo `_preco`).

---

### 2. **`@setter`: Modificando atributos de forma controlada**

O decorador `@setter` é utilizado em conjunto com `@property` para permitir que o valor de um atributo seja **modificado de forma controlada**. Dessa maneira, você pode aplicar validações, restrições ou qualquer lógica antes de realmente alterar o valor de um atributo.

#### Exemplo de `@setter`:

```python
class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        """Valida o preço antes de modificá-lo."""
        if valor < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = valor
```

#### Uso:

```python
produto = Produto("Notebook", 2500)
produto.preco = 3000  # Acessa o método setter para modificar o valor
print(produto.preco)  # 3000

produto.preco = -100  # Vai lançar um erro, pois o valor é inválido
```

Aqui, ao tentar modificar o preço usando `produto.preco = -100`, o setter valida o valor e impede a atribuição de um preço negativo, garantindo a integridade dos dados.

---

### 3. **`@deleter`: Removendo atributos de forma controlada**

O decorador `@deleter` é utilizado para permitir a **remoção controlada** de um atributo. Isso é útil quando você precisa fazer alguma ação específica ao remover um atributo, como liberar recursos, salvar dados, etc.

#### Exemplo de `@deleter`:

```python
class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = valor

    @preco.deleter
    def preco(self):
        """Exclui o preço do produto."""
        print("Preço excluído.")
        del self._preco
```

#### Uso:

```python
produto = Produto("Notebook", 2500)
del produto.preco  # Chama o método deleter, que deleta o atributo e exibe a mensagem

# Tentativa de acessar o atributo depois de ser deletado gera erro
# print(produto.preco)  # AttributeError: 'Produto' object has no attribute '_preco'
```

Aqui, o método `del produto.preco` aciona o método `@preco.deleter`, que remove o atributo `_preco` e exibe uma mensagem indicando que o preço foi excluído. Tentativas de acessar o preço depois da exclusão resultarão em erro, pois o atributo não existe mais.

---

### Resumo das Propriedades (`@property`, `@setter`, `@deleter`)

As propriedades permitem maior controle sobre os atributos de uma classe sem alterar a interface externa. Isso significa que você pode aplicar lógica interna sem que o usuário da classe perceba a diferença entre um atributo simples e um que usa métodos getter e setter.

#### Benefícios do Uso de Propriedades:
1. **Controle de acesso**: Você pode validar, transformar ou calcular valores ao acessar ou modificar um atributo.
2. **Interface limpa**: Para o usuário da classe, o acesso aos atributos ainda parece direto, mesmo que haja lógica de controle nos bastidores.
3. **Fácil manutenção**: Permite alterar a lógica interna sem mudar como a classe é usada externamente.

---

### Exemplo Completo

Aqui está um exemplo que combina as três propriedades: `@property`, `@setter` e `@deleter`, para encapsular o controle sobre o atributo `preco`:

```python
class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @property
    def preco(self):
        """Retorna o preço do produto."""
        return self._preco

    @preco.setter
    def preco(self, valor):
        """Valida e define o preço."""
        if valor < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = valor

    @preco.deleter
    def preco(self):
        """Exclui o preço."""
        print(f"Preço de {self._nome} foi removido.")
        del self._preco
```

#### Uso:

```python
produto = Produto("Notebook", 2500)
print(produto.preco)  # 2500

produto.preco = 3500  # Modifica o preço
print(produto.preco)  # 3500

del produto.preco  # Remove o preço
# print(produto.preco)  # Gera um erro
```

Neste exemplo, usamos as três formas de encapsulamento:
- **`@property`** para acessar o preço.
- **`@setter`** para validar e modificar o preço.
- **`@deleter`** para remover o preço e notificar a remoção.