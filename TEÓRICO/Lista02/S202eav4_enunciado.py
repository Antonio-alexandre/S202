   ###                           ##              ####
  ####                          ###              ####
  ###  ##########   ######## ########  #######   ####
 ####  ##### ####  ####  ####  ###   ####  #### #### 
 ####  ###   ####   ########  ####  ########### #### 
####  ####   #### ####  ####  ####  ####        ###  
####  ###    ### ########### ###### ########## ####                 S202 - Banco de dados II
#### ####   ####  ##########  ####   ######    ###       Prof. Dr. Jonas Lopes de Vilas Boas

# Exercício Avaliativo 4 - Banco de dados orientado à colunas e Cassandra

"""
Estoque da Montadora 

Um fabricante de automóveis contratou você para desenvolver um sistema de banco de dados distribuído usando o Cassandra para as linhas de montagem de toda a corporação, onde cada máquina pudesse acessar a base de dados e buscar as peças de maneira correta para ser montada nos respectivos modelos de veículos. Para isso, você deverá criar a tabela estoque no sistema DataStax ASTRA e inserir as colunas usando o arquivo auxiliar disponibilizado junto com essa atividade. 

Questão 1: Siga os itens listados abaixo: 

Faça a inserção de uma nova peça com os dados abaixo: 

id: 5 
nome: Pistao 
carro: Mustang 
estante: 4 
nível: 1 
quantidade: 167 

Faça a inserção de uma nova peça com os dados abaixo: 

id: 4
nome: Suspencao 
carro: Argo 
estante: 1 
nível: 1 
quantidade: 3500 

Questão 2: Escreva o comando CQL utilizado para cada item abaixo: 

Faça uma busca no banco de dados que retorno todos os dados do item com nome 'Pistão';
Faça uma busca no banco que calcule a média aritmética da quantidade de todas as colunas armazenadas na tabela;
Faça uma busca que retorne quantas colunas tem armazenadas na tabela;
Busque a maior e a menor quantidade de peças usando as alias "maior quantidade" e "menor quantidade" para a tabela estoque. 
Faça uma busca que retorne os atributos nome, carro e quantidade, onde a estante seja igual a 3;
Faça uma busca que retorne a média aritmética da quantidade onde o nível seja igual a 1; 
Faça uma busca retornando todos os atributos onde a estante seja menor do que 3 e o nível seja maior do que 4.
 

Questão 3: Elabore um script Python que seja capaz de fazer uma consulta mostrando nome, estante e quantidade do carro fornecido pelo usuário. 

"""

import json

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory 

class CassandraConnector:
	
	def get_cassandra_connector(self):
		if(self.cassandra_session == None):
			# This secure connect bundle is autogenerated when you download your SCB, 
			# if yours is different update the file name below
			cloud_config= {
				"secure_connect_bundle": "secure-connect-estoque.zip"
			}

			# This token JSON file is autogenerated when you download your token, 
			# if yours is different update the file name below
			with open("estoque-token.json") as f:
				secrets = json.load(f)

			CLIENT_ID = secrets["clientId"]
			CLIENT_SECRET = secrets["secret"]

			auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
			cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
			cassandra_session = cluster.connect()
			cassandra_session.row_factory = dict_factory

			# Use your keyspace name
			self.cassandra_session.set_keyspace("ksestoque")
		return self.cassandra_session
    
class AutoPart:
    def __init__(self, name, car, shelf, level, amount):
      self.name = name
      self.car = car
      self.shelf = shelf
      self.level = level
      self.amount = amount

    def to_dict(self):
      return {
          "name": self.name,
          "car": self.car,
          "shelf": self.shelf,
          "level": self.level,
          "amount": self.amount
	}


class AutoPartDAO:
    def __init__(self):
        self.cassandra_session = CassandraConnector.get_cassandra_connector()

    def create_table(self):
        pass
    
    def add_part(self):
        pass
    
    def get_part(self, name):
        pass

    def get_average_amount(self):
        pass

    def get_total_amount(self):
        pass

    def get_max_min(self):
        pass

    def get_parts_from_shelf(self, shelf):
        pass

    def get_average_amount_from_level(shelf, level):
        pass

    def get_parts_from_shelf_and_level(self, shelf, level):
        pass

    def get_parts_of_car(self, car): # Questão 3 (Puxa as informações de um carro)
        query = """
        SELECT nome, estante, quantidade FROM estoque WHERE carro = %s ALLOW FILTERING;
        """
        rows = self.cassandra_session.execute(query, (car,))
        return [row for row in rows]
    
    def consulta_estoque(self): # Questão 3 (Função que executa a consulta com o carro fornecido pelo usuário)
        car = input("Digite o nome do carro: ")
        dao = AutoPartDAO()
        parts = dao.get_parts_of_car(car)
        if parts:
            for part in parts:
                print(f"Nome: {part['nome']}, Estante: {part['estante']}, Quantidade: {part['quantidade']}")
        else:
            print("Nenhuma peça encontrada para o carro fornecido.")

    consulta_estoque() # Executa o código da questão 3