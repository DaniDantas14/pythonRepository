''' Python for Girls

    Exercicio final, turma 2

    JOKENPO

AUTHORS 

1. Camila Campelo
2. Carolina de Oliveira
3. Daniela Dantas
4. Maria Laura
'''
# %%
print("\033[35m===================================" + "\n\033[35m        PYTHON FOR GIRLS        " + "\n\033[35m SEJA BEM VINDO AO JOGO DE JOKENPO " + "\n\033[35m===================================")
print("\n\033[97mMenu de opções: \n [1] PEDRA" + "\n [2] PAPEL" + "\n [3] TESOURA")
jogador1 = ""
jogador2 = ""
while jogador1 == "":
    jogador1 = input("\n\033[36mJogador(a) 1, digite o seu nome: ")
while jogador2 == "":
    jogador2 = input("\n\033[36mJogador(a) 2, digite o seu nome: ")

def partida(num_partida):
    campeao = ""
    jogada1 = int(input(f"\n\033[32m{jogador1}, digite a sua {num_partida}ª jogada: "))
    while jogada1 not in [1,2,3]:
       print("Opção inválida. Favor entrar com : [1] PEDRA, [2] PAPEL ou [3] TESOURA")
       jogada1 = int(input(f"\n\033[32m{jogador1}, digite a sua {num_partida}ª jogada: "))
    
    jogada2 = int(input(f"\n\033[32m{jogador2}, digite a sua {num_partida}ª jogada: "))
    while jogada2 not in [1,2,3]:
       print("Opção inválida. Favor entrar com : [1] PEDRA, [2] PAPEL ou [3] TESOURA")
       jogada2 = int(input(f"\n\033[32m{jogador2}, digite a sua {num_partida}ª jogada: "))
    
    if jogada1 == jogada2:
       print("Não tivemos vencedor. Repetir Rodada.")
    elif (jogada1 == 1 and jogada2 == 3) or (jogada1 == 3 and jogada2 == 2) or (jogada1 == 2 and jogada2 == 1):
        campeao = "jogador1"
    elif (jogada2 == 1 and jogada1 == 3) or (jogada2 == 3 and jogada1 == 2) or (jogada2 == 2 and jogada1 == 1):
        campeao = "jogador2"
    else:
        campeao = "jogador2"

    return campeao

resultado = []

for i in range(3):
    resultado.append(partida(i+1))
    while resultado[i] == "":
        resultado[i]= partida(i+1)

vitoriap1 = 0
vitoriap2 = 0

for i in range(3):
    if resultado[i] == 'jogador1':
        vitoriap1 += 1
    else:
        vitoriap2 += 1
    
if vitoriap1 == vitoriap2:
    print("\033[31mResultado : Empate")
elif vitoriap1 > vitoriap2:
    print(f"\n\033[33mResultado : Jogador(a) {jogador1} venceu!")
else:
    print(f"\n\033[33mResultado : Jogador(a) {jogador2} venceu!")

print(f"\n\n\033[35mNa primeira rodada, {resultado[0]} venceu. \nNa segunda rodada, {resultado[1]} venceu. \nNa terceira rodada, {resultado[2]}  venceu. \n\nParabéns pelo jogo!")





# %%

# %%
