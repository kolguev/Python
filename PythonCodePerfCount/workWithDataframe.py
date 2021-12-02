import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta, datetime, date, time
import mssqlconnect as sql

Message = []
Servers = ['\\\\DBSRV', '\\\\FILESRV', '\\\\APPSRV1', '\\\\APPSRV2']

ObjectName = ['Физический диск', 'Память', 'Система', 'Сетевой адаптер', 'Процессор']

CounterName = {'Физический диск': ['Среднее время записи на диск (с)', 'Среднее время чтения с диска (с)',
 '% активности диска при чтении', '% активности диска при записи',
 'Скорость записи на диск (байт/с)', 'Скорость чтения с диска (байт/с)',
 'Текущая длина очереди диска', 'Средняя длина очереди диска',
 '% активности диска'],
 'Память': ['Доступно МБ', 'Обмен страниц/с', 'Чтений страниц/с'],
 'Система': ['Длина очереди процессора', 'Контекстных переключений/с'],
 'Сетевой адаптер': ['Всего байт/с'],
 'Процессор': ['% загруженности процессора']}

InstanceName = {'Физический диск': ['0 D:', '1 E:', '2 F:', '3 G:', '4 C:'], 'Сетевой адаптер': ['Broadcom NetXtreme Gigabit Ethernet', 'Broadcom NetXtreme Gigabit Ethernet _2']}

#Data = pd.read_sql_query(sql.SqlQuery, sql.conn, params=[sql.Date])

Data = pd.read_csv('august-20-24.csv')

#Data[Data['MachineName'] == f"{Servers[3]}"][Data['CounterName'] == f"{CounterName['Процессор'][0]}"].plot(x="CounterDateTime", y="CounterValue")

#for Server in Servers:
#Data[Data['MachineName'] == f"{Servers[0]}"][Data['CounterName'] == f"{CounterName['Система'][0]}"].plot(x="CounterDateTime", y="CounterValue")
#plt.show( )

for Server in Servers:
    ValueCounter = Data[Data['MachineName'] == f"{Servers[0]}"][Data['CounterName'] == f"{CounterName['Система'][0]}"]['CounterValue'].max(axis=0)
    if ValueCounter > 20:
        Message.append(f'Очередь процессора на сервере {Server} превысила допустимую! {ValueCounter}')

#print(Message)

#print(Data[Data['MachineName'] == f"{Servers[0]}"][Data['CounterName'] == f"{CounterName['Сетевой адаптер'][0]}"][Data['InstanceName'] == f"{InstanceName['Сетевой адаптер'][1]}"]['CounterValue'].max(axis=0))
#df.plot(x="CounterDateTime", y="CounterValue")
#plt.savefig')