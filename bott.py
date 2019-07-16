import requests
import re
from date_mom import get_date_mom
from mom import get_money
from time import sleep
from bs4 import BeautifulSoup
from anecdot import word


global last_upd
last_upd = 0

URL = 'https://api.telegram.org/bot871175772:AAHt36UUKeyyMAJHBTkFuvq7XtKmqed7Wpk/'

def get_updates():
    try:
        r = requests.get(f'{URL}getUpdates')
        return r.json()
    except requests.exceptions.ConnectionError:
        return print("Проблема с подлючение к верверу, проверте интернет или верность ссылки!")
    except KeyError:
        return print("Houston, we have a problem")

class Message():

    def __init__(self):
        pass

    def get_message(self):
        data = get_updates()

        last_obj = data['result'][-1]
        curr_update_id = last_obj['update_id']

        global last_upd
        if last_upd != curr_update_id:
            last_upd = curr_update_id

            chat_id = last_obj['message']['chat']['id']
            message_text = last_obj['message']['text']
            message = {'chat_id': chat_id,
                    'text': message_text}
            return message
        return None


    def send_message(self, chat_id, text):
        url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
        requests.get(url)

def currency_name():
    l = {}
    url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    response = requests.get(url).json()
    for i in response:
            l.update({i["Cur_Abbreviation"]: i["Cur_Name"]})
    return l


def main():
    while True:
        m = Message()
        answer = m.get_message()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']
            bot_text = "/help - Помощь\n" \
                       "/currency - курсы валют на текущий день\n" \
                       "/currs_date - курсы валют на конкретное число\n" \
                       "/anekdot - случайный анекдот"


            if text == '/help':
                m.send_message(chat_id, bot_text)

            if text == "/anekdot":
                m.send_message(chat_id, word())

            if text == '/currency':
                for k, v in currency_name().items():
                    m.send_message(chat_id, f"/{k} - {v}")

            if text == 'currs_date':
                m.send_message(chat_id, "Ввеедите в формате RUB 2019-10-10")


            if text[1:] in currency_name():
                m.send_message(chat_id, get_money(text[1:]))

            if text == "/currs_date":
                m.send_message(chat_id, "Введите курс и дату в формате: курс хххх-хх-xx")

            if re.match(r'\w{3}\s\d{4}-\d{2}-\d{2}', text):
                if text[:3].upper() in currency_name():
                    m.send_message(chat_id, get_date_mom(text))
                else:
                    m.send_message(chat_id, "что-то введенно не так")
        else:
            continue

            sleep(3)

if __name__ == '__main__':
    main()