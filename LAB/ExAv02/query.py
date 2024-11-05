from database import Database
import random

db = Database("neo4j+s://19fde513.databases.neo4j.io", "neo4j", "JzWaUr9940tSZaCMJsdWPsQ8HJmqpaHeFvdBmFUsAME")

class QueryHandler:
    def __init__(self, db):
        self.db = db

    # 1 - a)
    def getTeacherRenzo(self):
        query = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc, t.cpf"
        return self.db.execute_query(query)

    # 1 - b)
    def getMNames(self):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf"
        return self.db.execute_query(query)

    # 1 - c)
    def getCities(self):
        query = "MATCH (c:City) RETURN c.name"
        return self.db.execute_query(query)

    # 1 - d)
    def getSchoolByNumber(self):
        query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number"
        return self.db.execute_query(query)

    # 2 - a)
    def getYoungestAndOldestTeacherBirthYear(self):
        query = "MATCH (t:Teacher) RETURN min(t.ano_nasc) AS youngest, max(t.ano_nasc) AS oldest"
        return self.db.execute_query(query)
    
    # 2 - b)
    def getCityPopulation(self):
        query = "MATCH (c:City) RETURN c.name, c.population"
        return self.db.execute_query(query)
    
    # 2 - c)
    def getModifyCityName(self):
        query = "MATCH (c:City) WHERE c.cep = '37540-000' RETURN replace(c.name, 'a', 'A')"
        return self.db.execute_query(query)
    
    # 2 - d)
    def getThirdChar(self):
        query = "MATCH (t:Teacher) RETURN t.name, substring(t.name, 3, 1)"
        return self.db.execute_query(query)


query_handler = QueryHandler(db)

print("1 - a)")
result = query_handler.getTeacherRenzo()
print(f'Ano de nascimento: {result[0]["t.ano_nasc"]}.\nCPF: {result[0]["t.cpf"]}.')

print("\nb)")
result = query_handler.getMNames()
for item in result:
    print(f'Nome: {item["t.name"]}.\nCPF: {item["t.cpf"]}.\n')

print("c)")
result = query_handler.getCities()
for item in result:
    print(f'Cidade: {item["c.name"]}.')

print("\nd)")
result = query_handler.getSchoolByNumber()
for item in result:
    print(f'Nome: {item["s.name"]}.\nEndereço: {item["s.address"]}.\nNúmero: {item["s.number"]}.\n')

print("2 - a)")
result = query_handler.getYoungestAndOldestTeacherBirthYear()
print(f'Ano de nascimento do professor mais jovem: {result[0]["youngest"]}')
print(f'Ano de nascimento do professor mais velho: {result[0]["oldest"]}')

print("b)")
result = query_handler.getCityPopulation()
for item in result:
    print(f'Cidade: {item["c.name"]}.\nPopulação: {item["c.population"]}.\n')

print("c)")
result = query_handler.getModifyCityName()
for item in result:
    print('Cidade: {}.'.format(item["replace(c.name, 'a', 'A')"]))

print("\nd)")
result = query_handler.getThirdChar()
for item in result:
    name = item["t.name"]
    if len(name) > 3:
        random_char = random.choice(name[3:])
        print(f'{name}: {random_char}.')