import busca

def media_aluno(lista):
    if not lista:
        print('Lista de alunos vazia.')
        return

    aluno = busca.buscar_aluno(lista)

    if aluno is None:
        return
    
    notas = aluno['nota']
    media = sum(notas) / len(notas)
    print(f'Media do aluno {aluno["nome"]}')
    print(f'- {media:.2f} pts')


def aprovado_reprovado(lista):
    if not lista:
        print('Lista de alunos vazia.')
        return 

    aluno = busca.buscar_aluno(lista)

    if aluno is None:
        return

    notas = aluno['nota']
    media = sum(notas) / len(notas)
    if media > 7:
        print(f'Aluno {aluno['nome']} APROVADO com {media:.2f} pts')
    elif 5 <= media <= 6.9:
        print(f'Aluno {aluno['nome']} em RECUPERAÇÃO com {media:.2f} pts')
    else:
        print(f'Aluno {aluno['nome']} REPROVADO com {media:.2f} pts')