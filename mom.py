import requests

def get_money(currency):
    url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    response = requests.get(url).json()
    d = {}
    for x in response:
        d[x["Cur_Abbreviation"]] = x['Cur_ID']
    data = d[currency]
    for x in response:
        if data == x['Cur_ID']:
            return ('today for 1 BYN - {} {}'.format(x['Cur_OfficialRate'], x["Cur_Abbreviation"]))


