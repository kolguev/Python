import pyodbc
import pandas as pd
import matplotlib.pyplot as plt


conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOMEAPPSRV\SQLEXPRESS;DATABASE=hardware;UID=sa;PWD=HGFeiFTG_*')
cursor = conn.cursor()

#cursor.execute("SELECT CounterID,MachineName,ObjectName,CounterName,DefaultScale,InstanceName,CounterDateTime,CounterValue FROM hardware.dbo.View_hardware")
#row = cursor.fetchone()
#if row:
#    print(row)

df = pd.read_sql_query("SELECT MachineName,CounterName,InstanceName,CounterDateTime,CounterValue FROM hardware.dbo.View_hardware WHERE MachineName = '\\\\dbsrv' AND CounterName ='Средняя длина очереди диска' AND InstanceName = '2 F:'", conn)
#df = pd.read_sql_query("SELECT MachineName,CounterName,InstanceName,CounterDateTime,CounterValue FROM hardware.dbo.View_hardware WHERE MachineName = '\\\\BARIONSRVFILES2' AND CounterName ='% активности диска' AND InstanceName = '1 D:'", conn)

print(df['CounterDateTime'][1:20])
s = df['CounterDateTime'].astype('string')[0][2:19]
#s1 = s.astype('string')
print(s)
#df['CounterDateTime'] = s
#print(df)
#print(s)
#df.plot(x="CounterDateTime", y=["CounterValue",])
#plt.show()
