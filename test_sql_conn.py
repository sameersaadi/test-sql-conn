import pymssql
from getpass import getpass
host = input("Enter IP or DNS (without instance name): ")
instance = input("Enter Instance name (Hit Enter for None): ")
port = input("Enter Port (Hit Enter for 1433): ")
db = input("Enter database (Hit Enter for MASTER): ")
username = input("Enter username: ")
pwd = getpass()

if instance.strip() != "":
    host = host + '\\' + instance 

if port.strip() == "":
    port = 1433

if db.strip() == "":
    db = "master"
if host == "" or username == "" or pwd == "":
    print("Please fill in required values..")
else:
    try:
        print(">>> Connecting to Host", host, "on port", port, "...")
        conn = pymssql.connect(host=host, user=username, password=pwd, database=db, port=port)
        cursor = conn.cursor()
        print(">>> Running query/getting server name...")

        cursor.execute('SELECT @@servername')
        row = cursor.fetchone()
        print(row[0])
    except Exception as e:
        print(">>> SQL Connection Failed: ")
        print(e)
    else:
        print(">>> SUCCESS!!")
    