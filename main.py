alunoDict = dict()
alunosList = list()

def lin():
    print('-='*30)

def dados_aluno(nome, idade, nota):

    aluno = {
        'nome': nome,
        'idade': idade,
        'nota': nota,
    }

    alunosList.append(aluno)

def cadastrar_aluno():
    while True:
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        nota = float(input('Nota: '))

        dados_aluno(nome, idade, nota)

        qs = str(input('Deseja continuar? [S/N] '))

        if qs.upper() == 'N':
            print(alunosList)
            break
        else:
            lin()

def procurar_aluno(nome):
    for aluno in alunosList:
        if nome.lower() == aluno['nome'].lower():
            print(f'Aluno encontrado: {aluno}')
        if nome.lower() == aluno['nome'].lower():
            print(f'O aluno não foi encontrado!')

def remover_aluno(nome):
    for aluno in alunosList:
        if nome.lower() == aluno['nome'].lower():
            alunosList.remove(aluno)
            print(f'Aluno removido: {aluno}')
            print(alunosList)
            break

def media_geral():
    notaTotal = 0
    for aluno in alunosList:
        notaTotal += aluno['nota']
    mediaGeral = notaTotal / len(alunosList)
    print(mediaGeral)
    print(notaTotal)
        
cadastrar_aluno()
remover_aluno('Joana')
procurar_aluno('Henrique')
procurar_aluno('Santana')
media_geral()
