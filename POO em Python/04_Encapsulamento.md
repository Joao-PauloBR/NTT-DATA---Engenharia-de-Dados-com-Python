### O que é Encapsulamento?

Encapsulamento é um dos princípios fundamentais da **Programação Orientada a Objetos (POO)**, que está relacionado com a ideia de ocultar os detalhes internos de uma classe e controlar o acesso aos seus atributos e métodos. A principal ideia por trás do encapsulamento é garantir que o estado interno de um objeto só possa ser alterado de maneiras controladas e previsíveis.

Em Python, o encapsulamento pode ser implementado através de **modificadores de acesso**, que permitem definir a visibilidade dos atributos e métodos de uma classe.

### Níveis de Acesso em Python

Embora Python não tenha modificadores de acesso rígidos como outras linguagens (por exemplo, `public`, `private` ou `protected` em Java ou C++), ele oferece convenções e mecanismos que ajudam a definir o nível de acesso a atributos e métodos.

Os níveis de acesso em Python são definidos principalmente por **convenção**:

#### 1. **Atributos e métodos públicos**
   - **Definição**: Tudo o que é definido sem um sublinhado (underscore) à frente do nome.
   - **Exemplo**:
     ```python
     class Pessoa:
         def __init__(self, nome, idade):
             self.nome = nome  # atributo público
             self.idade = idade  # atributo público
     
         def apresentar(self):  # método público
             return f"Meu nome é {self.nome} e tenho {self.idade} anos."
     
     pessoa = Pessoa("João", 30)
     print(pessoa.nome)  # acesso direto ao atributo público
     print(pessoa.apresentar())  # chamada de método público
     ```

   - **Uso**: Tanto os atributos quanto os métodos públicos podem ser acessados e modificados diretamente a partir de instâncias da classe. Este é o comportamento padrão.

#### 2. **Atributos e métodos protegidos**
   - **Definição**: Colocando um único sublinhado `_` antes do nome do atributo ou método.
   - **Exemplo**:
     ```python
     class Pessoa:
         def __init__(self, nome, idade):
             self._nome = nome  # atributo protegido
             self._idade = idade  # atributo protegido
     
         def _mostrar_detalhes(self):  # método protegido
             return f"Nome: {self._nome}, Idade: {self._idade}"
     ```
   - **Uso**: A convenção do sublinhado (`_`) indica que esses atributos ou métodos **não devem ser acessados diretamente** fora da classe ou de suas subclasses, mas **não impede completamente** o acesso. O propósito aqui é mais **uma sinalização para os desenvolvedores**, dizendo: "Cuidado, esses membros são para uso interno da classe ou de suas subclasses".
   
   - **Exemplo de Uso Prático**:
     ```python
     pessoa = Pessoa("Ana", 25)
     print(pessoa._nome)  # Não recomendado, mas possível
     ```

#### 3. **Atributos e métodos privados**
   - **Definição**: Colocando dois sublinhados `__` antes do nome do atributo ou método.
   - **Exemplo**:
     ```python
     class ContaBancaria:
         def __init__(self, saldo):
             self.__saldo = saldo  # atributo privado
     
         def __calcular_juros(self):  # método privado
             return self.__saldo * 0.05
     ```
   - **Uso**: Com dois sublinhados, o Python realiza um processo chamado **name mangling** (embaralhamento de nomes), o que torna o atributo ou método inacessível diretamente fora da classe. Na prática, o nome do atributo ou método é alterado internamente, dificultando o acesso externo.

   - **Exemplo de Name Mangling**:
     ```python
     conta = ContaBancaria(1000)
     # print(conta.__saldo)  # Isso gera um erro, pois o atributo é privado
     
     # Porém, ainda é possível acessar indiretamente:
     print(conta._ContaBancaria__saldo)  # Não recomendado, mas acessível
     ```

   O uso de dois sublinhados indica que o atributo ou método é **estritamente para uso interno** da classe, e o Python faz um esforço para dificultar o acesso.

---

### Por que usar Encapsulamento?

O encapsulamento oferece diversos benefícios no design e desenvolvimento de software:

1. **Proteção do estado interno**: Ao ocultar os atributos, evitamos que outras partes do programa modifiquem os dados de forma indevida, preservando a integridade dos objetos.
   
2. **Controle de acesso**: Através de métodos, podemos controlar como o estado interno de um objeto pode ser modificado. Isso ajuda a garantir que as alterações sejam válidas.
   
3. **Manutenção e flexibilidade**: O encapsulamento facilita futuras mudanças na implementação interna da classe, pois os detalhes internos estão escondidos e só os métodos públicos são expostos.
   
4. **Abstração**: Ocultando os detalhes de implementação, aumentamos a clareza e simplicidade da interface da classe. O usuário da classe não precisa saber como os dados são manipulados internamente.

### Exemplo de Encapsulamento na Prática

Suponha que estamos desenvolvendo uma classe que representa uma conta bancária. Queremos garantir que o saldo da conta não possa ser alterado diretamente, exceto por métodos específicos, como `depositar` ou `sacar`.

```python
class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # atributo privado
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor do depósito deve ser positivo.")
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido.")
    
    def consultar_saldo(self):
        return self.__saldo
```

Aqui, o saldo (`__saldo`) é privado e só pode ser modificado por métodos controlados como `depositar` e `sacar`. Isso evita que alguém inadvertidamente modifique o saldo diretamente.

#### Uso:

```python
conta = ContaBancaria(500)
conta.depositar(150)  # Depósito de 150
print(conta.consultar_saldo())  # Saldo: 650

conta.sacar(100)  # Saque de 100
print(conta.consultar_saldo())  # Saldo: 550

# Não é possível modificar o saldo diretamente
# conta.__saldo = 1000  # Isso vai gerar um erro
```