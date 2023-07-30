import os
import json
import codecs
import config as config

from tinkoff.invest import Client

from tools.trader_api.TraderAPI import TraderAPI

from tinkoff.invest.utils import now, quotation_to_decimal, decimal_to_quotation

TOKEN = config.TOKEN_TINKOFF


def main():
    trader = TraderAPI(response_format="json")

    with Client(TOKEN) as client:
        tools = client.instruments.shares()
        data = []
        for item in tools.instruments:
            currency = item.currency
            if (currency == 'rub'):
                share = {
                    'name': item.name,
                    'figi': item.figi,
                    'ticker': item.ticker,
                    'isin': item.isin,
                    'minPriceIncrement': float(quotation_to_decimal(item.min_price_increment)),
                    'currency': item.currency,
                    'is_dividend': 0,
                }
                data.append(share)

        with open('rus_sctocks.json', 'wb') as f:
            json.dump(data, codecs.getwriter('utf-8')(f), ensure_ascii=False)

        trader.store_rus_stock(json.dumps(data))
        print('Получено ' + str(len(data)) + ' акций. Данные записаны.')


if __name__ == "__main__":
    main()
