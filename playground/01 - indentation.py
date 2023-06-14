# program 1

print("Começando o programa!")

cont = 1 # criando uma variável

while cont < 10:
    if cont % 2 == 0:   # estrutura de decisão
        print(f"É par {cont}")
    else:
        print(f"É ímpar {cont}")
    cont+=1 # atualizando o valor da variável

print("fim")