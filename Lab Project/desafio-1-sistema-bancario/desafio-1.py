# Operação de depósito


print("Bem vindo ao nosso sitema bancário!\n")

saldo = str(0)

print("Digite a operação desejada:\n[1]\tDepósito\n[2]\tExtrato bancário\n[3]\tSaque")
escolha = int(input())

if escolha == 1:
    print(f"Saldo atual R${saldo}\nVocê selecionou Depósito, qual é o valor que deseja depositar na sua conta?")
    deposito = str(input())
    saldo += deposito
    print(f"Você adicionou R${deposito} à sua conta!\nSeu saldo atual é R${saldo}")
elif escolha == 2:
    print(f"EXTRATO BANCÁRIO\nSaldo atual R${saldo}\n*")
    
    
        
