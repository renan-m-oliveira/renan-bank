# 🏦 Renan Bank — Sistema Bancário em Python

Sistema bancário desenvolvido em Python com arquitetura em camadas, persistência em JSON e interface via terminal.

---

## 📋 Sobre o Projeto

O Renan Bank é um sistema bancário completo desenvolvido do zero, passando por duas versões principais. O objetivo foi aprender Python na prática construindo um projeto real, aplicando cada conceito aprendido diretamente no sistema.

---

## 🗂️ Estrutura do Projeto

```
RENAN BANK PY/
│
├── main.py                  → Menu principal e submenus
│
├── services/
│   ├── cliente_service.py   → Cadastro, busca, exclusão de clientes
│   ├── conta_services.py    → Depósito, saque, PIX, saldo, extrato
│   └── credito_service.py   → Solicitação de empréstimo
│
├── models/
│   └── clientee.py          → Classe Cliente
│
├── database/
│   └── json_db.py           → Leitura e escrita no JSON
│
└── clientes.json            → Banco de dados
```

---

## 🚀 Versão 1.0

### O que foi construído:
- Menu principal com 6 opções
- Cadastro de clientes
- Listagem de clientes
- Busca de cliente por ID
- Exclusão de cliente
- Solicitação de empréstimo com cálculo de limite (renda × 3)
- Persistência de dados em JSON

### Conceitos aprendidos e aplicados:
- **Classes e Objetos** — Classe `Cliente` com atributos e métodos
- **`__init__`** — Construtor da classe com valores padrão
- **`to_dict()`** — Método para serialização do objeto
- **Variáveis e tipos de dados** — `int`, `float`, `str`
- **If / Elif / Else** — Condicionais para lógica de negócio
- **While + Break** — Loops de menu e validação
- **For loops** — Percorrer lista de clientes
- **Funções** — Separação de responsabilidades
- **Importação de módulos** — `import` e `from...import`
- **Arquitetura em camadas** — Separação em `models`, `services`, `database`
- **JSON** — `json.dump`, `json.load`, `os.path.exists`
- **List comprehension** — Converter dados do JSON em objetos
- **Parâmetros entre arquivos** — Passar a lista de clientes entre funções
- **Git e GitHub** — Versionamento do código

---

## 🚀 Versão 2.0

### O que foi adicionado:

#### Novas funcionalidades:
- **Depósito** — Adicionar saldo na conta do cliente
- **Saque** — Retirar saldo com validação de saldo suficiente
- **PIX** — Transferência entre contas com devolução automática se destinatário não encontrado
- **Consultar saldo** — Visualizar saldo atual
- **Extrato bancário** — Histórico completo de transações com tipo, valor e data
- **Menu hierárquico** — Menu principal com submenus de Clientes, Conta e Crédito

#### Melhorias em relação à v1.0:
- **Try/Except** — Proteção de todos os inputs contra erros de digitação
- **Validação de nome** — `.isalpha()` + `.replace()` para aceitar apenas letras
- **Geração de ID único** — `max()` no lugar de `len()` para evitar IDs duplicados após exclusão
- **Lista única de clientes** — Bug de lista dupla corrigido, passando a lista como parâmetro
- **Histórico de transações** — Registro automático de depósito, saque e PIX com data e hora
- **Data automática** — `datetime.now()` para registrar data e hora das transações
- **Menu com retorno** — Possibilidade de voltar ao menu anterior

### Conceitos aprendidos e aplicados na v2.0:
- **Try/Except/ValueError** — Tratamento de erros nos inputs
- **isalpha() + replace()** — Validação de strings
- **max()** — Geração de ID único sem repetição
- **datetime** — Data e hora automática
- **Dicionários dentro de listas** — Histórico de transações
- **for/else** — Identificar quando item não foi encontrado no loop
- **Parâmetros obrigatórios** — Passar lista entre arquivos corretamente
- **return vs break** — Diferença entre encerrar função e sair do loop
- **Arquitetura expandida** — Novo arquivo `conta_services.py`

---

## ⚙️ Como executar

```bash
# Clone o repositório
git clone https://github.com/renan-m-oliveira/renan-bank.git

# Entre na pasta
cd renan-bank

# Execute o sistema
python main.py
```

---

## 🎯 Funcionalidades

| Funcionalidade | Versão |
|---|---|
| Cadastrar cliente | v1.0 |
| Listar clientes | v1.0 |
| Buscar cliente por ID | v1.0 |
| Excluir cliente | v1.0 |
| Solicitar empréstimo | v1.0 |
| Persistência em JSON | v1.0 |
| Depositar | v2.0 |
| Sacar | v2.0 |
| PIX entre contas | v2.0 |
| Consultar saldo | v2.0 |
| Extrato de transações | v2.0 |
| Validação de inputs | v2.0 |
| Histórico com data/hora | v2.0 |
| Menu hierárquico | v2.0 |

---

## 🗺️ Próximas versões

```
v3.0 → Banco de dados SQLite + API com FastAPI
v4.0 → Frontend em React
v5.0 → Deploy online + MySQL + Autenticação JWT
```

---

## 👨‍💻 Desenvolvido por

**Renan Martins**
GitHub: [@renan-m-oliveira](https://github.com/renan-m-oliveira)
