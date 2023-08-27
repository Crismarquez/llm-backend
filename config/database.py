import os
from urllib.parse import quote_plus
from sqlalchemy.engine import URL, create_engine

from config.config import ENV_VARIABLES


# db conexion
driver = os.environ.get("DRIVER")
server = os.environ.get("SERVER")
database = os.environ.get("DATABASE")
username = os.environ.get("USERNAMEDB")
password = os.environ.get("PASSWORDDB")

print(server)

connection_url = URL.create(
    drivername="mssql+pyodbc",
    username=username,
    password=password,
    host=server,
    port=1433,
    database=database,
    query={
        "driver": "ODBC Driver 18 for SQL Server",
        "TrustServerCertificate": "no"
        },
    )
# engine = create_engine(connection_url)
engine = ""
# conn = f"""DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"""
# quoted = quote_plus(conn)
# uri = "mssql+pyodbc:///?odbc_connect={}".format(quoted)

