import pyodbc
#
cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};server=XXX\SQLEXPRESS;database=testepython;trusted_connection=Yes;')
cursor = cnxn.cursor()