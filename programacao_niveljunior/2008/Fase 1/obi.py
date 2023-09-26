user_input = input('')
competidores = int(user_input.split(' ')[0])
nota_minima = int(user_input.split(' ')[1])
alunos_aprovados = 0
for a in range(competidores):
    result_aluno = input('')
    nota1 = int(result_aluno.split(' ')[0])
    nota2 = int(result_aluno.split(' ')[1])
    if nota1+nota2 >= nota_minima:
        alunos_aprovados+=1

print(alunos_aprovados)
    