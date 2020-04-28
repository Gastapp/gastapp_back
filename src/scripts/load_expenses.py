from pymongo import MongoClient


conn = MongoClient(host='127.0.0.1', port=27017)
conn = MongoClient()

db = conn.gastapp
collection = db.expenses

expenses = [
    {"id_user": "1", "amount": 450, "category": "food", "date": "17/04/2020"},
    {"id_user": "1", "amount": 235, "category": "clothes", "date": "10/03/2020"},
    {"id_user": "2", "amount": 900, "category": "clothes", "date": "20/04/2020"},
    {"id_user": "2", "amount": 5200, "category": "home appliances", "date": "19/04/2020"},
    {"id_user": "2", "amount": 350, "category": "food", "date": "19/04/2020"},
    {"id_user": "2", "amount": 420, "category": "food", "date": "18/04/2020"},
    {"id_user": "2", "amount": 7999, "category": "home appliances", "date": "17/04/2020"},
    {"id_user": "2", "amount": 1400, "category": "clothes", "date": "17/04/2020"},
    {"id_user": "2", "amount": 599, "category": "clothes", "date": "17/04/2020"},
    {"id_user": "3", "amount": 1000, "category": "clothes", "date": "14/04/2020"},
]

collection.insert_many(expenses)
