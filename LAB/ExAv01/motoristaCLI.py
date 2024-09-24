from typing import Any
from models.Corrida import Corrida
from models.Motorista import Motorista
from models.Passageiro import Passageiro
from motoristaDAO import MotoristaDAO

class MotoristaCLI:
    def __init__(self, dao: MotoristaDAO):
        self.dao = dao
    
    def menu(self):
        option = input ("Escolha uma opção:\n1 - Cadastrar motorista\n2 - Listar motoristas\n3 - Cadastrar corrida\n4 - Listar corridas")

        if option == "1":
            self.create()
        elif option == "2":
            self.read()
        elif option == "3":
            self.update()
        elif option == "4":
            self.delete()
        else:
            print("Opção inválida")
            self.menu()
        
    def create(self):
        print ("Cadastre o motorista:")
        nome = input("Nome: ")
        documento = input("Documento: ")
        passageiro = Passageiro(nome, documento)
        aux = 1
        corridas = []
        while aux == 1:
            print("Cadastre a corrida:")
            nota = input("Nota: ")
            distancia = input("Distância: ")
            valor = input("Valor: ")
            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.append(corrida)
            aux = int(input("Deseja cadastrar outra corrida? 1 - Sim, 0 - Não"))
        nota = input("Nota do motorista: ")
        motorista = Motorista(nota, corridas)
        self.dao.create(motorista)

    def read(self):
        id = input("Digite o ID do motorista a ser pesquisado: ")
        motorista = self.dao.read(id)
        if motorista:
            print(motorista)
        else:
            print("Motorista não encontrado")

    def update(self):
        id = input("Digite o ID do motorista a ser atualizado: ")
        motorista = self.dao.read(id)
        if motorista:
            nota = input("Digite a nova nota do motorista: ")
            motorista["nota"] = nota
            self.dao.update(id, motorista)

    def delete(self):
        id = input("Digite o ID do motorista a ser deletado: ")
        motorista = self.dao.read(id)
        if motorista:
            self.dao.delete(id)

    def start(self):
        while True:
            self.menu()
            aux = input("Deseja continuar? 1 - Sim, 0 - Não")
            if aux == 0:
                break
            else:
                continue