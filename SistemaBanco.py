
menu_dirc = {
1: "1 - Saque",
2: "2 - Depósito",
3: "3 - Extrato",
0: "0 - Sair"
}


saldo = 0
limite_saque = 0
saques_diarios = 0
saques_realizados = 0
valores_sacados = 0
valores_depositados = 0
depositos = 0



while True:
    
    print("Bem Vindo ao seu App Bancário")

    for i in menu_dirc:
      print(menu_dirc[i])
    opcao_desejada = int(input("Digite a operação que deseja realizar: "))
    
    if opcao_desejada == 1:
        print("Você Selecionou Opção Depósito")
        valor = float(input("Informe o valor do Depósito: "))

        if valor > 0:
            saldo += valor
            depositos += valor
    
    elif opcao_desejada == 2:
        print("Voce Selecionou a Opção Saque")
        valor = float(input("Informe o Valor Que Deseja Sacar: "))

        if valor > saldo:
            print("Saldo Insuficiente")

        elif valor <= 0 :
            print("Valor de Saque NÃO pode ser menor ou igual a zero")    
        
        elif saques_diarios == 3:
            print("Saques Diarios Excedidos. Entre em contato com seu Gerente")

        elif limite_saque >= float(500):
            print("Valor limite para Saques Excedidos. Entre em contato com seu Gerente")      

        elif (limite_saque + valor) > float(500):
            print("Valor Excede o Valor Limite permitido para Saque")  

        elif valor < saldo and limite_saque < float(500) and saques_diarios < 3:
            saldo -= valor
            limite_saque += valor
            saques_diarios += 1               

    elif opcao_desejada == 3:
        print(f'''
              
      ========== Extrato ==========

Saldo: R$ {saldo:.2f} 

Depositos: R$ {depositos:.2f}

Saques Diarios Efetuados: {saques_diarios}

Valor Sacado no Dia: R$ {limite_saque:.2f}

            === FIM ===

''')

    elif opcao_desejada == 0:
        print("Fechamento Solicitado. Tenha um òtimo Dia!!!")
        break    
    