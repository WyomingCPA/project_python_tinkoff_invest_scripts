from xml.etree import ElementTree
import datetime
import requests
import json

from tools.trader_api.URLs import *

class TraderAPI:
    def __init__(self, response_format="json"):
        self.format = response_format
        self.url = URLs()
        self.auth = ''

    def __get_symbol_string(self, symbols):
        if not isinstance(symbols, str): # list
            symbols = ",".join(symbols)
        return symbols

    def __to_format(self, response):
        if self.format == "json":
            return response.json()
        else:
            return ElementTree.fromstring(response.content)

    def __get_data(self, url):
        return self.__to_format(requests.get(url, auth=self.auth))

    def __submit_post(self, url, data):
        return self.__to_format(requests.post(url, data=data))

    def store_order(self, data):
        return self.__submit_post(self.url.order_store_url(), data)

    def store_spot(self, order_id, type, value):
        data=[('order_id', order_id), ('type', type), ('value', value)] 
        return self.__submit_post(self.url.spot_store_url(), data)

    def store_console(self, type, message, value):
        data=[('type', type), ('message', message), ('value', value)] 
        return self.__submit_post(self.url.console_store_url(), data)

    def store_check_script(self, data):
        return self.__submit_post(self.url.check_script_url(), data)

    def update_futures_database(self, data): 
        return self.__submit_post(self.url.update_futures_url(), data)

    def get_favorite_futures(self):
        return self.__get_data(self.url.favorutes_futures_url())

    def get_favorite_stock(self):
        return self.__get_data(self.url.favorutes_stock_url())

    def get_accounts(self):
        """Returns all of the user's accounts."""
        return self.__get_data(self.url.accounts_url())

    def get_account(self, id):
        """Returns a specific account provided the account ID (account number)
        """
        return self.__get_data(self.url.account_url().format(id=str(id)))

    def get_account_balances(self, id):
        """Returns the balances of a specific account (ID = account number)
        """
        return self.__get_data(self.url.account_balances_url().format(id=str(id)))

    def get_account_history(self, id):
        """Returns the history of a specific account (ID = account number)
        """
        return self.__get_data(self.url.account_history_url().format(id=str(id)))

    def get_account_holdings(self, id):
        """Returns the holdings of a specific account (ID = account number)"""
        return self.__get_data(self.url.account_holdings_url().format(id=str(id)))

    def get_market_clock(self):
        """Returns the state of the market, the time until next state change, and current server timestamp."""
        return self.__get_data(self.url.clock_url())

    def get_quote(self, symbols):
        """Returns quote information for a single ticker or list of tickers. Note: this function does not implement selecting customer FIDs as described in the API documentation. These can be filtered from the return if need be."""
        url = self.url.quote_url()+"?symbols={symbols}"
        symbols = self.__get_symbol_string(symbols)
        return self.__get_data(url.format(symbols=symbols))