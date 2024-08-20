class Professor:
    def __init__(self, nome):
        self.nome = nome

class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Aula:
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

    def addaluno(self, aluno):
        self.alunos.append(aluno)

prof1 = Professor("Carlos Ynoguti")
prof2 = Professor("Daniela Barude")
prof3 = Professor("Carlos Francisco")

alunos_01 = [Aluno("José"), Aluno("João"), Aluno("Henrique"), Aluno("André")]
alunos_02 = [Aluno("Marcos"), Aluno("Lucas"), Aluno("Felipe"), Aluno("Paulo")]
alunos_03 = [Aluno("Bruno"), Aluno("Miguel"), Aluno("Luana"), Aluno("Clara")]

aula1 = Aula(prof1, "Algoritmos")
for aluno in alunos_01:
    aula1.addaluno(aluno)

aula2 = Aula(prof2, "Física")
for aluno in alunos_02:
    aula2.addaluno(aluno)

aula3 = Aula(prof3, "Circuitos")
for aluno in alunos_03:
    aula3.addaluno(aluno)

collection_aulas = {
    "aulas": [
        {
            "professor": {"nome": aula1.professor.nome},
            "assunto": aula1.assunto,
            "alunos": [{"nome": aluno.nome} for aluno in aula1.alunos]
        },
        {
            "professor": {"nome": aula2.professor.nome},
            "assunto": aula2.assunto,
            "alunos": [{"nome": aluno.nome} for aluno in aula2.alunos]
        },
        {
            "professor": {"nome": aula3.professor.nome},
            "assunto": aula3.assunto,
            "alunos": [{"nome": aluno.nome} for aluno in aula3.alunos]
        }
    ]
}