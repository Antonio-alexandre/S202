from database import Database
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="compras")


class ProductAnalyzer:

    def __init__(self, database: Database):
        self.db = database
    
    def totalSales(self):
        result = self.db.collection.aggregate([
            {"$group": {"_id": "$data_compra", "total": {"$count": {}}}}
        ])
        writeAJson(result, "total_sales")

    def mostSoldProduct(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
        writeAJson(result, "most_sold_product")

    def highestPurchase(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"}, 
            {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}, 
            {"$sort": {"total": -1}}, 
            {"$limit": 1}
        ])
        writeAJson(result, "highest_purchase")

    def productsSoldMoreThanOnce(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"}, 
            {"$group": {"_id": "$produtos.descricao", "total": {"$count": {}}}}
        ])
        writeAJson(result, "products_sold_more_than_once")