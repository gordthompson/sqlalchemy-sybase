import os
import pyodbc

cnxn = pyodbc.connect(
    f"DSN=sybase_test_dsn;UID=sa;PWD={os.environ['sa_PWD']}", autocommit=True
)
crsr = cnxn.cursor()

# original approach
#
# tables = crsr.tables(tableType="TABLE").fetchall()
# for table_name in [x[2] for x in tables]:
#     print(table_name)
#     crsr.execute(f"DROP TABLE [{table_name}]")

# plan B: after a few runs the tests would start to hang,
#         usually on test_autoincrement_col
#
db_name = "[sqla_test]"
print(f"Re-creating database {db_name}")
crsr.execute("USE master")
crsr.execute(f"DROP DATABASE {db_name}")
crsr.execute(f"CREATE DATABASE {db_name}")
