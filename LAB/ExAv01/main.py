from database import Database
from motoristaCLI import MotoristaCLI
from motoristaDAO import MotoristaDAO

if __name__ == "__main__":

    db = Database(database="ExAvaliativo", collection="Motoristas")

    motorista_dao = MotoristaDAO(db.collection)

    motorista_cli = MotoristaCLI(motorista_dao)

    motorista_cli.start()