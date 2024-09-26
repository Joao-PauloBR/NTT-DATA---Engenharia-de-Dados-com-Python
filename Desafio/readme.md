# Visão Geral

Fomos contratados por um grande banco para desenvolver seu novo sistema. Este banco deseja modernizar suas operações e, para isso, escolheu a linguagem Python. Na primeira versão do sistema, implementaremos apenas três operações: depósito, saque e extrato.

## Operação de Depósito

Deve ser possível depositar valores positivos na conta bancária. A versão 1 do projeto trabalha apenas com um usuário, portanto, não é necessário identificar o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

## Operação de Saque

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo suficiente em conta, o sistema deve exibir uma mensagem informando que não será possível efetuar o saque por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

## Operação de Extrato

Esta operação deve listar todos os depósitos e saques realizados na conta. Ao final da listagem, deve ser exibido o saldo atual da conta. Os valores devem ser exibidos no formato R$ xxx.xx (exemplo: 1500.45 = R$ 1500.45).

# Versão 2.0

Com os novos conhecimentos adquiridos sobre data e hora, você foi encarregado de implementar as seguintes funcionalidades no sistema:

- Estabelecer um limite de 10 transações diárias para uma conta.
- Informar o usuário caso ele tente fazer uma transação após atingir o limite, indicando que excedeu o número de transações permitidas para aquele dia.
- Mostrar no extrato a data e a hora de todas as transações.

# Versão 3.0

## Objetivo Geral

Precisamos tornar nosso código mais modularizado. Para isso, criaremos funções para as operações existentes:
- Sacar, depositar e visualizar o extrato.

Além disso, para a versão 3 do nosso sistema, precisamos criar duas novas funções:
- Cadastrar usuário (cliente do banco).
- Cadastrar conta corrente (vinculada ao usuário).

## Separação em Funções

Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada função terá uma regra específica na passagem de argumentos. O retorno e a forma como serão chamadas podem ser definidos por você da maneira que achar melhor.

### Saque

A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

### Depósito

A função depósito deve receber os argumentos apenas por posição (position only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

### Extrato

A função extrato deve receber os argumentos por posição e nome (position only e keyword only). Argumentos posicionais: saldo; argumentos nomeados: extrato.

## Novas Funções

Precisamos criar duas novas funções: criar usuário e criar conta corrente. Sinta-se à vontade para adicionar mais funções, como por exemplo: listar contas.

### Criar Usuário (Cliente)

O programa deve armazenar os usuários em uma lista. Um usuário é composto por: nome, data de nascimento, CPF e endereço. O endereço é uma string com o formato: logradouro, número - Bairro - Cidade/sigla estado. Devem ser armazenados somente os números do CPF. Não é permitido cadastrar dois usuários com o mesmo CPF.

### Criar Conta Corrente

O programa deve armazenar contas em uma lista. Uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta deve pertencer a somente um usuário.

## Dica

Para vincular um usuário a uma conta corrente, filtre a lista de usuários buscando o número de CPF informado para cada usuário da lista.