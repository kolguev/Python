#import pytube

#url = 'https://www.youtube.com/watch?v=MvWt0O4Jweo'

#youtube = pytube.YouTube(url)
#video = youtube.streams.first()
#video.download('../Video')

#print(youtube.author.title())
import datetime

DayOfMonth = datetime.datetime.now().day
Month = datetime.datetime.now().strftime("%B")

print('{0} {1}-{2}'.format(Month, DayOfMonth - 7, DayOfMonth - 3))

