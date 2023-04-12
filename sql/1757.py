import sqlite3


sql_connect = sqlite3.connect('sql/1757.db')
cursor = sql_connect.cursor()

query = """
VACUUM;
Create table If Not Exists Products ( product_id int, low_fats TEXT CHECK( low_fats IN ('Y','N') ), recyclable TEXT CHECK( recyclable IN ('Y','N') ));
insert into Products (product_id, low_fats, recyclable) values ('0', 'Y', 'N');
insert into Products (product_id, low_fats, recyclable) values ('1', 'Y', 'Y');
insert into Products (product_id, low_fats, recyclable) values ('2', 'N', 'Y');
insert into Products (product_id, low_fats, recyclable) values ('3', 'Y', 'Y');
insert into Products (product_id, low_fats, recyclable) values ('4', 'N', 'N');
"""
queries = [q for q in query.split('\n') if len(q) > 0]
for query in queries:
    results = cursor.execute(query).fetchall()

query = """
SELECT product_id 
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y'
"""
query = query.replace('\n', ' ').strip()
results = cursor.execute(query).fetchall()

sql_connect.close()
