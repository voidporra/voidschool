import os

cursos_escolha=['ingles R$69', 'espanhol R$24', 'programação R$100', 'informática R$80', 'design gráfico R$90']
valor_cursos_escolha=[69, 24, 100, 80, 90]

def lista_cursos():
        print('\nNossa lista de cursos:')
        print('[1] - Inglês R$69')
        print('[2] - Espanhol R$24')
        print('[3] - programação (mas não é o programa que você ta pensando não) 100R$')
        print('[4] - Informática R$80')
        print('[5] - design gráfico R$90')

def listar():
    for file in os.listdir("."):
        if file.endswith(".txt"):
            lista_dos_alunos, _ = os.path.splitext(file)
            print(lista_dos_alunos)


def reset():
    os.system('cls')
    escolha=input('gostaria de fazer mais alguma coisa? y/n: ')
    if escolha=='y':
        matricula_de_alunos()
    elif escolha=='n':
        exit
    else:
        input('opção inválida\n pressione enter para continuar')
        reset()

def matricula_de_alunos():
    print('Matricula de alunos')
    print('~~~~~~~~~~~~~~~~~\n')
    print('1: Cadastrar aluno')
    print('2: Editar aluno')
    print('3: Listar alunos')
    print('4: Remover aluno')
    print('5: Lista de cursos')

    opcao=int(input('Qual opção você deseja? '))
    if opcao==1:
        os.system('cls')
        print('Cadastro de alunos')
        print('~~~~~~~~~~~~~~~~~\n')
        nome=input('Digite o nome do aluno: ')
        data=input('Digite a data de nascimento do aluno: ')
        cpf=input('Digite o cpf do aluno: ')
        nome_res=input('Digite o nome completo do responsável: ')
        data_res=input('Digite a data de nascimento do responsável: ')
        cpf_res=input('Digite o cpf do responsável: ')
        tele_res=input('Digite o telefone do responsável: ')
        lista_cursos()
        escolha_aluno=input('escolha quais cursos o aluno fará, separe por vírgulas: ')
        numeros_cursos = [int(numero.strip()) for numero in escolha_aluno.split(',')]
        cursos_escolhidos = [cursos_escolha[numero - 1] for numero in numeros_cursos]
        valor_cursos_escolha_escolhidos = [valor_cursos_escolha[numero - 1] for numero in numeros_cursos]
        cursos_formatados = ', '.join(cursos_escolhidos)
        soma_valores=sum(valor_cursos_escolha_escolhidos)
        nome_arquivo = nome + '.txt'
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write('nome: {}\n'.format(nome))
            arquivo.write('data de nascimento: {}\n'.format(data))
            arquivo.write('cpf: {}\n'.format(cpf))
            arquivo.write('nome do responsável: {}\n'.format(nome_res))
            arquivo.write('data de nascimento do responsável: {}\n'.format(data_res))
            arquivo.write('cpf do responsável: {}\n'.format(cpf_res))
            arquivo.write('telefone do responsável: {}\n'.format(tele_res))
            arquivo.write('cursos escolhidos: {}\n'.format(cursos_formatados))
            arquivo.write('valor total: R${}\n'.format(soma_valores))

            reset()
    elif opcao==2:
        os.system('cls')
        nome_edit=input('qual aluno você gostaria de editar? ')
        new_nome=input('Digite o novo nome do aluno: ')
        new_data=input('Digite a nova data de nascimento do aluno: ')
        new_cpf=input('Digite o novo cpf do aluno: ')
        new_nome_res=input('Digite o novo nome do responsável: ')
        new_data_res=input('Digite a nova data de nascimento do responsável: ')
        new_cpf_res=input('Digite o novo cpf do responsável: ')
        new_tele_res=input('Digite o novo telefone do responsável: ')
        lista_cursos()
        new_escolha_aluno=input('escolha quais cursos o aluno fará, separe por vírgulas: ')
        new_numeros_cursos = [int(numero.strip()) for numero in new_escolha_aluno.split(',')]
        new_cursos_escolhidos = [cursos_escolha[numero - 1] for numero in new_numeros_cursos]
        new_valor_cursos_escolha_escolhidos = [valor_cursos_escolha[numero - 1] for numero in new_numeros_cursos]
        new_cursos_formatados = ', '.join(new_cursos_escolhidos)
        new_soma_valores=sum(new_valor_cursos_escolha_escolhidos)
        nome_arquivo = new_nome + '.txt'
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write('nome: {}\n'.format(new_nome))
            arquivo.write('data de nascimento: {}\n'.format(new_data))
            arquivo.write('cpf: {}\n'.format(new_cpf))
            arquivo.write('nome do responsável: {}\n'.format(new_nome_res))
            arquivo.write('data de nascimento do responsável: {}\n'.format(new_data_res))
            arquivo.write('cpf do responsável: {}\n'.format(new_cpf_res))
            arquivo.write('telefone do responsável: {}\n'.format(new_tele_res))
            arquivo.write('cursos escolhidos: {}\n'.format(new_cursos_formatados))
            arquivo.write('valor total: R${}\n'.format(new_soma_valores))
        nome_edit_remove=nome_edit+'.txt'
        os.remove(nome_edit_remove)
        input('aluno alterado com sucesso, pressione enter para continuar')
        reset()

    elif opcao==3:
        listar()
        input('pressione enter para voltar à tela inicial')
        reset()

    elif opcao==4:
        os.system('cls')
        nome_remocao=input('Qual aluno você deseja remover? \n')
        nome_remove=nome_remocao+'.txt'
        try: os.remove(nome_remove)
        except FileNotFoundError:
            input('aluno não encontrado, pressione enter para continuar')
            reset()
            print
        os.system('cls')
        input('Aluno ',nome_remocao,' foi removido com sucesso, pressione enter para continuar')
        reset()
    elif opcao==5:
        os.system('cls')
        lista_cursos()
        input('pressione enter para continuar ')
        reset()               
    else:
        input('opção inválida, pressione enter para continuar')
        os.system('cls')
        matricula_de_alunos()
matricula_de_alunos()