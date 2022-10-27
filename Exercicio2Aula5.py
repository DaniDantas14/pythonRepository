def CalculaMedia(nota1, nota2, nota3, nota4):
    Media = 0
    Media = (nota1+nota2+nota3+nota4)/4
    return Media
 
listaAluno = []
listaMediaAlunos = []
listaNotasAlunos = []
qtdAlunosComMesmaMedia = 0
nomeAluno = ""
Nota1 = 0
Nota2 = 0
Nota3 = 0
Nota4 = 0
nomeAluno = input("Entrar com o nome do Aluno: ")
 
while nomeAluno:
    listaAluno.append(nomeAluno)
    listaNotasAlunos.append(float(input(f"Entrar com a 1ª Nota do Aluno {nomeAluno} : ")))
    listaNotasAlunos.append(float(input(f"Entrar com a 2ª Nota do Aluno {nomeAluno} : ")))
    listaNotasAlunos.append(float(input(f"Entrar com a 3ª Nota do Aluno {nomeAluno} : ")))
    listaNotasAlunos.append(float(input(f"Entrar com a 4ª Nota do Aluno {nomeAluno} : ")))
    resp = input("Deseja entrar com um novo Aluno (s/n): ")
    if resp in ("s","S"):
        nomeAluno = input("Entrar com o nome do Aluno: ")
    else:
        break
print("\n")
for i in range(len(listaAluno)):
    Media = CalculaMedia(listaNotasAlunos[i*4],listaNotasAlunos[i*4+1],listaNotasAlunos[i*4+2],listaNotasAlunos[i*4+3],)
    
    if Media in listaMediaAlunos:
        qtdAlunosComMesmaMedia += 1
    else:
        listaMediaAlunos.append(Media)

    if Media >= 7:
        print(f"Aluno(a) {listaAluno[i]} foi aprovado com Média {Media}")
    else:
        print(f"Aluno(a) {listaAluno[i]} foi reprovado com Média {Media}")

print(f"\nLista original dos Alunos \n {listaAluno}")
listaAluno.sort()
print(f"Lista ordenada dos Alunos \n {listaAluno}")

if qtdAlunosComMesmaMedia == 0:
    print("\nNão tivemos alunos com Médias iguais")
else:
    print(f"\nTivemos {qtdAlunosComMesmaMedia} aluno(s) com Média(s) igual(is)")
