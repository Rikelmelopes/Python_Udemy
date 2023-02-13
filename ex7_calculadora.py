#Minha logica

print(12*'=-')
print('>>>>> CALCULADORA <<<<<<')
print(12*'=-')
Primeiro = int(input('Digite o primeiro numero:  '))
Segundo = int(input('Digite o segundo numero:  '))
opção = 0
while opção != 6:
    print('''
[1]Adição
[2]Subtração
[3]Multiplicação
[4]Divisão
[5]Novos numeros
[6]Sair
    ''')
    opção = int(input('Sua opção?  '))

    if opção == 1:
        adição = Primeiro + Segundo
        print('{} + {} é igual á {}'.format(Primeiro , Segundo , adição))
    elif opção == 2:
        subtração = Primeiro - Segundo
        print('{} - {} é igual á {}'.format(Primeiro , Segundo , subtração))
    elif opção == 3:
        multiplicação = Primeiro * Segundo
        print('{} x {} é igual á {}'.format(Primeiro , Segundo , multiplicação))
    elif opção == 4:
        divisão = Primeiro / Segundo
        print('{} dividido por {} é igual á {}'.format(Primeiro , Segundo, divisão))
    elif opção == 5:
        print('Digite abaixo os novos numeros')
        Primeiro = int(input('Digite o primeiro numero:  '))
        Segundo = int(input('Digite o segundo numero:  '))
    elif opção == 6:
        print('Finalizando ......')
print('Fim do programa ... Volte sempre!!')