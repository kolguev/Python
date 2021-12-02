import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta, datetime, date, time


conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEAPPSRV\SQLEXPRESS;DATABASE=hardware;UID=sa;PWD=HGFeiFTG_*')
cursor = conn.cursor()

#cursor.execute("SELECT CounterID,MachineName,ObjectName,CounterName,DefaultScale,InstanceName,CounterDateTime,CounterValue FROM hardware.dbo.View_hardware")
#row = cursor.fetchone()
#if row:
#    print(row)

#df = pd.read_sql_query("SELECT MachineName,CounterName,InstanceName,CounterDateTime,CounterValue FROM hardware.dbo.View_hardware WHERE MachineName = '\\\\filesrv' AND CounterName ='% активности диска' AND InstanceName = '2 F:'", conn)
df = pd.read_sql_query("SELECT MachineName,CounterName,InstanceName,CounterDateTime,CounterValue FROM hardware.dbo.View_hardware WHERE MachineName = '\\\\BARIONSRVFILES3' AND CounterName ='% активности диска' AND InstanceName = '0 C:'", conn)

print(df)

df.plot(x="CounterDateTime", y=["CounterValue",])
plt.show()


#-----

def connection():
    sql = """
                    DRIVER={SQL Server};
                    SERVER=DBSRV\BARION;
                    DATABASE=hardware;
                    UID=user;
                    PWD=password;
                    trusted_connection='no'
      """ 
    return sql

c_my_db =  pyodbc.connect(connection())
c_my_db.autocommit = True
cursor = c_my_db.cursor()

#time
print('Начато выполнение ', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

query = """
				SELECT [CounterID]
					  ,[MachineName]
					  ,[ObjectName]
					  ,[CounterName]
					  ,[CounterDateTime]
					  ,[CounterValue]
				FROM [hardware].[dbo].[View_hardware]
				WHERE [CounterDateTime] > '2021-07-25 00:00:00.000'
				ORDER BY 5
        """
df = pd.read_sql(query, c_my_db)
df.head(3)

for i in df['ObjectName'].unique():   
    print(i, '\n', df[df['ObjectName']==i]['CounterName'].unique())
