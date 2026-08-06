import busca
def lancar_nota(lista):
    notas = []
    if not lista:
        print('Lista de alunos vazia...')
        return

    aluno = busca.buscar_aluno(lista)

    if aluno is None:
        return
    try:
        while True:
            quant = int(input('Quantas notas serão lançadas? '))
            if quant <= 0:
                print('\033[0;31mError: Adicione um valor maior que "0".\033[m')
                continue
            else:
                break
        for i in range(quant):
            notas.append(float(input(f'{i+1}º nota: ')))
        
        aluno['nota'] = notas
        if quant == 1:
            print('\033[0;32mNota adicionada com sucesso!\033[m')
        else:
            print('\033[0;32mNotas adicionadas com sucesso!\033[m')
    except ValueError:
        print('\033[0;31mError: Digite um valor válido!\033[m')

def ranking(lista):
    if not lista:
        print('Lista de alunos vazia.')
        return

    ranking = sorted(lista, key=lambda 
        aluno: sum(aluno['nota']) / len(aluno['nota'])
        if aluno['nota'] else 0,
        reverse=True)
    for posicao, aluno in enumerate(ranking, start=1):
        if aluno['nota']:
            media = sum(aluno['nota']) / len(aluno['nota'])
        else:
            media = 0

        print(f'{posicao}º lugar: {aluno["nome"]} - média: {media:.2f}')






    