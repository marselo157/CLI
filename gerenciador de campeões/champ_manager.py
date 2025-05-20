# Sistema de gerenciamento de campeões do League of Legends (CLI)
from typing import Dict, Tuple, Set
import random

# Lista principal de campeões
campeoes = []

# Função para criar um campeão
def criar_campeao() -> Dict:
    print("\n=== Cadastro de Campeão ===")
    nome = input("Nome do campeão: ").strip().title()
    funcao = input("Função (Ex: Mago, Lutador, Assassino): ").strip().title()
    tipo_dano = input("Tipo de dano (Físico/Mágico/Misto): ").strip().title()

    atributos_fixos: Tuple[str, str] = (funcao, tipo_dano)

    habilidades: Set[str] = set()
    while True:
        habilidade = input("Adicione uma habilidade (ou pressione Enter para sair): ").strip()
        if habilidade == "":
            break
        habilidades.add(habilidade.title())

    campeao: Dict = {
        "nome": nome,
        "atributos": atributos_fixos,
        "habilidades": habilidades,
        "regiao": None,
        "id": nome.lower().replace(" ", "_")
    }

    campeoes.append(campeao)
    print(f"Campeão {nome} cadastrado com sucesso!")

# Função para associar uma região a um campeão
def associar_regiao():
    print("\n=== Associação de Região ao Campeão ===")

    if not campeoes:
        print("Nenhum campeão cadastrado.")
        return

    print("Campeões cadastrados:")
    for i, campeao in enumerate(campeoes):
        print(f"{i + 1}. {campeao['nome']} (Região atual: {campeao['regiao'] or 'Nenhuma'})")

    try:
        escolha = int(input("Selecione o número do campeão para associar uma região: ")) - 1
        if escolha < 0 or escolha >= len(campeoes):
            print("Escolha inválida.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    regiao = input("Digite a região para associar (Ex: Demacia, Noxus, Ionia): ").strip().title()
    campeoes[escolha]["regiao"] = regiao

    print(f"Região '{regiao}' associada com sucesso ao campeão {campeoes[escolha]['nome']}.")

# Função para listar os campeões cadastrados
def listar_campeoes():
    print("\n=== Campeões Cadastrados ===")
    if not campeoes:
        print("Nenhum campeão cadastrado.")
        return

    for i, campeao in enumerate(campeoes, start=1):
        nome = campeao["nome"]
        funcao, tipo_dano = campeao["atributos"]
        habilidades = ", ".join(campeao["habilidades"]) if campeao["habilidades"] else "Nenhuma"
        regiao = campeao["regiao"] or "Nenhuma"

        print(f"\nCampeão {i}:")
        print(f"  Nome: {nome}")
        print(f"  Função: {funcao}")
        print(f"  Tipo de Dano: {tipo_dano}")
        print(f"  Região: {regiao}")
        print(f"  Habilidades: {habilidades}")

# Nó da lista duplamente encadeada
class NoDuplo:
    def __init__(self, campeao):
        self.campeao = campeao
        self.anterior = None
        self.proximo = None

# Lista duplamente encadeada usada como fila de combate
class FilaCombate:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.inicio is None

    def enfileirar(self, campeao):
        novo_no = NoDuplo(campeao)
        if self.esta_vazia():
            self.inicio = self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            novo_no.anterior = self.fim
            self.fim = novo_no

    def desenfileirar(self):
        if self.esta_vazia():
            return None
        campeao = self.inicio.campeao
        self.inicio = self.inicio.proximo
        if self.inicio:
            self.inicio.anterior = None
        else:
            self.fim = None
        return campeao

    def mostrar_fila(self):
        atual = self.inicio
        i = 1
        print("\n=== Fila de Combate ===")
        if self.esta_vazia():
            print("Fila vazia.")
            return
        while atual:
            print(f"{i}. {atual.campeao['nome']}")
            atual = atual.proximo
            i += 1

    def remover_por_nome(self, nome):
        atual = self.inicio
        while atual:
            if atual.campeao["nome"].lower() == nome.lower():
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.inicio = atual.proximo
                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.fim = atual.anterior
                print(f"Campeão '{nome}' removido da fila.")
                return
            atual = atual.proximo
        print(f"Campeão '{nome}' não encontrado na fila.")

    def esta_na_fila(self, campeao):
        atual = self.inicio
        while atual:
            if atual.campeao["id"] == campeao["id"]:
                return True
            atual = atual.proximo
        return False

# Instância global da fila de combate
fila_combate = FilaCombate()

# Adiciona um campeão à fila de combate
def adicionar_a_fila():
    print("\n=== Adicionar à Fila de Combate ===")
    if not campeoes:
        print("Nenhum campeão cadastrado.")
        return

    print("Campeões disponíveis:")
    for i, campeao in enumerate(campeoes):
        print(f"{i + 1}. {campeao['nome']}")

    try:
        escolha = int(input("Escolha o número do campeão para entrar na fila: ")) - 1
        if escolha < 0 or escolha >= len(campeoes):
            print("Escolha inválida.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    campeao_escolhido = campeoes[escolha]
    if fila_combate.esta_na_fila(campeao_escolhido):
        print(f"O campeão '{campeao_escolhido['nome']}' já está na fila de combate.")
    else:
        fila_combate.enfileirar(campeao_escolhido)
        print(f"{campeao_escolhido['nome']} foi adicionado à fila de combate!")

# Inicia um confronto entre os dois primeiros campeões da fila
def iniciar_confronto():
    print("\n=== Iniciar Confronto ===")
    if fila_combate.esta_vazia():
        print("Fila de combate vazia.")
        return

    c1 = fila_combate.desenfileirar()
    c2 = fila_combate.desenfileirar()

    if not c2:
        print(f"Aguardando mais um campeão para o confronto. {c1['nome']} continua na fila.")
        fila_combate.enfileirar(c1)
        return

    vencedor = random.choice([c1, c2])
    perdedor = c1 if vencedor == c2 else c2

    print(f"Confronto: {c1['nome']} VS {c2['nome']}")
    print(f"Vencedor: {vencedor['nome']}")

# Remove um campeão da fila de combate pelo nome
def remover_da_fila():
    print("\n=== Remover Campeão da Fila ===")
    while True:
        nome = input("Digite o nome do campeão a remover da fila: ").strip()
        if nome:
            break
        print("O nome tem que ser informado. Tente novamente.")
    fila_combate.remover_por_nome(nome)

# Menu principal do sistema
def main():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Cadastrar um campeão")
        print("2. Associar região a um campeão")
        print("3. Ver todos os campeões cadastrados")
        print("4. Adicionar à fila de combate")
        print("5. Iniciar próximo confronto")
        print("6. Ver fila de combate atual")
        print("7. Remover campeão da fila")
        print("8. Sair")

        opcao = input("Escolha uma opção (1-8): ").strip()

        if opcao == "1":
            criar_campeao()
        elif opcao == "2":
            associar_regiao()
        elif opcao == "3":
            listar_campeoes()
        elif opcao == "4":
            adicionar_a_fila()
        elif opcao == "5":
            iniciar_confronto()
        elif opcao == "6":
            fila_combate.mostrar_fila()
        elif opcao == "7":
            remover_da_fila()
        elif opcao == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
