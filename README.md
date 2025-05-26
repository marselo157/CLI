
# 🛡️ Champ Manager - Gerenciador de Campeões de League of Legends

Sistema CLI em Python para gerenciamento de campeões do universo de League of Legends, com funcionalidades como cadastro, associação de região, fila de combate e confrontos simulados.

---

## 👥 Integrantes

| Nome Completo                           | RA       |
|----------------------------------------|----------|
| Artur Camilo Taroco                    | 2009597  |
| Marcelo Beverari do Nascimento Filho  | 1997165  |
| Mateus Felix de Moura dos Santos      | 1998770  |

---

## 📝 Descrição Geral

Este sistema permite ao usuário:

- Cadastrar campeões com atributos e habilidades.
- Associar uma região a um campeão.
- Gerenciar uma fila de combate com confrontos entre campeões.
- Visualizar e remover campeões da fila.

Tudo isso através de um menu simples e intuitivo via terminal.

---

## ⚙️ Requisitos e Execução

> 💡 Testado com **Python 3.6+**

### 🔧 Instalação

1. Instale o Python:  
   👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   cd seu_repositorio
   ```

3. Execute o sistema:
   ```bash
   python champ_manager.py
   ```

---

## 🧠 Estruturas e Justificativas

### 📌 Lista de Campeões

```python
campeoes = []
```

Usada para armazenar todos os campeões cadastrados. Optamos por lista pela simplicidade e acesso sequencial.

---

### 🧱 Classe `NoDuplo`

Implementa um nó de lista duplamente encadeada — útil para manipular a fila de combate com facilidade, removendo ou adicionando elementos nas extremidades.

---

### 🔄 Classe `FilaCombate`

Fila baseada em lista duplamente encadeada, representando o sistema de confrontos. Permite:

- Adição e remoção de campeões
- Desenfileirar para confrontos
- Visualização da fila
- Verificação de duplicidade na fila

---

## 🚀 Funcionalidades

| Funcionalidade              | Descrição                                                                 |
|----------------------------|---------------------------------------------------------------------------|
| 📥 Cadastrar Campeão       | Nome, função, tipo de dano e habilidades (com validações)                 |
| 🌍 Associar Região         | Vincula uma região ao campeão                                            |
| 📋 Listar Campeões         | Mostra os dados completos de todos os campeões                            |
| 🥊 Adicionar à Fila        | Escolhe um campeão para participar da fila de combate                     |
| ⚔️ Iniciar Confronto       | Simula um combate entre os dois primeiros campeões da fila                |
| 🧹 Remover da Fila         | Remove um campeão da fila pelo nome                                       |

---

## 📌 Observações Finais

- O projeto visa exercitar conceitos de estruturas de dados como listas, conjuntos e listas duplamente encadeadas.
- Toda interação é feita via terminal (CLI).
- Sistema ideal para simular lógicas de gerenciamento e combate com personagens fictícios.

---

## 🏁 Conclusão

Este projeto demonstra de forma prática o uso de estruturas de dados e lógica de programação com Python. É ideal para quem quer aplicar conceitos de filas, listas e classes com um tema divertido e envolvente.

---
