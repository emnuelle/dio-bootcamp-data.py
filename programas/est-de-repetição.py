# praticando estruturas de repetição

#  Comando "for"

texto = input("informe um texto: ")
vogais = "AEIOU"

for letra in texto:
    if  letra.upper() in vogais:
        print(letra, end="")

print() #quebra de linha

# "for/else"

texto = input("informe um texto: ")
vogais = "AEIOU"

for letra in texto:
    if  letra.upper() in vogais:
        print(letra, end="")
else:
    print("lero-lero")

# range

list(range(4))

# range com for 
for numero in range(0,11):
    print(numero, end="")

# while

opcao = 1

while opcao != 0:
    opcao = int(input("{1} sacar \n{2} extrato \n{0} sair"))

    if opcao == 1:
        print("sacando...")
    elif opcao == 2:
        print("exibindo o extrato...")
else:
    print("obrigada por utilizar o sistema")