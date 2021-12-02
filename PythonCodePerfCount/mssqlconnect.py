import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta, datetime, date, time


conn = pyodbc.connect('DRIVER=SQL Server;SERVER=DBSRV\BARION;DATABASE=hardware;Trusted_Connection=yes;')
cursor = conn.cursor()
Date = str(datetime.now() - timedelta(minutes=15))[:-3]
#cursor.execute("SELECT CounterID,MachineName,ObjectName,CounterName,DefaultScale,InstanceName,CounterDateTime,CounterValue FROM hardware.dbo.View_hardware")
#row = cursor.fetchone()
#if row:
#    print(row)

#df = pd.read_sql_query("SELECT MachineName,CounterName,InstanceName,CounterDateTime,CounterValue FROM hardware.dbo.View_hardware WHERE MachineName = '\\\\filesrv' AND CounterName ='% активности диска' AND InstanceName = '2 F:'", conn)
SqlQuery = """SELECT
                          MachineName,
                          ObjectName,
                          CounterName,
                          InstanceName,
                          CounterDateTime,
                          CounterValue
                          FROM hardware.dbo.View_hardware 
                          WHERE 
                          CounterDateTime > ?
                          """
df = pd.read_sql_query(SqlQuery, conn, params=[Date])
#'2021-08-20 00:00:00.000'
df.to_csv('1.csv')

#dbSRV = df[df['MachineName'] == '\\DBSRV']
#print(dbSRV.head(10))
#for i in df['ObjectName'].unique():   
#    print(i, '\n', df[df['ObjectName']==i]['CounterName'].unique())

#df.plot(x="CounterDateTime", y="CounterValue")
#plt.savefig


