def cadastrar_aluno(lista):
    from datetime import date, datetime
    aluno = {}
    while True:
        nome = input('Nome: ').strip().title()
        if not nome.replace(' ', '').isalpha():
            print('\033[0;31mError: digite apenas letras!\033[m')
            continue
        else:
            aluno['nome'] = nome
            break

    while True:
        data = input('Data de nascimento (DD/MM/YYYY): ')
        try:
            data_nasci = datetime.strptime(data, "%d/%m/%Y").date()
            data_atual = date.today()

            idade = data_atual.year - data_nasci.year
            aluno['idade'] = idade
            break
        except ValueError:
            print('\033[0;31mError: Data inválida. Tente novamente.\033[m')

    aluno['nota'] = []
    lista.append(aluno)
    print('\033[0;32mAluno cadastrado com sucesso!\033[m')

def dado_aluno(lista):
    import busca
    if not lista:
        print('Lista de alunos vazia.')
        return
    aluno = busca.buscar_aluno(lista)

    if aluno is None:
        return

    for chave, valor in aluno.items():
        if chave == 'nota':
            print('Notas:')
            for nota in valor:
                print(f' - {nota}')
        else:
            print(f'{chave}: {valor}')

