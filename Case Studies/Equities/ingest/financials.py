from cmath import log
import re
import logging
from tkinter import N
from typing import Dict, List, AnyStr
from bs4 import BeautifulSoup
import yfinance as yfi
import requests as _requests
import pandas as pd
from sys import exc_info

class IngestFinancialData:
    """
    TODO:
    1. Streaming Service [Kafka, Spark Structured Streaming]
    2. Design and Create Schema
    """
    __slots__ = ["session", "logger", "df", "stock_names"]
    __doc__ = ""

    is_digit = lambda self, _val: bool(re.match('^[0-9\.]*$',_val)) # 3.19
    is_comma_numeric = lambda self, _val: bool(re.match('^[0-9\,]*$',_val)) # 3,19
    is_percent = lambda self, _val: bool(re.match('^[0-9\%]*$',_val)) # 3% identify for  3.19%
    
    def __init__(self) -> None:
        self.session = None
        self.df = None
        logging.basicConfig(filename='example.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filemode="w")
        self.logger = logging.getLogger("example.log")
    
    def run(self) -> Dict:
        import pdb
        pdb.set_trace()
        stock_data = {}
        stock = yfi.Ticker("INFY.NS")
        stock_data['financials'] = self.get_financial_data(stock_name="INFY.NS")
        return stock_data

    def get_financial_data(
        self, stock_name: AnyStr="", target_table: AnyStr="profit-loss", table_clss:AnyStr="data-table responsive-text-nowrap"
    ):
        try:
            self.read_source()
            session = self.session or _requests
            stock_names = self.stock_names if self.stock_names else (stock_name.split('.NS')[0] if ".NS" in stock_name else stock_name)
            stock_names = [stock_names[0]]
            for stock_name in stock_names:
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

    def read_source(self, target_col:AnyStr=""):
        try:
            # NSE
            self.df = pd.read_csv("/Users/akshayterode/Desktop/DEV/CS-BigData/Case Studies/Equities/ingest/data/NSE_Securities.csv", index_col=False)
            self.stock_names = [f"{i}" for i in self.df["SYMBOL"].unique().tolist()]
            # BSE
            # self.df = pd.read_csv("/Users/akshayterode/Desktop/DEV/CS-BigData/Case Studies/Equities/ingest/data/NSE_Securities.csv", index_col=False)
            # self.stock_names = [f"{i}.BO" for i in self.df["Security Id"].unique().tolist()]
        except Exception as err:
            self.logger.error(msg=err, exc_info=True)
            raise err

if __name__ == "__main__":
    obj = IngestFinancialData()
    obj.run()
    # obj.get_financial_data()
    # df = obj.get_financial_data(stock_name="ABB")
    import pdb
    pdb.set_trace()
    a=1
    b=1