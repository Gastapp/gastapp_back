from pymongo import MongoClient

conn = MongoClient(host='127.0.0.1', port=27017)
conn = MongoClient()

db = conn.gastapp
collection = db.expenses

expenses = [
    {"id_user": "1", "amount": "450", "category": "food"},
    {"id_user": "1", "amount": "1500", "category": "clothes"},
    {"id_user": "2", "amount": "5200", "category": "home appliances"},
    {"id_user": "2", "amount": "300", "category": "food"},
    {"id_user": "2", "amount": "235", "category": "clothes"},
    {"id_user": "3", "amount": "1500", "category": "clothes"},

]

collection.insert_many(expenses)
