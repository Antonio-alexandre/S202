from database import Database
from bson.objectid import ObjectId
from models.Motorista import Motorista

class MotoristaDAO:
    def __init__(self, db: Database):
        self.db = db
        
    def create(self, motorista: Motorista):
        r = self.db.collection.insert_one(motorista.to_dict())
        return r

    def read(self, motorista_id):
        r = self.db.collection.find_one({"_id": motorista_id})
        return r
    
    def update(self, motorista_id, new_value):
        r = self.db.collection.update_one({"_id": motorista_id}, {"$set": new_value})
        return r
    
    def delete(self, motorista_id):
        r = self.db.collection.delete_one({"_id": motorista_id})
        return r
    