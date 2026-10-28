#Trabalho Avaliativo - Protótipo de Produto De Sw - Pousada
#Curso: ADS 
#Turno: Matutino
#Nome: Fernando Massahiro Ogi
#Nome: Vinicius Amorim Oliveira
#Nome: Natan Augusto de Paula Cavalcante


from tabulate import tabulate
import os
verde = "\033[0;32m"
resetar = "\033[0m"
vermelho = "\033[31m"

funcionario = []#Aqui foi criado uma lista chamado de funcionario
while True:
    os.system("cls")

    relat =f''' 
    {verde}
[0;37m    ▄▄[0;90m▄[0;37m    [0;97m▄▄[0;37m▄▄▄[0;90m▄▄▄▄[0;37m       ▄▄[0;90m▄[0;37m     [0;97m▄[0;37m▄▄▄[0;90m▄▄▄▄[0;37m    [0;97m▄▄[0;37m▄▄▄[0;90m▄▄▄▄▄▄▄[0;37m    ▄▄[0;90m▄[0;37m     [0;97m▄▄[0;37m▄▄▄      [0;90m▄▄▄[0;37m  [0;97m▄▄[0;37m▄▄▄[0;90m▄▄▄▄▄[0;37m [0;97m▄▄[0;37m▄▄    [0;97m▄[0;37m▄[0;90m▄▄▄[0;37m [0;97m▄▄[0;37m▄▄▄[0;90m▄▄▄▄▄▄▄[0;37m    [0;97m▄[0;37m▄▄▄[0;90m▄[0;37m    [0m
[0;37m  [0;97m▄[0;97;41m▀[0;91;41m█▓▓[0;90;41m▀[0;90m▄[0;37m  [0;97;47m▐[0;91;41m░▒▒▒▓▓▓█░[0;90m▄[0;37m   [0;97m▄[0;97;41m▀[0;91;41m█▓▓[0;90;41m▀[0;90m▄[0;37m  [0;97;47m▌[0;91;41m░▒▒▒▓▓▓█░[0;90m▄[0;37m  [0;97;41m▌ [0;91;41m░░▒▒▒▒▓▓█[0;90m▌[0;37m  [0;97m▄[0;97;41m▀[0;91;41m█▓▓[0;90;41m▀[0;90m▄[0;37m  [0;97m▀[0;97;41m▄[0;91;41m░▒▒▒[0;90m█[0;37m   [0;97m▄[0;37;41m▀[0;91;41m▒░[0;90;41m▄[0;90m▀[0;97m▀[0;97;41m▄[0;91;41m░▒▒▒▓▓▓█[0;90;41m▐[0;97m▀[0;97;41m▄[0;91;41m░▒▒▒[0;90m▄[0;37m ▀[0;90;41m▄[0;31m▓[0;91;41m▒░[0;90;41m▀[0;90m▌[0;97;41m▌ [0;91;41m░░▒▒▒▒▓▓█[0;90m▌[0;37m  [0;97m▄[0;97;41m▀[0;91;41m░▒▒▒░[0;90;41m▀[0;90m▄[0;37m  [0m
[0;37m  [0;97;41m▌[0;91;41m▓[0;90;41m▄[0;90m▀[0;90;41m▄[0;91;41m▒[0;90;41m▐[0;37m   [0;31;47m▐[0;91;41m░▒[0;90;41m▄[0;90m▀▀▀▐[0;91;41m▓░[0;90m▌[0;37m  [0;97;41m▌[0;91;41m▓[0;90;41m▄[0;90m▀[0;90;41m▄[0;91;41m▒[0;90;41m▐[0;37m  [0;97m▐[0;31;47m▐[0;91;41m░▒[0;90;41m▄[0;90m▀▀▀▐[0;91;41m▓░[0;90m▌[0;37m ▀[0;90m▀▀▀[0;90;41m▌[0;91;41m░▒[0;90;41m▐[0;90m▀▀▀[0;37m   [0;97;41m▌[0;91;41m▓[0;90;41m▄[0;90m▀[0;90;41m▄[0;91;41m▒[0;90;41m▐[0;37m    [0;31;47m▐[0;91;41m░▒▓▒[0;90;47m▄[0;37m▄[0;37;41m▀[0;91;41m░▓░[0;90;41m▐[0;90m▌[0;37m   [0;31;47m▐[0;91;41m░▒[0;90;41m▄[0;90m▀▀▀[0;90;41m▄[0;90m█[0;37m  [0;31;47m▐[0;91;41m░▒▓▒[0;90m█[0;37m  [0;90;47m▌[0;91;41m░[0;90;41m▓[0;31m█[0;90m▌[0;37m▀[0;90m▀▀▀[0;90;41m▌[0;91;41m░▒[0;90;41m▐[0;90m▀▀▀[0;37m  [0;97m▐[0;91;41m░░[0;90;41m▄[0;90m▀▀▀[0;90;41m▄[0;91;41m░░[0;90m▌[0;37m [0m
[0;37m ▐[0;91;41m▒▒[0;90m▌[0;37m ▐[0;91;41m░▒[0;90m▌[0;37m  [0;31;47m▐[0;31m▓[0;31;41m [0;90;41m▐[0;90m▌[0;37m [0;97m▄[0;37;41m▀[0;90;41m▄[0;90m▀[0;37m  ▐[0;91;41m▒▒[0;90m▌[0;37m ▐[0;91;41m░▒[0;90m▌[0;37m  [0;31;47m▐[0;31m▓[0;31;41m [0;90;41m▐[0;90m▌[0;37m [0;97m▄[0;37;41m▀[0;90;41m▄[0;90m▀[0;37m      [0;90;41m▌ [0;91;41m░[0;90;41m▐[0;37m     ▐[0;91;41m▒▒[0;90m▌[0;37m ▐[0;91;41m░▒[0;90m▌[0;37m   [0;31;47m▐[0;31m▓[0;31;41m [0;90;41m▐[0;90m█[0;31m█▒█▓[0;90;41m░▓[0;90m█[0;37m    [0;31;47m▐[0;31m▓[0;31;41m [0;90;41m▐[0;90m▄▄▄[0;37m    [0;31;47m▐[0;31m▓[0;91;41m░▒▓▒[0;90m▌[0;37m [0;90;47m▐[0;90;41m▓░[0;31m█[0;90m▌[0;37m    [0;90;41m▌ [0;91;41m░[0;90;41m▐[0;37m     [0;97;41m▌[0;31m▓[0;31;41m [0;90m▌[0;37m   ▐[0;31;41m [0;31m▓[0;90;41m▐[0;37m [0m
[0;37m [0;90m▐[0;31m█▓[0;90;41m▀[0;37;41m▀[0;97;41m▀[0;31m▓█[0;90m▌[0;37m  [0;90;41m▌[0;31m▒▓▓[0;90;41m▀[0;37;41m▀[0;90;41m▄[0;90m▀[0;37m    [0;90m▐[0;31m█▓[0;90;41m▀[0;37;41m▀[0;97;41m▀[0;31m▓█[0;90m▌[0;37m  [0;90;41m▌[0;31m▒▓▓[0;90;41m▀[0;37;41m▀[0;90;41m░▀[0;90m▄[0;37m       [0;90m▌[0;31m▓[0;31;41m [0;90;41m▐[0;37m     [0;90m▐[0;31m█▓[0;90;41m▀[0;37;41m▀[0;97;41m▀[0;31m▓█[0;90m▌[0;37m   [0;90;41m▌[0;31m▒▓[0;90m█▌▀[0;90;41m▄[0;90m▀█[0;31m▓[0;90;41m░▐[0;90m▌[0;37m   [0;90;41m▌[0;31m▒▓▓▒░[0;90m▌[0;37m    [0;90;41m▌[0;31m▒▓[0;90m█▌[0;31m█[0;91;41m░[0;31m▄▐▒▓▓[0;90m█[0;37m    [0;90m▌[0;31m▓[0;31;41m [0;90;41m▐[0;37m    ▐[0;31m▓▒[0;90;41m▐[0;37m     [0;37;41m▌[0;31m▒▓[0;90m▌[0m
[0;37m [0;90;41m▌[0;31m▓▒[0;90m▄▄▄[0;31m▒▓[0;90;41m▐[0;37m  [0;90m▌[0;31m░[0;37m [0;90;41m▐[0;90m▀[0;37m▀      [0;90;41m▌[0;31m▓▒[0;90m▄▄▄[0;31m▒▓[0;90;41m▐[0;37m  [0;90m▌[0;31m░[0;37m [0;90;41m▐[0;90m▀[0;37m▀[0;37;41m▄[0;31m▓▒[0;90m█[0;37m      ▌ [0;31m▓[0;90;41m▐[0;37m     [0;90;41m▌[0;31m▓▒[0;90m▄▄▄[0;31m▒▓[0;90;41m▐[0;37m   [0;90m▌[0;31m░[0;37m [0;90m█[0;37m    [0;90m█[0;31m░▓░[0;90m█[0;37m   [0;90m▌[0;31m░[0;37m [0;90;41m▐[0;90m▀▀[0;37m     [0;90m▌[0;31m░[0;37m [0;90m█[0;37m [0;90m▐[0;31m░▒░[0;37m [0;31m░░[0;90m▌[0;37m    ▌ [0;31m▓[0;90;41m▐[0;37m     [0;31;47m▐[0;31m▒░[0;90m▌[0;37m   ▐[0;31m░▒[0;90;41m▐[0;37m [0m
[0;37m [0;90m▌[0;31m░[0;37m [0;90m▌[0;37m ▐ [0;31m░[0;90m▐[0;37m  [0;90m▐[0;37m  [0;90m█[0;37m        [0;90m▌[0;31m░[0;37m [0;90m▌[0;37m ▐ [0;31m░[0;90m▐[0;37m  [0;90m▌[0;37m  [0;90m█[0;37m   █[0;31m░[0;37m [0;90m█[0;37m     ▌ [0;31m▒[0;90m▐[0;37m     [0;90m▌[0;31m░[0;37m [0;90m▌[0;37m ▐ [0;31m░[0;90m▐[0;37m  [0;90m▐▌[0;37m  [0;90m▐▌[0;37m   [0;97m▐[0;37m▌[0;31m░[0;37m [0;90m▐▌[0;37m  [0;90m▌[0;37m  [0;90m▀▄▄▄▀█[0;37m [0;90m▐▌[0;37m  [0;90m▐▌[0;37m [0;90m▀▄[0;37m [0;31m░[0;37m [0;90m▐▌[0;37m    ▌ [0;31m▒[0;90m▐[0;37m     [0;90m▐[0;31m░░[0;90m▀▄▄▄[0;37m▀[0;31m░░[0;90m▌[0;37m [0m
[0;37m▐  [0;90m▐[0;37m   ▌  [0;90m▌[0;37m▄[0;90m█[0;37m  [0;90m▀▄[0;37m      ▐  [0;90m▐[0;37m   ▌  [0;90m▌▄▀[0;37m  [0;90m▀▄[0;37m ▄▀   [0;90m█[0;37m   ▐    [0;90m▌[0;37m   ▐  [0;90m▐[0;37m   ▌  [0;90m▌[0;37m [0;90m█[0;37m    [0;90m▀▄[0;37m  █    [0;90m█▄▀[0;37m        [0;90m▐[0;37m [0;90m█[0;37m    [0;90m▀▄[0;37m [0;90m▀▄[0;37m  [0;90m█[0;37m    ▐    [0;90m▌[0;37m     [0;90m▀▄[0;37m     [0;90m▄▀[0;37m  [0m
[0;37m▀[0;90m▀▀▀[0;37m   ▀[0;90m▀▀▀▀▀▀▀▀▀▀[0;37m     ▀[0;90m▀▀▀[0;37m   ▀[0;90m▀▀▀▀▀▀▀▀▀[0;37m  [0;90m▀▀▀▀[0;37m    ▀[0;90m▀▀▀▀[0;37m    ▀[0;90m▀▀▀[0;37m   ▀[0;90m▀▀▀[0;37m  [0;90m▀▀▀▀▀[0;37m    [0;90m▀▀▀▀[0;37m  [0;90m▀▀▀▀▀▀▀▀▀▀[0;37m  [0;90m▀▀▀▀▀[0;37m    [0;90m▀▀[0;37m     ▀[0;90m▀▀▀▀[0;37m        [0;90m▀▀▀▀▀[0;37m    [0m
[0;37m.                                                     [0;97m▄[0;37m▄▄▄[0;90m▄[0;37m        [0;97m▄[0;37m▄▄[0;90m▄▄▄▄▄[0;37m   [0;97m▄▄[0;37m▄▄▄[0;90m▄▄[0;37m [0m
[0;37m                                                      [0;97m▄[0;97;41m▀[0;91;41m░▒▒▒░[0;90;41m▀[0;90m▄[0;37m    [0;97m▄[0;97;41m▀[0;91;41m░▒▒▓▓▓█[0;90;41m▐[0;37m  [0;97m▀[0;97;41m▄[0;91;41m░▒▒▒▓[0;90m█▀[0m
[0;37m                                                     [0;97m▐[0;91;41m░░[0;90;41m▄[0;90m▀▀▀[0;90;41m▄[0;91;41m░░[0;90m▌[0;37m  [0;97m▐[0;91;41m░░[0;90;41m▄[0;90m▀▀▀▀▀▀▀[0;37m    [0;31;47m▐[0;91;41m░▒[0;90;41m▄[0;90m█[0;37m  [0m
[0;37m                                                     [0;97;41m▌[0;31m▓[0;31;41m [0;90m▌[0;37m   ▐[0;31;41m [0;31m▓[0;90;41m▐[0;37m  [0;97;41m▌[0;31m▓[0;31;41m [0;90m▌[0;97m▄[0;37m▄[0;90m▄▄[0;37m▄[0;90m▄▄▄[0;37m   [0;31;47m▐[0;31m▓[0;31;41m [0;90;41m▓[0;90m▌[0;37m  [0m
[0;37m                                                    ▐[0;31m▓▒[0;90;41m▐[0;37m     [0;37;41m▌[0;31m▒▓[0;90m▌▐[0;31m▓▒[0;90;41m▐[0;37m ▐[0;31m▓▒░▓▓█[0;90m█[0;37m   [0;90;41m▌[0;31m▒▓▓[0;90m▌[0;37m  [0m
[0;37m                                                     [0;31;47m▐[0;31m▒░[0;90m▌[0;37m   ▐[0;31m░▒[0;90;41m▐[0;37m  [0;31;47m▐[0;31m▒░[0;90m▌▐▀▀▓[0;31m░░▒▓[0;37m   [0;90m▌[0;31m░[0;37m [0;90;41m▐[0;90m▌[0;37m  [0m
[0;37m                                                     [0;90m▐[0;31m░░[0;90m▀▄▄▄[0;37m▀[0;31m░░[0;90m▌[0;37m  [0;90m▐[0;31m░░[0;90;41m▀[0;90m▄▄▄▒[0;31m░[0;37m [0;31m░[0;90;41m▐[0;37m   [0;90m▌[0;37m   [0;90m█[0;37m  [0m
[0;37m                                                      [0;90m▀▄[0;37m     [0;90m▄▀[0;37m    [0;90m▀[0;90;41m▄[0;31m░░[0;37m [0;90m▄▄[0;37m   [0;90m▐▌▄▀[0;37m  [0;90m░▓█▄[0;37m [0m
[0;37m                                                        [0;90m▀▀▀▀▀[0;37m        [0;90m▀▀▀▀[0;37m [0;90m▀▀▀▀[0;37m  [0;90m▀▀▀▀▀▀[0;37m  [0m

    {resetar}                                                                                                                                                                                      
    ''' 
    print(relat)
    nome = input("\nDigite o nome do funcionário: ").capitalize()#Nesta parte quando o usuario digitar o seu nome a primeira letra estara em maiusculo, devido a funcao .capitalize()
    if nome.replace(" ", "").isalpha():#No trecho abaixo esta sendo utilizado a funcao .isalpha() para validar se o usuario digitou apenas letras
        nome = nome
    else:
        print(f"{vermelho}Aviso: No nome não pode haver números{resetar}")
        input("\nPressione ENTER para digitar novamente")
        continue
    while True:#No trecho a seguir esta sendo feito as validacoes do cpf e rf onde o usuario pode somente digitar numeros, caso ao contrario ira perguntar novamente 
        try:
            cpf = int(input("\nEntre com o cpf do funcionário: "))
            cpfStr = str(cpf)

            cpfFormatado = f"{cpfStr[:3]}.{cpfStr[3:6]}.{cpfStr[6:9]}-{cpfStr[9:]}"
        except ValueError:
            print(f"{vermelho}Aviso: No CPF só é permitido números{resetar}")
            input("\nPressione ENTER para digitar novamente")
            continue
        else:
            break

    while True:
            try:
                rf=int (input("\nEntre com o número de registro do funcionário: "))
            except ValueError:
                print(f"{vermelho}Aviso: No Registro do Funcionário só é permitido números{resetar}")
                input("\nPressione ENTER para digitar novamente")
            else:
                break

        

    print("\n [ APARTAMENTO ]")#Aqui fica a tabela dos precos dos apartamentos
    headers = ["Quantidade de pessoas","Diaria tipo 1", "Diaria tipo 2"]
    data = [
    [1, f"R$ {verde}20{resetar} ",f"R$ {verde}25{resetar} "],
    [2, f"R$ {verde}28{resetar} ",f"R$ {verde}34{resetar} "],
    [3, f"R$ {verde}35{resetar} ",f"R$ {verde}42{resetar} "],
    [4, f"R$ {verde}42{resetar} ",f"R$ {verde}50{resetar} "],
    [5, f"R$ {verde}48{resetar} ",f"R$ {verde}57{resetar} "],
    [6, f"R$ {verde}53{resetar} ",f"R$ {verde}63{resetar} "]
    ]
    
    print(tabulate(data, headers=headers, numalign="center",tablefmt="rounded_grid"))#Neste parte esta sendo utilizado a biblioteca tabulate
    #No codigo abaixo esta sendo feito as validacoes do tipo de apartamentos,quantidade de pessoas e quantidade de dias
    while True:
        ap = input("\nQual tipo de diária de apartamento deseja escolher? (Digite 1 ou 2): ")
        if ap == "1" or ap =="2":
            break
        else:
            print(f"{vermelho}Aviso: Apartamento Inválido. A opção digitada não existe.{resetar}")
            input("\nPressione ENTER para digitar novamente")
    while True:
        try:
            qp = int(input("Digite quantas pessoas irao ficar (limite maximo de ate 6 pessoas): "))
            if qp >= 1 and qp <= 6:
                break
            if qp<1:
                print(f"{vermelho}Aviso: O valor digitado é menor do que 1{resetar}")
                input("\nPressione ENTER para digitar novamente")
            else:
                print(f"{vermelho}Aviso: O número de pessoas digitado é maior do que 6.{resetar}")
                input("\nPressione ENTER para digitar novamente")
        except ValueError:
            print(f"{vermelho}Apenas números são permitido{resetar}")
            input("\nPressione ENTER para digitar novamente")
    while True:
        try:
            qd = int(input("Digite quantos dias permanecerá (limite maximo de até 7 dias): "))
            if qd > 0 and qd <= 7:
                break
            if  qd < 1:
                print(f"{vermelho}Aviso: O valor digitado é menor do que 1{resetar}")
                input("\nPressione ENTER para digitar novamente")
            else:
                print(f"{vermelho}Aviso: O número de dias digitado é maior do que 6{resetar}")
                input("\nPressione ENTER para digitar novamente")
        except ValueError:
            print(f"{vermelho}Apenas números são permitido{resetar}")
            input("\nPressione ENTER para digitar novamente")

    if ap == "1":
        if qp == 1:
            diaria = 20
        elif qp == 2:
            diaria = 28
        elif qp == 3:
            diaria = 35
        elif qp == 4:
            diaria = 42
        elif qp == 5:
            diaria = 48
        elif qp == 6:
            diaria = 53

    elif ap == "2":
        if qp == 1:
            diaria = 25
        elif qp == 2:
            diaria = 34
        elif qp == 3:
            diaria = 42
        elif qp == 4:
            diaria = 50
        elif qp == 5:
            diaria = 57
        elif qp == 6:
            diaria = 63  


    valor = diaria * qd
    #Abaixo esta sendo utilizado a funcao .append() para adicionar dados dentro de uma lista 
    funcionario.append([
        nome,
        cpfFormatado,
        rf,
        ap,
        qp,
        qd,
        f"R$ {verde}{valor:,.2F}{resetar} "

    ])
    if funcionario:
        print("\n [ RESUMO DO CADASTRO ]")#Aqui mostra o resultado do cadastro
        cabecalho= ["Nome","CPF","RF","Apartamento","Pessoas","Dias","Valor"]
        print(tabulate(funcionario, headers=cabecalho, tablefmt="double_grid"))
    else:
        print("\nNenhum funcionário foi cadastrado.")

    opcao = input("\nDeseja continuar com outro cadastro ?(S/N): ")
    if opcao in ["S","s","Sim","SIM","sim"]:
        continue
    else:
        input(f"\nPressione ENTER para encerrar o programa")
        print(f"{verde}\nO programa foi encerrado...{resetar}")
        break
    

        

