import sqlite3


sql_connect = sqlite3.connect('sql/176.db')
cursor = sql_connect.cursor()

query = """
VACUUM;
Create table If Not Exists Employee (id int, salary int);
insert into Employee (id, salary) values ('1', '100');
insert into Employee (id, salary) values ('2', '200');
insert into Employee (id, salary) values ('3', '300');
"""
queries = [q for q in query.split('\n') if len(q) > 0]
for query in queries:
    results = cursor.execute(query).fetchall()

query = """
SELECT (
SELECT DISTINCT Salary 
FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1
) AS SecondHighestSalary
"""
query = query.replace('\n', ' ').strip()
results = cursor.execute(query).fetchall()

sql_connect.close()
