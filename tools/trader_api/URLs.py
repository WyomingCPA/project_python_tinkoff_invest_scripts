class URLs:
    def __init__(self, response_format="json"):
        self.format = response_format
        self.base_url = "http://localhost/trade-tools/public/api"
        #self.base_url = "http://trade-tools.simpleitrunner.ru:3000/api"

        # account
        self.accounts = "accounts.{format}".format(format=self.format)
        self.accounts_balances = "accounts/balances.{format}".format(format=self.format)
        self.account = "accounts/{id}.{format}".format(format=self.format, id="{id}")
        self.account_balances = "accounts/{id}/balances.{format}".format(format=self.format, id="{id}")
        self.account_history = "accounts/{id}/history.{format}".format(format=self.format, id="{id}")
        self.account_holdings = "accounts/{id}/holdings.{format}".format(format=self.format, id="{id}")

        # market
        self.clock = "market/clock.{format}".format(format=self.format)
        self.quote = "market/ext/quotes{format}".format(format=self.format)

        #orders
        self.order_store = "/trader/store"
        self.spot_store = "/trader/add_spot"
        self.check_script = "/trader/check-script"

        #futures
        self.update_futures_store = "/trader/store-all-futures"
        self.get_favorites_futures = "/trader/favorites"

        #stock
        self.get_favorites_stock = "/trader/favorites-stock"

        #console log
        self.console_store = "/console/store"

        #get data from Tinkoff
        self.save_rus = "/data/save-rus-stock"
        

    def base_url(self):
        return self.base_url

    def accounts_url(self):
        return self.base_url + self.accounts

    def order_store_url(self):
        return self.base_url + self.order_store

    def check_script_url(self):
        return self.base_url + self.check_script

    def spot_store_url(self):
        return self.base_url + self.spot_store

    def console_store_url(self):
        return self.base_url + self.console_store

    def update_futures_url(self):
        return self.base_url + self.update_futures_store

    def favorutes_futures_url(self):
        return self.base_url + self.get_favorites_futures

    def favorutes_stock_url(self):
        return self.base_url + self.get_favorites_stock

    def account_url(self):
        return self.base_url + self.account

    def account_history_url(self):
        return self.base_url + self.account_history

    def account_holdings_url(self):
        return self.base_url + self.account_holdings

    def clock_url(self):
        return self.base_url + self.clock

    def quote_url(self):
        return self.base_url + self.quote
    
    def save_rus_stock(self):
        return self.base_url + self.save_rus