import pymysql, argparse, os, sys, json
from sqlalchemy import create_engine
import pandas as pd

from sqlalchemy import inspect

from passwords import db_connector

db_conn = db_connector
engine = create_engine(db_conn)
table_list: list[str] = []



inspector = inspect(engine)
for table_name in inspector.get_table_names():
    table_list.append(table_name)
print(table_list)

def pushToSql(df, basename):
    df.to_sql(basename, con=engine, if_exists="replace", index=False)
    table_list.append(basename)


