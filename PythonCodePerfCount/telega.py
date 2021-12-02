from datetime import timedelta, datetime, date, time
import requests
import workWithDataframe

def send_telegram(text: str):
    url = "https://api.telegram.org/bot"
    token = "873647994:AAFyT6A-3gh26JIlqS_fbU-Nmk0in5Rapf0"
    channel_id = "-1001529682908"
    method = url + token + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")
    return r

if __name__ == '__main__':
    now = str(datetime.now())[:20]
    r = send_telegram(f"{now} {workWithDataframe.Message}")

print('over')