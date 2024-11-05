from teacher_crud import TeacherCRUD
from database import Database

db = Database("neo4j+s://19fde513.databases.neo4j.io", "neo4j", "JzWaUr9940tSZaCMJsdWPsQ8HJmqpaHeFvdBmFUsAME")
crud = TeacherCRUD(db)

op = 0

while op != 5:
    print("=== MENU ===\n")
    print("1 - Criar professor")
    print("2 - Buscar professor")
    print("3 - Deletar um professor")
    print("4 - Atualizar o CPF de um professor")
    print("5 - Sair\n")
    print("=============\n")
    
    try:
        option = int(input("Selecione uma opção: "))
    
    except ValueError:
        print("Opção inválida, insira outra de acordo com o menu.\n")
        continue

    print()

    if op == 1:
        name = input("Nome: ")

        try:
            ano_nasc = int(input("Ano de nascimento: "))
        
        except ValueError:
            print("Ano de nascimento inválido.\n")
            continue

        cpf = input("CPF: ")
        crud.createTeacher(name, ano_nasc, cpf)

        print ("Professor criado com sucesso.\n")

    elif op == 2:
        name = input("Nome do professor a ser buscado: ")
        teacher = crud.readTeacher(name)

        print()

        if teacher:
            print("Professor encontrado.\n")
            print(f'Nome: {teacher[0]["t.name"]}.\nAno de nascimento: {teacher[0]["t.ano_nasc"]}.\nCPF: {teacher[0]["t.cpf"]}.')

        else:
            print("Professor não encontrado.\n")

        print()

    elif op == 3:
        name = input("Nome do professor a ser deletado: ")
        print()
        crud.deleteTeacher(name)
        print("Professor deletado com sucesso.\n")

        print()

    elif op == 4:
        name = input("Nome do professor cujo cpf será atualizado: ")
        new_cpf = input("Novo CPF: ")

        print()

        crud.updateTeacher(name, new_cpf)

        print("CPF atualizado com sucesso.\n")

    elif op == 5:
        db.close()
        print("Conexão encerrada.")

    else:
        print("Opção inválida, insira um valor válido.\n") 
        
    
    