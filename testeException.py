while True:
    try:
        a = int(input('Numerador: '))
        b = int(input('Denominador: '))
        r = a / b 
    except (ValueError, TypeError):
        print('Tivemos um problema com os tipos de dados que você digitou. \nTente novamente: ')
    except ZeroDivisionError:
        print('Não é possível dividir um número por zero! \nTente novamente: ')
    except KeyboardInterrupt:
        print('O usuário preferiu não informar os dados.')
    except Exception as erro:
        print(f'O erro encontrado foi {erro.__cause__}. \nTente novamente: ')
    else:
        print(f'O resultado é {r}')
        break

print('Volte sempre!')
