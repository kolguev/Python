from os import path
import requests
from datetime import datetime
import pandas as pd
import openpyxl

DayOfMonth = datetime.now().day
Month = datetime.now().strftime("%B")
WeekNumber = (DayOfMonth - 1) // 7 + 1
SheetName = '{0} {1} неделя'.format(Month, WeekNumber)
FilePath = 'Tasks.xlsx'
ArchivingCards = ''
Data = [] # data from response

DoneListUrl = "https://api.trello.com/1/lists/60bf2b696d4e4a59dc1ae9d3/cards"
ArchiveListUrl = "https://api.trello.com/1/lists/60bf2b696d4e4a59dc1ae9d3/archiveAllCards"
Headers = {
   "Accept": "application/json"
}

Query = {
"key": "22801ceb02ae1296e7cc15e1c061bd1a",
"token": "2659532865da4041464a1e94cf0f76ef2d67ae8c19b861b1ab53f0652d21264a"
}

GetDoneList = requests.request(
   "GET",
   DoneListUrl,
   headers=Headers,
   params=Query
)

Result = GetDoneList.json()
#print(Result)
for i in Result:
    print(i.items())
    DateOfCard = datetime.fromisoformat(i['dateLastActivity'][:10]).date()
    if int(str(datetime.now().day)) - int(str(DateOfCard.day)) < 8:
        Data.append([i['name'], str(DateOfCard), i['desc'], i['dateLastActivity'], i['idMembers']])
       
DataFrame = pd.DataFrame(Data, columns = ['Name', 'Date', 'Desc', 'LastActivity', 'Members'])
print(DataFrame)