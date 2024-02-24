menu = """
-------------------------------------
-     BEM VINDO(A) A SUA CONTA      - 
-------------------------------------
Opções:

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
-------------------------------------
Escolha uma opção:
"""

saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
        
    if opcao == "d":
        print("-------------- DEPÓSTIO --------------\n")
        valor = float(input("Qual o valor do depósito? R$ "))
        
        if valor >= 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n" f"Depósito de R$ {valor:.2f}  realizado com sucesso!")

        else:
            print("Depósito não realizado! Valor informado inválido!\n")
                                
    elif opcao == "s":
        print("--------------- SAQUE ---------------\n")
        valor = float(input("Qual o valor do saque? R$ "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = num_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
             print("\nSaque não realizado! Saldo insuficiente!\n")            
        
        elif excedeu_limite:
             print("\nSaque não realizado! Valor informado excedeu o limite!\n")
        
        elif excedeu_saques:
             print("\nSaque não realizado! Número de saques excedido!\n")
        
        elif valor > 0: 
            saldo -= valor
            extrato += "\n"f"Saque: R$ {valor:.2f}\n"
            num_saques += 1
        
        else:
            print("\nSaque não realizado! Valor de saque inválido!\n")     
   
    elif opcao == "e":
        
        print("-------------- EXTRATO --------------\n")
        print("\nNão foram realizadas transações!" if not extrato else extrato)
        print("\n")
        print("Quantidade de saques realizados: ", num_saques)
        print("-------------------------------------")
        print(f"Saldo: R$ {saldo:.2f}") 
        print("-------------------------------------")
        
               
    elif opcao == "q":
        print("Opção SAIR escolhida!")
        print("Saindo...")
        
        break
    
    else:
        print("\nOpção inválida! Informe a operação desejada.")    
            
print(menu)