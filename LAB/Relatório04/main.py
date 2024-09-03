from database import Database
from productAnalyzer import ProductAnalyzer
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="compras")
db.resetDatabase()

analyzer = ProductAnalyzer(db)

analyzer.totalSales()
analyzer.mostSoldProduct()
analyzer.highestPurchase()
analyzer.productsSoldMoreThanOnce()