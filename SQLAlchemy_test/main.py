import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///chinook.db')

with engine.connect() as conn, conn.begin():
    data = pd.read_sql_query("SELECT FirstName || ' ' || LastName as full_name, email FROM customers", engine)
    print(data)


