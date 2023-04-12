import sqlite3


sql_connect = sqlite3.connect('sql/577.db')
cursor = sql_connect.cursor()
query = """
VACUUM;
Create table If Not Exists Employee (empId int, name varchar(255), supervisor int, salary int)
Create table If Not Exists Bonus (empId int, bonus int)
insert into Employee (empId, name, supervisor, salary) values ('3', 'Brad', 'None', '4000')
insert into Employee (empId, name, supervisor, salary) values ('1', 'John', '3', '1000')
insert into Employee (empId, name, supervisor, salary) values ('2', 'Dan', '3', '2000')
insert into Employee (empId, name, supervisor, salary) values ('4', 'Thomas', '3', '4000')
insert into Bonus (empId, bonus) values ('2', '500')
insert into Bonus (empId, bonus) values ('4', '2000')
"""
queries = [q for q in query.split('\n') if len(q) > 0]
for query in queries:
    results = cursor.execute(query).fetchall()

query = """
SELECT name, bonus
FROM Employee
LEFT JOIN Bonus
ON Employee.empId = Bonus.empId
WHERE bonus < 1000 OR bonus is NULL
"""
query = query.replace('\n', ' ').strip()
results = cursor.execute(query).fetchall()

sql_connect.close()
