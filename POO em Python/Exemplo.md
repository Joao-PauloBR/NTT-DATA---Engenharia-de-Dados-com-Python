Vamos criar um exemplo de código em Python que combina os conceitos de Programação Orientada a Objetos (POO), incluindo métodos públicos, privados e protegidos, métodos construtores e destrutores, herança simples e múltipla, e encapsulamento. 

### Cenário: Sistema de Gerenciamento de Animais

Neste exemplo, vamos desenvolver um sistema que gerencia diferentes tipos de animais em um zoológico. Teremos uma superclasse `Animal`, subclasses específicas como `Mamifero` e `Ave`, e uma subclasse que herda de ambas chamada `Pinguim`. O sistema também demonstrará o uso de métodos públicos, privados e protegidos, bem como construtores e destrutores.

#### Código Completo

```python
class Animal:
    def __init__(self, nome, idade):
        """Construtor da classe Animal: inicializa os atributos nome e idade."""
        self.nome = nome  # Atributo público
        self.idade = idade  # Atributo público
        self._status = "ativo"  # Atributo protegido

    def emitir_som(self):
        """Método que deve ser sobrescrito pelas subclasses."""
        raise NotImplementedError("Método deve ser implementado na subclasse.")

    def apresentar(self):
        """Método público que apresenta o animal."""
        return f"Nome: {self.nome}, Idade: {self.idade}, Status: {self._status}"

    def __del__(self):
        """Destrutor: notifica que o animal foi removido."""
        print(f"O animal {self.nome} foi removido do sistema.")


class Mamifero(Animal):
    def __init__(self, nome, idade, tipo_pelo):
        """Construtor da classe Mamifero: chama o construtor da classe pai e inicializa tipo_pelo."""
        super().__init__(nome, idade)
        self.__tipo_pelo = tipo_pelo  # Atributo privado

    def emitir_som(self):
        """Sobrescreve o método emitir_som."""
        return "Som de mamífero"

    def tipo_pelo(self):
        """Método público para acessar o tipo de pelo."""
        return self.__tipo_pelo

    def mudar_status(self, novo_status):
        """Método público para mudar o status do animal."""
        self._status = novo_status


class Ave(Animal):
    def __init__(self, nome, idade, tipo_voo):
        """Construtor da classe Ave: chama o construtor da classe pai e inicializa tipo_voo."""
        super().__init__(nome, idade)
        self._tipo_voo = tipo_voo  # Atributo protegido

    def emitir_som(self):
        """Sobrescreve o método emitir_som."""
        return "Som de ave"

    def tipo_voo(self):
        """Método público para acessar o tipo de voo."""
        return self._tipo_voo


class Pinguim(Mamifero, Ave):
    def __init__(self, nome, idade):
        """Construtor da classe Pinguim: chama os construtores das classes pai."""
        Mamifero.__init__(self, nome, idade, "sem pelo")  # Inicializa a classe Mamifero
        Ave.__init__(self, nome, idade, "não voa")  # Inicializa a classe Ave

    def emitir_som(self):
        """Sobrescreve o método emitir_som."""
        return "Som de pinguim"

# Demonstração do uso das classes
pinguim = Pinguim("Pingu", 3)

print(pinguim.apresentar())       # Apresenta informações do pinguim
print(pinguim.emitir_som())       # Saída: Som de pinguim
print(f"Tipo de pelo: {pinguim.tipo_pelo()}")  # Saída: Tipo de pelo: sem pelo
print(f"Tipo de voo: {pinguim.tipo_voo()}")    # Saída: Tipo de voo: não voa

# Mudando o status do animal
pinguim.mudar_status("adotado")
print(pinguim.apresentar())       # Apresenta informações atualizadas do pinguim

# Removendo o pinguim
del pinguim  # O destrutor será chamado aqui
```

### Explicação do Código

1. **Classes e Herança**:
   - `Animal` é a superclasse que contém métodos e atributos comuns a todos os animais.
   - `Mamifero` e `Ave` são subclasses de `Animal`. Cada uma sobrescreve o método `emitir_som`.
   - `Pinguim` é uma subclasse que herda de ambas as classes `Mamifero` e `Ave`, demonstrando a **herança múltipla**.

2. **Métodos Públicos e Privados**:
   - O método `apresentar` é público e acessível fora da classe, mostrando os atributos do animal.
   - O atributo `__tipo_pelo` em `Mamifero` é privado e não pode ser acessado diretamente fora da classe.
   - O atributo `_tipo_voo` em `Ave` é protegido e pode ser acessado por subclasses.

3. **Construtores e Destrutores**:
   - O construtor `__init__` é utilizado para inicializar os atributos da classe.
   - O destrutor `__del__` é chamado automaticamente quando um objeto é destruído, notificado que o animal foi removido do sistema.

4. **Encapsulamento**:
   - O encapsulamento é demonstrado com o uso de atributos protegidos e privados, permitindo um controle mais rigoroso sobre o acesso a dados internos da classe.

### Resultados Esperados

Ao executar o código, você verá a apresentação das informações do pinguim, o som que ele emite, e o tipo de pelo e voo. Após mudar o status do pinguim, as informações são atualizadas. Finalmente, ao remover o pinguim, o destrutor é chamado, e você verá uma mensagem indicando que o animal foi removido.