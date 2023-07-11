import os
import json, codecs
import config as config

from tinkoff.invest import Client

from tools.trader_api.TraderAPI import TraderAPI



TOKEN = config.TOKEN_TINKOFF

def main():
    with Client(TOKEN) as client:
        tools = client.instruments.shares()
        data = []
        for item in tools.instruments:
            currency = item.currency
            if (currency == 'rub'):
                share = {item.figi : item.name }
                data.append(share)

        with open('rus_sctocks.json', 'wb') as f:
            json.dump(data, codecs.getwriter('utf-8')(f), ensure_ascii=False)        
        print('Получено ' + str(len(data)) + ' акций. Данные записаны.')



if __name__ == "__main__":
    main()