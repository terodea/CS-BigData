import re
import logging
from typing import Dict, List, AnyStr
from bs4 import BeautifulSoup
import yfinance as yfi
import requests as _requests
import pandas as pd
from sys import exc_info

class IngestFinancialData:
    __slots__ = ["session", "logger"]
    __doc__ = ""

    is_digit = lambda _val: bool(re.match('^[0-9\.]*$',_val))
    is_comma_numeric = lambda _val: bool(re.match('^[0-9\,]*$',_val))
    is_percent = lambda _val: bool(re.match('^[0-9\%]*$',_val))
    
    def __init__(self) -> None:
        self.session = None
        self.logger = logging.basicConfig(filename='example.log')
    
    def run(self) -> Dict:
        stock_data = {}
        stock = yfi.Ticker("INFY.NS")
        stock_data['financials'] = self.get_financial_data(stock_name="INFY.NS")
        return stock_data

    def get_financial_data(
        self, stock_name: AnyStr="", target_table: AnyStr="profit-loss", table_clss:AnyStr="data-table responsive-text-nowrap"
    ):
        try:
            
            session = self.session or _requests
            stock_name = stock_name.split('.NS')[0] if ".NS" in stock_name else stock_name

            crawled_data = session.get(f"https://www.screener.in/company/{stock_name}/")
            stock_soup = BeautifulSoup(crawled_data.text, "html.parser")
            pl_table = stock_soup.find("section", {"id":target_table}).find("table", {"class": table_clss})
            df = pd.DataFrame(columns = [i.text for i in pl_table.find_all("th")])

            for j in pl_table.find_all("tr")[1:]:
                row_val = []
                for i in j.find_all("td"):
                    _val = i.text
                    if self.is_digit(_val) or self.is_comma_numeric(_val) or self.is_percent(_val):
                        row_val.append(_val)
                    else:
                        row_val.append(" ".join(re.findall("[a-zA-Z0-9]+", _val)))
                df.loc[len(df)] = row_val
            
            return df.to_dict(orient="records")
        except Exception as err:
            self.logger.error(err, exc_info=True)


if __name__ == "__main__":
    obj = IngestFinancialData()
    obj.get_financial_data(stock_name="ABB")
