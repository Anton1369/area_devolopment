import requests

url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'

def get_date_mom(text):
    x = text.split()
    response = requests.get(url).json()
    d = {}
    for i in response:
        d[i["Cur_Abbreviation"]] = i['Cur_ID']

    url2 = 'http://www.nbrb.by/API/ExRates/Rates/'+ str(d[x[0].upper()]) + '?onDate=' + x[-1]

    r = requests.get(url2).json()

    return f'{r["Date"]:.10} 1 {r["Cur_Abbreviation"]} стоил {r["Cur_OfficialRate"]:.3} BYN'

