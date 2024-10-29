from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

uri = "neo4j+s://31e5ab0b.databases.neo4j.io"  
user = "neo4j"  
password = "FBYJ47SklnwCeJadAR6B2YHFhzzP9WoRzcSoayG6aR8" 

driver = GraphDatabase.driver(uri, auth=(user, password))

def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return [record for record in result]

query1 = """
MATCH (p:Pessoa:Engenheiro)
RETURN p.nome AS Nome
"""

query2 = """
MATCH (p1:Pessoa {nome: "João"})-[:PAI_DE]->(p2:Pessoa)
RETURN p2.nome AS Filho
"""

query3 = """
MATCH (p1:Pessoa {nome: "Clara"})-[r:NAMORA_COM]->(p2:Pessoa)
RETURN p2.nome AS Namorado, r.Desde AS Desde
"""

print("Quem da família é Engenheiro?")
result1 = run_query(query1)
for record in result1:
    print(record['Nome'])

print("\nJoão é pai de quem?")
result2 = run_query(query2)
for record in result2:
    print(record['Filho'])

print("\nClara namora com quem desde quando?")
result3 = run_query(query3)
for record in result3:
    print(f"{record['Namorado']} desde {record['Desde']}")

driver.close()


#CREATE (p1:Pessoa:Engenheiro {nome: "João", sexo: "M", idade: 50})
#CREATE (p2:Pessoa:Médico {nome: "Maria", sexo: "F", idade: 48})
#CREATE (p3:Pessoa:Advogado {nome: "Pedro", sexo: "M", idade: 25})
#CREATE (p4:Pessoa:Estudante {nome: "Ana", sexo: "F", idade: 22})
#CREATE (p5:Pessoa:Estudante {nome: "Carlos", sexo: "M", idade: 18})
#CREATE (p6:Pessoa:Designer {nome: "Clara", sexo: "F", idade: 20})
#CREATE (p7:Pessoa:Professor {nome: "José", sexo: "M", idade: 70})
#CREATE (p8:Pessoa:Enfermeiro {nome: "Lúcia", sexo: "F", idade: 68})
#CREATE (p9:Pet:Cachorro {nome: "Rex", sexo: "M", idade: 3})
#CREATE (p10:Pet:Gato {nome: "Mimi", sexo: "F", idade: 2})

#match (e:Engenheiro),(m:Médico),(a:Advogado)
#CREATE (e)-[:PAI_DE]->(m),(e)-[:PAI_DE]->(a),(m)-[:FILHO_DE]->(e),(a)-[:FILHO_DE]->(e)

#match (a:Advogado),(d:Designer)
#CREATE (d)-[:NAMORA_COM{Desde:'2020'}]->(a),(a)-[:NAMORA_COM{Desde:'2020'}]->(d)

#match (e:Engenheiro),(c:Cachorro),(m:Médico),(g:Gato)
#CREATE (e)-[:DONO_DE]->(c),(m)-[:DONO_DE]->(g)