import random

while True:
    print("== DUELO DE HERÓIS ==")
    escolha = int(input("1 - Iniciar jogo\n"
                        "2 - Sair do jogo\n"
                        "Escolha a opção que deseja realizar: "))

    if escolha == 2:
        print("Jogo encerrado.")
        break
    else:
        jogador = input("\nDigite seu nick: ")
        inimigo = "inimigo"

        hp = random.randint(50, 200)
        ataque1 = random.randint(1, 50)
        defesa1 = random.randint(1, 50)
        print(f"\n== {jogador} ==")
        print(f"HP: {hp}")
        print(f"ATQ: {ataque1}     DF: {defesa1}\n")

        ataque2 = random.randint(1, 50)
        defesa2 = random.randint(1, 50)
        print(f"== {inimigo} ==")
        print(f"HP: {hp}")
        print(f"ATQ: {ataque2}     DF: {defesa2}")

        hp_jog1 = hp
        hp_inimigo = hp

        rodada = 1
        while hp_jog1 > 0 and hp_inimigo > 0:

            print(f"\n== Turno {rodada} ==")
            print(f"HP de {jogador}: {hp_jog1} | HP de {inimigo}: {hp_inimigo}")
            acao_dict = {1: "atacar", 2: "curar"}
            acao = int(input(f"Vez de {jogador}. Escolha: [1] Atacar ou [2] Curar? "))
            print(f"\n{jogador} escolheu {acao_dict.get(acao, 'Opção inválida')}")
            if acao == 1:
                ataque = ataque1 - defesa2
                if ataque <= 0:
                    ataque = ataque1 - defesa2
                ataque = max(ataque, 0)
                print(f"O dano em {inimigo} foi de:", ataque)
                hp_inimigo -= ataque
            elif acao == 2:
                hp_jog1 += 10

            acao = random.choice(["atacar", "curar"])
            print(f"\n{inimigo} escolheu {acao}")
            if acao == "atacar":
                ataque = ataque2 - defesa1
                if ataque <= 0:
                    ataque = ataque2 - defesa1
                ataque = max(ataque, 0)
                print(f"O dano em {jogador} foi de:", ataque)
                hp_jog1 -= ataque

            elif acao == "curar":
                hp_inimigo += 10

            rodada += 1

    print("\n=== FIM DO JOGO ===")
    if hp_jog1 <= 0:
        print(f"{inimigo} venceu!")
    elif hp_inimigo <= 0:
        print(f"{jogador} venceu!")
