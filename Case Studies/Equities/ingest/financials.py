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
    
    def __init__(self) -> None:
        self.session = None
        self.logger = logging.basicConfig(filename='example.log', encoding='utf-8')
    
    def run(self) -> Dict:
        stock_data = {}
        stock = yfi.Ticker("INFY.NS")
        stock_data['financials'] = self.get_financial_data(stock_name="INFY.NS", )
        return stock_data

    def get_financial_data(
        self, stock_name: AnyStr="", target_table: AnyStr="profit-loss", table_clss:AnyStr="data-table responsive-text-nowrap"
    ):
        try:
            session = self.session or _requests
            stock_name = stock_name.split('.NS')[0] if ".NS" in stock_name else stock_name

            crawled_data = session.get(f"https://www.screener.in/company/{stock_name}/")
            stock_soup = BeautifulSoup(crawled_data, "lxml")
            pl_table = stock_soup.find("section", {"id":target_table}).find("table", {"class": table_clss})
            df = pd.DataFrame(columns = [i.text for i in pl_table.find_all("th")])

            for j in pl_table.find_all("tr")[1:]:
                row = [" ".join(re.findall("[a-zA-Z]+", i.text)) for i in j.find_all("td")]
                df.loc[len(df)] = row
            
            return df.to_dict(orient="records")
        except Exception as err:
            self.logger.error(err, exc_info=True)
