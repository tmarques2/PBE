import random

while True:
    print("== DUELO DE HERÓIS ==")
    menu = int(input("1 - Iniciar jogo\n"
                    "2 - Sair do jogo\n"
                    "Escolha a opção que deseja realizar: "))

    if menu == 2:
        print("Jogo encerrado.")
        break
    
    else:

        escolha = int(input("Escolha como deseja jogar(1 ou 2):"
                            "\n1 - Contra CPU"
                            "\n2 - 2 jogadores\n"))

        if escolha == 1:
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
        else:
            jogador1 = input("\nDigite o nick do jogador 1: ")
            jogador2 = input("\nDigite o nick do jogador 2: ")

            
            hp = random.randint(10, 20)
            ataque1 = random.randint(1, 50)
            defesa1 = random.randint(1, 50)
            print(f"\n== {jogador1} ==")
            print(f"HP: {hp}")
            print(f"ATQ: {ataque1}     DF: {defesa1}\n")

            ataque2 = random.randint(1, 50)
            defesa2 = random.randint(1, 50)
            print(f"== {jogador2} ==")
            print(f"HP: {hp}")
            print(f"ATQ: {ataque2}     DF: {defesa2}")

            hp_jog1 = hp
            hp_jog2 = hp

            rodada = 1
            while hp_jog1 > 0 and hp_jog2 > 0:

                print(f"\n== Turno {rodada} ==")
                print(f"HP de {jogador1}: {hp_jog1} | HP de {jogador2}: {hp_jog2}")
                acao_dict = {1: "atacar", 2: "curar"}
                acao = int(input(f"\nVez de {jogador1}. Escolha: [1] Atacar ou [2] Curar? "))
                print(f"\n{jogador1} escolheu {acao_dict.get(acao, 'Opção inválida')}")
                if acao == 1:
                    ataque = ataque1 - defesa2
                    if ataque <= 0:
                        ataque = ataque1 - defesa2
                    ataque = max(ataque, 0)
                    print(f"O dano em {jogador2} foi de:", ataque)
                    hp_jog2 -= ataque
                elif acao == 2:
                    hp_jog1 += 10


                acao_dict = {1: "atacar", 2: "curar"}
                acao = int(input(f"\nVez de {jogador2}. Escolha: [1] Atacar ou [2] Curar? "))
                print(f"\n{jogador2} escolheu {acao_dict.get(acao, 'Opção inválida')}")
                if acao == 1:
                    ataque = ataque2 - defesa1
                    if ataque <= 0:
                        ataque = ataque2 - defesa1
                    ataque = max(ataque, 0)
                    print(f"O dano em {jogador1} foi de:", ataque)
                    hp_jog1 -= ataque
                elif acao == 2:
                    hp_jog2 += 10

        print("\n=== FIM DO JOGO ===")
        if hp_jog2 <= 0:
            print(f"{jogador1} venceu!\n")
        elif hp_jog1 <= 0:
            print(f"{jogador2} venceu!\n")
    