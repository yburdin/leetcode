import sqlite3


sql_connect = sqlite3.connect('sql/175.db')
cursor = sql_connect.cursor()

query = """
VACUUM;
CREATE TABLE IF NOT EXISTS Person (personId int, firstName varchar(255), lastName varchar(255));
CREATE TABLE IF NOT EXISTS Address (addressId int, personId int, city varchar(255), state varchar(255));
insert into Person (personId, lastName, firstName) values ('1', 'Wang', 'Allen');
insert into Person (personId, lastName, firstName) values ('2', 'Alice', 'Bob');
insert into Address (addressId, personId, city, state) values ('1', '2', 'New York City', 'New York');
insert into Address (addressId, personId, city, state) values ('2', '3', 'Leetcode', 'California');
"""
queries = [q for q in query.split('\n') if len(q) > 0]
for query in queries:
    results = cursor.execute(query).fetchall()

query = """
SELECT Person.firstName, Person.lastName, Address.city, Address.state
FROM Person 
LEFT JOIN Address 
ON Person.personId = Address.personId;
"""
query = query.replace('\n', ' ').strip()
results = cursor.execute(query).fetchall()

sql_connect.close()
