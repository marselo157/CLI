from typing import Dict, Tuple, Set

campeoes = []

def criar_campeao() -> Dict:
    print("=== Cadastro de Campeão ===")
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

def associar_regiao():
    print("=== Associação de Região ao Campeão ===")

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

def listar_campeoes():
    print("=== Campeões Cadastrados ===")
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

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Cadastrar um campeão")
        print("2. Listar campeões e associar região")
        print("3. Ver todos os campeões cadastrados")
        print("4. Sair")

        opcao = input("Escolha uma opção (1/2/3/4): ").strip()

        if opcao == "1":
            criar_campeao()
        elif opcao == "2":
            associar_regiao()
        elif opcao == "3":
            listar_campeoes()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()