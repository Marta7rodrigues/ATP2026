#Jogo dos 100

print ("Bem vindo ao jogo dos 100!")
print ("O objetivo do jogo é jogar números de 1 a 10, alternadamente, até que a soma total seja igual a 100. Quem chegar primeiro a 100 vence o jogo!")
print ("--------------------------------")
print ("Modalidades disponíveis:")
print ("(1) O computador começa a jogar.")
print ("(2) O jogador começa a jogar.")

modalidade = int(input("Escolha a modalidade: "))

total = 0

if modalidade == 1:
    print ("O computador começa a jogar!")

    computador = 1
    total = total + computador
    print(f"O computador jogou {computador}. Soma total: {total}")

while total < 100:
    print ("Agora é a sua vez de jogar!")
    limite_maximo = 100 - total 
    if limite_maximo > 10:
        limite_maximo = 10
    jogador = int(input(f"Escolha um número de 1 a {limite_maximo}: "))

    total = total + jogador
    print(f"Você jogou {jogador}. Soma total: {total}")

    if total == 100:
        print ("Parabéns! Venceu o jogo!")
    else:
        computador = 11 - jogador
        total = total + computador
        print(f"O computador jogou {computador}. Soma total: {total}")

        if total == 100:
            print ("O computador venceu o jogo! Tente novamente.")
        
