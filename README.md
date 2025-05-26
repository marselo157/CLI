## Integrantes

- Nome Completo: Artur Camilo Taroco
- RA: 2009597
- Nome Completo: Marcelo Beverari do Nascimento Filho
- RA: 1997165
- Nome Completo: Mateus Felix de Moura dos Santos
- RA: 1998770

---

## Descrição do Sistema

Este projeto é um sistema de gerenciamento de campeões do jogo League of Legends, implementado em Python. O sistema permite o cadastro de campeões, a associação de regiões a eles, a adição de campeões a uma fila de combate e a realização de confrontos entre campeões.

### Funcionalidades

- **Cadastro de Campeões**: Permite ao usuário cadastrar novos campeões com nome, função, tipo de dano e habilidades.
- **Associação de Região**: O usuário pode associar uma região a um campeão já cadastrado.
- **Listagem de Campeões**: Exibe todos os campeões cadastrados com seus atributos e habilidades.
- **Fila de Combate**: Adiciona campeões a uma fila para confrontos e permite iniciar confrontos entre os dois primeiros campeões da fila.
- **Remoção de Campeões da Fila**: Permite remover um campeão da fila de combate pelo nome.

---

## Requisitos para Execução

Para executar o sistema, você precisará ter o Python instalado em sua máquina. O código foi testado com Python 3.6 ou superior. 

### Instalação de Dependências

1. **Instale o Python**: Caso não tenha o Python instalado, você pode baixá-lo em [python.org](https://www.python.org/downloads/).
2. **Clone o repositório**: Utilize o comando abaixo para clonar o repositório:
   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   ```
3. **Navegue até o diretório do projeto**:
   ```bash
   cd seu_repositorio
   ```

4. **Execute o script**: Para iniciar o sistema, execute o seguinte comando:
   ```bash
   python champ_manager.py
   ```

---

## Estrutura do Código

O código é organizado em várias funções e classes, cada uma responsável por uma parte específica do sistema. Abaixo, detalhamos cada uma delas:

### 1. Lista Principal de Campeões

```python
campeoes = []
```
- **Descrição**: Esta lista armazena todos os campeões cadastrados no sistema. Cada campeão é representado como um dicionário contendo suas informações.

### 2. Função `criar_campeao()`

```python
def criar_campeao() -> Dict:
```
- **Descrição**: Esta função permite ao usuário cadastrar um novo campeão.
- **Funcionamento**:
  - Solicita ao usuário o nome, função, tipo de dano e habilidades do campeão.
  - Armazena as habilidades em um conjunto para evitar duplicatas.
  - Cria um dicionário com as informações do campeão e o adiciona à lista `campeoes`.
  - Exibe uma mensagem de sucesso após o cadastro.

### 3. Função `associar_regiao()`

```python
def associar_regiao():
```
- **Descrição**: Permite associar uma região a um campeão já cadastrado.
- **Funcionamento**:
  - Verifica se há campeões cadastrados.
  - Exibe a lista de campeões e suas regiões atuais.
  - Solicita ao usuário que escolha um campeão e insira a nova região.
  - Atualiza a região do campeão selecionado e exibe uma mensagem de sucesso.

### 4. Função `listar_campeoes()`

```python
def listar_campeoes():
```
- **Descrição**: Lista todos os campeões cadastrados com seus atributos.
- **Funcionamento**:
  - Verifica se há campeões cadastrados.
  - Itera sobre a lista de campeões e exibe suas informações, incluindo nome, função, tipo de dano, região e habilidades.

### 5. Classe `NoDuplo`

```python
class NoDuplo:
```
- **Descrição**: Representa um nó em uma lista duplamente encadeada.
- **Atributos**:
  - `campeao`: Armazena o campeão associado ao nó.
  - `anterior`: Referência para o nó anterior na lista.
  - `proximo`: Referência para o próximo nó na lista.

### 6. Classe `FilaCombate`

```python
class FilaCombate:
```
- **Descrição**: Implementa uma fila de combate usando uma lista duplamente encadeada.
- **Métodos**:
  - `esta_vazia()`: Verifica se a fila está vazia.
  - `enfileirar(campeao)`: Adiciona um campeão ao final da fila.
  - `desenfileirar()`: Remove e retorna o campeão do início da fila.
  - `mostrar_fila()`: Exibe todos os campeões na fila de combate.
  - `remover_por_nome(nome)`: Remove um campeão da fila pelo nome.

### 7. Função `adicionar_a_fila()`

```python
def adicionar_a_fila():
```
- **Descrição**: Adiciona um campeão à fila de combate.
- **Funcionamento**:
  - Verifica se há campeões cadastrados.
  - Exibe a lista de campeões disponíveis.
  - Solicita ao usuário que escolha um campeão para adicionar à fila.
  - Chama o método `enfileirar` da classe `FilaCombate` para adicionar o campeão.

### 8. Função `iniciar_confronto()`

```python
def iniciar_confronto():
```
- **Descrição**: Inicia um confronto entre os dois primeiros campeões da fila de combate.
- **Funcionamento**:
  - Verifica se a fila de combate está vazia.
  - Desenfileira os dois primeiros campeões.
  - Se houver apenas um campeão, ele permanece na fila.
  - Escolhe aleatoriamente um vencedor entre os dois campeões e exibe o resultado.

### 9. Função `remover_da_fila()`

```python
def remover_da_fila():
```
- **Descrição**: Remove um campeão da fila de combate pelo nome.
- **Funcionamento**:
  - Solicita ao usuário que insira o nome do campeão a ser removido.
  - Chama o método `remover_por_nome` da classe `FilaCombate` para realizar a remoção.

### 10. Função `main()`

```python
def main():
```
- **Descrição**: Função principal que exibe o menu do sistema e gerencia a interação do usuário.
- **Funcionamento**:
  - Exibe um menu com opções para o usuário.
  - Chama as funções apropriadas com base na escolha do usuário.
  - Permite que o usuário saia do sistema.

---

## Conclusão

Este sistema de gerenciamento de campeões é uma ferramenta útil para jogadores e entusiastas de League of Legends, permitindo uma melhor organização e interação com os campeões do jogo. A implementação em Python e a escolha cuidadosa das estruturas de dados garantem eficiência e facilidade de uso.

## Explicação do Sistema

O sistema é uma aplicação de linha de comando (CLI) que permite ao usuário interagir com um conjunto de campeões do jogo League of Legends. As principais funções do sistema são:

- **Cadastro de Campeões**: O usuário pode inserir informações sobre um novo campeão, incluindo nome, função, tipo de dano e habilidades. Essas informações são armazenadas em uma lista de dicionários.

- **Associação de Região**: O sistema permite que o usuário associe uma região a um campeão já cadastrado, facilitando a organização dos campeões por suas respectivas regiões.

- **Listagem de Campeões**: O usuário pode visualizar todos os campeões cadastrados, incluindo suas habilidades e regiões associadas.

- **Fila de Combate**: Os campeões podem ser adicionados a uma fila de combate, onde dois campeões são selecionados aleatoriamente para um confronto. O vencedor é escolhido aleatoriamente entre os dois.

- **Remoção de Campeões da Fila**: O usuário pode remover um campeão da fila de combate pelo nome, permitindo uma gestão dinâmica da fila.

---

## Conclusão

Este sistema de gerenciamento de campeões é uma ferramenta útil para jogadores e entusiastas de League of Legends, permitindo uma melhor organização e interação com os campeões do jogo. A implementação em Python e a escolha cuidadosa das estruturas de dados garantem eficiência e facilidade de uso.
