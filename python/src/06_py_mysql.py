import pymysql
from pymysql import Connection
from pymysql.cursors import Cursor

conn = pymysql.connect(
    host="sql8.freemysqlhosting.net",
    user="sql8720660",
    password="HiJgu6xgNR",
    db="sql8720660"
)
cur: Cursor = conn.cursor()
cur.execute("select * from employees;")
out: list= cur.fetchall()
for register in out:
    print(f" EmployeeNumber = {register[0]},"
          f"LastName={register[1]}"
          f"FirstName={register[2]}"
          f"Extensions= {register[3]}")
print(out)
conn.close()





