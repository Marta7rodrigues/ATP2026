#Programa dos números

listaNumeros = []
escolha = -1
import random
print ("-------------------------------------------")
print("Bem vindo a aplicação das listas!")

while escolha != 0:
  print ("-Menu-")
  print ("(1) Criar lista.")
  print ("(2) Ler lista.")
  print ("(3) Soma.")
  print ("(4) Média.")
  print ("(5) Maior.")
  print ("(6) Menor.")
  print ("(7) estaOrdenada por ordem crescente.")
  print ("(8) estaOrdenada por ondem decrescente.")
  print ("(9) Procurar um elemento.")
  print ("(0) Sair da aplicação.")
  print ("------------------------------------------")
  
  escolha = int(input("Selecione a operação de deseja realizar, escrevendo aqui o número correspondente:"))


  if escolha == 0:
    print (f"Saiu do programa, obrigada por nos ter escolhido! A sua lista final é {listaNumeros}.")

  elif escolha == 1:
        listaNumeros = []
        for i in range(10):
            numeroAleatorio = random.randint(1, 100)
            listaNumeros.append(numeroAleatorio)
        print("Lista criada com sucesso!")
        print(listaNumeros)
        
  elif escolha == 2:
        listaNumeros = []
        quantidade = int(input("Quantos números queres meter na lista? "))
        for i in range(quantidade):
            num = int(input(f"Introduz o {i+1}º número: "))
            listaNumeros.append(num)
        print("Lista lida com sucesso!")
        print(listaNumeros)

  elif escolha == 3:
        if len(listaNumeros) == 0:
            print("A lista está vazia!")
        else:
            soma = 0
            for numero in listaNumeros:
                soma += numero
            print(f"A soma dos elementos é: {soma}")

  elif escolha == 4:
        if len(listaNumeros) == 0:
            print("A lista está vazia!")
        else:
            media = sum(listaNumeros) / len(listaNumeros)
            print(f"A média dos elementos é: {media}")

  elif escolha == 5:
        if len(listaNumeros) == 0:
            print("A lista está vazia!")
        else:
            maior = max(listaNumeros)
            print(f"O maior elemento é: {maior}")

  elif escolha == 6:
        if len(listaNumeros) == 0:
            print("A lista está vazia!")
        else:
            menor = min(listaNumeros)
            print(f"O menor elemento é: {menor}")

  elif escolha == 7:
        if len(listaNumeros) == 0:
            print("A lista está vazia!")
        else:
            if listaNumeros == sorted(listaNumeros):
                print("A lista está ordenada por ordem crescente.")
            else:
                print("A lista não está ordenada por ordem crescente.")

  elif escolha == 8:
        if len(listaNumeros) == 0:
            print("A lista está vazia!")
        else:
            if listaNumeros == sorted(listaNumeros, reverse=True):
                print("A lista está ordenada por ordem decrescente.")
            else:
                print("A lista não está ordenada por ordem decrescente.")   

  elif escolha == 9:
        if len(listaNumeros) == 0:
            print("A lista está vazia!")
        else:
            elemento = int(input("Introduza o elemento que deseja procurar: "))
            posicao = -1
            i = 0
            while i < len(listaNumeros) and posicao == -1:
                if listaNumeros[i] == elemento:
                    posicao = i
                i = i + 1

            if elemento in listaNumeros and posicao != -1:

                
                print(f"O elemento {elemento} foi encontrado na lista, na posição {posicao + 1}.")
            else:
                print(f"O elemento {elemento} não foi encontrado na lista.")
  