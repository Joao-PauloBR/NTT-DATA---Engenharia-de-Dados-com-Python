# Sistema Bancário NTT DATA

## Visão Geral

Este é um sistema bancário desenvolvido em Python para a NTT DATA. O sistema oferece uma variedade de funcionalidades para gerenciar contas bancárias, usuários e transações financeiras.

## Funcionalidades Principais

### 1. Gerenciamento de Usuários
- Cadastrar novo usuário
- Deletar usuário existente
- Editar informações de usuário
- Listar todos os usuários cadastrados

### 2. Gerenciamento de Contas
- Criar nova conta corrente
- Deletar conta existente
- Listar todas as contas cadastradas

### 3. Operações Bancárias
- Realizar depósitos
- Efetuar saques
- Visualizar extrato da conta

### 4. Sistema de Autenticação
- Selecionar usuário ativo
- Selecionar conta corrente ativa

## Regras de Negócio

1. **Depósitos**
   - Não há limite para o número de depósitos diários
   - Valor mínimo de depósito: R$ 0,01

2. **Saques**
   - Limite de 3 saques diários
   - Valor máximo por saque: R$ 500,00
   - O usuário não pode sacar mais do que o saldo disponível

3. **Limites de Transações**
   - Máximo de 10 transações (saques + depósitos) por dia para cada conta

4. **Extrato**
   - Mostra todas as transações realizadas na conta
   - Exibe data e hora de cada transação
   - Apresenta o saldo atual da conta

5. **Contas**
   - Número da agência é fixo: "0001"
   - Número da conta é sequencial, iniciando em 1
   - Um usuário pode ter múltiplas contas
   - Uma conta pertence a apenas um usuário

6. **Usuários**
   - Informações armazenadas: nome, data de nascimento, CPF e endereço
   - CPF deve ser único no sistema
   - Endereço no formato: logradouro, número - Bairro - Cidade/sigla estado

## Como Usar o Sistema

O sistema opera em três etapas principais:

### 1ª Etapa - Cadastro de Usuário e Conta
- Opções para cadastrar, deletar e editar usuários
- Opções para cadastrar e deletar contas correntes

### 2ª Etapa - Escolha de Usuário e Conta
- Selecionar o usuário ativo
- Selecionar a conta corrente ativa
- Listar usuários e contas cadastradas

### 3ª Etapa - Operações Bancárias
- Realizar depósitos
- Efetuar saques
- Visualizar extrato

## Requisitos do Sistema

- Python 3.x

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina
2. Baixe o arquivo `sistema_bancario.py`
3. Abra um terminal ou prompt de comando
4. Navegue até o diretório onde o arquivo está salvo
5. Execute o comando: `python sistema_bancario.py`

## Notas Adicionais

- O sistema utiliza armazenamento em memória, então todos os dados são perdidos ao encerrar o programa
- Todas as operações são registradas com data e hora para melhor rastreabilidade
- O sistema possui verificações para garantir a integridade dos dados e evitar operações inválidas

## Autor

[João Paulo Souza Bernucio](https://www.linkedin.com/in/joaobernucio/)