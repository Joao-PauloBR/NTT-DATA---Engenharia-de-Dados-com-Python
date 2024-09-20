# NTT DATA: Engenharia de Dados com Python

Este repositório contém meus estudos e práticas realizadas durante o bootcamp **NTT DATA: Engenharia de Dados com Python** oferecido pela [DIO](https://www.dio.me/) em parceria com a [NTT DATA](https://www.nttdata.com/). O bootcamp aborda desde conceitos básicos da linguagem Python até o domínio no tratamento de dados e criação de dashboards com Power BI, proporcionando uma base sólida para atuar como Engenheiro de Dados.

Com base na imagem que você forneceu, vou ajustar a estrutura e descrição do repositório para refletir melhor a organização dos arquivos e pastas, conforme visualizado.

### 📁 Estrutura do Repositório

O repositório está organizado em pastas que representam os tópicos e exercícios realizados durante o bootcamp, conforme descrito abaixo:

#### 1. 📂 Introdução ao Python
- **Conteúdo:** Scripts introdutórios sobre tipos de dados, operações básicas de entrada e saída, estruturação de código e criação do tradicional "Hello, World!".
- **Arquivos:**
  - `conversao_tipos.py`: Conversão entre diferentes tipos de dados.
  - `entrada_saida.py`: Manipulação de entrada e saída de dados.
  - `hello_world.py`: Exemplo básico de um programa Python.
  - `identacao_blocos.py`: Demonstração da importância da indentação e blocos de código em Python.
- **Objetivo:** Familiarizar-se com conceitos fundamentais da linguagem e a estrutura básica de um script Python.

#### 2. 📂 Sintaxe Básica Python

Esta pasta contém subdiretórios com exercícios focados em conceitos fundamentais da linguagem Python, como estruturas condicionais, funções, operadores e manipulação de strings.

##### 2.1 📂 Condicionais e Repetições
- **Conteúdo:** Exemplos de uso de estruturas de controle como `if`, `for`, e `while`.
- **Arquivos:**
  - `aninhada.py`: Condicionais aninhadas.
  - `break.py`: Uso da instrução `break` em loops.
  - `for.py`: Estrutura de repetição `for`.
  - `if.py`: Estrutura condicional `if`.
  - `while.py`: Estrutura de repetição `while`.
- **Objetivo:** Aprender a controlar o fluxo de execução do programa usando estruturas condicionais e de repetição.

##### 2.2 📂 Funções
- **Conteúdo:** Exemplos de como definir e utilizar funções, passando parâmetros de diferentes formas.
- **Arquivos:**
  - `args_kwargs.py`: Uso de argumentos `*args` e `**kwargs`.
  - `argumento_nomeado.py`: Passagem de argumentos nomeados.
  - `escopo_local_global.py`: Diferença entre escopo local e global.
  - `objeto_primeira_classe.py`: Funções como objetos de primeira classe.
  - `parametro_posicao.py`: Passagem de parâmetros por posição.
  - `parametro.py`: Passagem de parâmetros de função.
  - `retorno.py`: Utilização da palavra-chave `return`.
- **Objetivo:** Entender como criar funções reutilizáveis e trabalhar com diferentes tipos de parâmetros e escopos.

##### 2.3 📂 Operadores
- **Conteúdo:** Utilização de operadores aritméticos, lógicos e comparativos em Python.
- **Arquivos:**
  - `aritmeticos.py`: Exemplos de operadores aritméticos (`+`, `-`, `*`, `/`).
  - `associacao.py`: Operadores de associação (`in`, `not in`).
  - `atribuicao.py`: Operadores de atribuição (`=`, `+=`, `-=`, etc.).
  - `comparacao.py`: Operadores de comparação (`==`, `!=`, `>`, `<`, etc.).
  - `identidade.py`: Operadores de identidade (`is`, `is not`).
  - `logico.py`: Operadores lógicos (`and`, `or`, `not`).
- **Objetivo:** Compreender como usar operadores para realizar operações básicas e lógicas em Python.

##### 2.4 📂 Strings e Fatiamento
- **Conteúdo:** Manipulação de strings e uso de técnicas de fatiamento.
- **Arquivos:**
  - `fatiamento.py`: Exemplos de fatiamento de strings.
  - `interpolacao.py`: Interpolação de strings usando diferentes métodos.
  - `multiplas_linhas.py`: Uso de strings de múltiplas linhas.
  - `principais_metodos.py`: Principais métodos para manipulação de strings (`upper()`, `lower()`, `replace()`, etc.).
- **Objetivo:** Aprender a manipular e formatar strings eficientemente em Python.

#### 3. 📂 Desafio: Sistema Bancário
- **Conteúdo:** Implementação de um sistema bancário com funcionalidades de depósito, saque e exibição de extrato.
- **Arquivos:**
    - `readme.md`: Arquivo de documentação específico do desafio, contendo o enunciado e as instruções para a implementação do sistema bancário.
    - `sistema_bancario.py`: Script Python com a implementação das funcionalidades do sistema bancário, incluindo operações de depósito, saque e exibição do extrato.
- **Objetivo:** Aplicar os conceitos aprendidos em um desafio mais complexo, simulando um caso de uso real de um sistema de gerenciamento bancário.
- [Leia mais sobre o desafio aqui](link_para_o_README_do_desafio).

## 🧑‍🏫 Instrutor

O bootcamp foi ministrado por [Guilherme Carvalho](https://github.com/guicarvalho), que forneceu uma série de exemplos e exercícios práticos para fortalecer o aprendizado.

## 🚀 Motivação

O principal objetivo de publicar este repositório é compartilhar meu progresso e estudos no campo de Engenharia de Dados com Python, além de servir como referência e fonte de consulta para quem estiver participando do mesmo bootcamp ou desejando aprender mais sobre o tema.

## 📚 Como Utilizar

### 1. Configuração do Ambiente Python

Antes de executar os scripts deste repositório, você precisa ter o Python instalado e configurado em seu computador. Siga as instruções abaixo conforme o seu sistema operacional:

#### ⬇️ Windows ⬇️
1. **Baixar e instalar o Python:**
   - Acesse [python.org](https://www.python.org/downloads/) e baixe a versão mais recente do Python.
   - Durante a instalação, marque a opção "Add Python to PATH" para configurar as variáveis de ambiente automaticamente.
   - Siga o assistente de instalação até o final.

2. **Verificar a instalação:**
   - Abra o Prompt de Comando (cmd).
   - Digite `python --version` para verificar se o Python foi instalado corretamente.

#### ⬇️ Ubuntu/Debian ⬇️
1. **Instalar o Python via terminal:**
   - Abra o terminal.
   - Atualize a lista de pacotes:
     ```bash
     sudo apt update
     ```
   - Instale o Python (normalmente já vem pré-instalado em sistemas Linux):
     ```bash
     sudo apt install python3
     ```

2. **Verificar a instalação:**
   - Digite `python3 --version` no terminal para confirmar a instalação.

#### ⬇️ Fedora ⬇️
1. **Instalar o Python via terminal:**
   - Abra o terminal.
   - Atualize a lista de pacotes:
     ```bash
     sudo dnf update
     ```
   - Instale o Python:
     ```bash
     sudo dnf install python3
     ```

2. **Verificar a instalação:**
   - Digite `python3 --version` no terminal para confirmar a instalação.

#### ⬇️ openSUSE ⬇️
1. **Instalar o Python via terminal:**
   - Abra o terminal.
   - Atualize a lista de pacotes:
     ```bash
     sudo zypper refresh
     ```
   - Instale o Python:
     ```bash
     sudo zypper install python3
     ```

2. **Verificar a instalação:**
   - Digite `python3 --version` no terminal para confirmar a instalação.

#### Outras Dependências
- Certifique-se de ter o `pip` instalado para gerenciar pacotes Python. Você pode verificar digitando `pip --version` no terminal. Se não estiver instalado, você pode instalar executando:
  ```bash
  sudo apt install python3-pip     # Para Ubuntu/Debian
  sudo dnf install python3-pip     # Para Fedora
  sudo zypper install python3-pip  # Para openSUSE

### 2. Clone o Repositório

Após configurar o ambiente Python, clone este repositório para sua máquina:
   ```bash
   git clone https://github.com/Joao-PauloBR/NTT-DATA---Engenharia-de-Dados-com-Python.git
   ```

### 3. Navegar pelas Pastas e Executar os Scripts
- Entre na pasta do repositório clonado:
  ```bash
  cd seu-repositorio
  ```
- Navegue até a pasta desejada para visualizar os exercícios ou o desafio específico.
- Execute os scripts Python conforme necessário, usando:
  ```bash
  python nome_do_script.py      # Para Windows
  python3 nome_do_script.py     # Para Linux
  ```

### 4. Executar o Sistema Bancário
Para executar o desafio do sistema bancário:
- Entre na pasta do desafio e execute o arquivo principal, por exemplo:
  ```bash
  python sistema_bancario.py
  ```

Agora, você está pronto para explorar o repositório e executar os exemplos e desafios!
