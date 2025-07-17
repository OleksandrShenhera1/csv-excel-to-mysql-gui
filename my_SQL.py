import pymysql, argparse, os, sys, json
from sqlalchemy import create_engine
import pandas as pd

from sqlalchemy import inspect
from sqlalchemy import text

from passwords import db_connector

max_length = 64
db_conn = db_connector
engine = create_engine(db_conn)

table_dict = {}
dfs = {}

def readDf(df_name):
    df = pd.read_sql_table(df_name, engine)
    dfs[df_name] = df
    return df

inspector = inspect(engine)
def tables() -> tuple[dict, dict]:
    for table_name in inspector.get_table_names():
        col = inspector.get_columns(table_name)
        with engine.connect() as conn:
            result = conn.execute(text(f"SELECT COUNT(*) FROM `{table_name}`"))
            row = result.scalar()
        table_dict[table_name] = [row, len(col)]
        dfs[table_name] = readDf(table_name)
    return table_dict, dfs

table_dict, dfs = tables()

print(table_dict)


def pushToSql(df, basename) -> dict:
    if len(basename) >= max_length:
        basename = basename[:max_length]
    df.to_sql(basename, con=engine, if_exists="replace", index=False)
    inspector_new = inspect(engine)
    col = inspector_new.get_columns(basename)
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT COUNT(*) FROM `{basename}`"))
        row = result.scalar()
    table_dict[basename] = [len(col), row]
    return {basename: [row, len(col)]}

