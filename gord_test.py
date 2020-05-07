# this is /gord_test.py
import datetime
import decimal
import urllib
import uuid

import numpy
import pandas as pd
import pyodbc
import sqlalchemy as sa
import sqlalchemy_access as sa_a

print(sa.__version__)

db_path = r"C:\Users\Public\test\sqlalchemy-access\gord_test.accdb"
db_path = r"C:\Users\Public\Database1.accdb"
connection_string = (
    'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_path};'
    'ExtendedAnsiSQL=1;'
)
connection_url = f"access+pyodbc:///?odbc_connect={urllib.parse.quote_plus(connection_string)}"

engine = sa.create_engine(connection_url, echo=True)
# engine_mssql = sa.create_engine("mssql+pyodbc://@sqlMyDb", echo=True)

# with engine.connect() as cnxn:
#     with cnxn.begin() as tran:
#         sql = sa.text("INSERT INTO foo_tbl (txt) VALUES (:p1)")
#         params = {"p1": "w00t"}
#         cnxn.execute(sql, params)
#         # tran.rollback()

# with engine.connect() as cnxn:
#     cnxn.execution_options(isolation_level="AUTOCOMMIT")
#     sql = sa.text("INSERT INTO foo_tbl (txt) VALUES (:p1)")
#     params = {"p1": "w00t"}
#     cnxn.execute(sql, params)



t = sa.Table("Donor", sa.MetaData(), autoload_with=engine)
with engine.connect() as conn:
    result = conn.execute(sa.select([t.c.DonorID]).order_by(t.c.DonorID).limit(1).offset(1)).fetchall()
    print(result)


# pyodbc_cnxn = engine.raw_connection()
# print(pyodbc_cnxn.getinfo(pyodbc.SQL_DRIVER_NAME))
# print(pyodbc_cnxn.getinfo(pyodbc.SQL_DRIVER_VER))

# metadata = sa.MetaData()
# parent = sa.Table('parent', metadata, autoload=True, autoload_with=engine)
# daughter = sa.Table('daughter', metadata, autoload=True, autoload_with=engine)
# son = sa.Table('son', metadata, autoload=True, autoload_with=engine)
# stmt = select([parent.c.parent_name, daughter.c.daughter_name, son.c.son_name])\
#     .select_from(parent
#                  .join(daughter, daughter.c.parent_id == parent.c.parent_id)
#                  .join(son, son.c.parent_id == parent.c.parent_id))\
#     .order_by(parent.c.parent_id)\
#     .limit(2)
# # stmt = select([parent.c.parent_name])\
# #     .select_from(parent)\
# #     .where(parent.c.parent_name.like('h%'))
# with engine.begin() as cnxn:
#     print(cnxn.execute(stmt).fetchall())


# df = pd.DataFrame(
#     [(1, 3.14),
#      (2, 6.28),
#     ], columns=['id', 'col1'],)
# # max_text_column_len = df.text_column.map(lambda x: len(x) if x else 0).max()
# dtype_dict = None
# # dtype_dict = {'text_column': sa.types.String(255)} if max_text_column_len <= 255 else None
# dtype_dict = {
#     'index': sa_a.AutoNumber,  # no effect :(
#     'col1': sa_a.Decimal(6, 5),
# }
#
# print(df)
# df.to_sql("my_table", engine, if_exists="replace", index=True, dtype=dtype_dict)


# df = pd.read_sql_query("SELECT * FROM compendium", engine)
# dtype_dict = {
#     'id': sa_a.AutoNumber,
#     'fldText': sa_a.ShortText(252),
#     'fldByte': sa_a.Byte,
#     'fldShort': sa_a.Integer,
#     'fldSingle': sa_a.Single,
#     'fldRepl': sa_a.ReplicationID,
#     'fldDecimal': sa_a.Decimal(19, 1),
#     'fldCurrency': sa_a.Currency,
#     'fldBlob': sa_a.OleObject,
#     'fldCHAR': sa_a.Char(129),
# }
# df.to_sql("zzz", engine, if_exists='replace', index=False, dtype=dtype_dict)


# with engine.begin() as cnxn:
#     result = cnxn.execute("SELECT * FROM compendium").fetchone()
# print(result)

# try:
#     with engine.begin() as cnxn:
#         cnxn.execute("DROP TABLE foo_tbl")
# except:
#     pass
# metadata = sa.MetaData()
# tbl = sa.Table("foo_tbl", metadata,
#                        sa.Column("id", sa_a.AutoNumber, primary_key=True),
#                        sa.Column("txt", sa_a.ShortText(50), index=True))
# metadata.create_all(engine)
