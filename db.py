import sqlite3

conn = sqlite3.connect('diet_app/test.db')
cur = conn.cursor()

def totalprice(limit):
    price = cur.execute(f'SELECT r.menu , SUM(price) FROM reicpe r  JOIN ingredient i ON r.ingred = i.name GROUP BY menu HAVING SUM(price) <= {price}')
    return price

def print_recipe():
    price = cur.execute('SELECT r.menu, r.ingred, r.num, i.unit, (r.num * i.unit_price) ingred_price FROM reicpe r JOIN ingredient i ON r.ingred = i.name ')
    return price
