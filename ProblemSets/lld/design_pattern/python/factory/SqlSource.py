from abc import abstractmethod
from IngestToDb import IngestToDb
class SqlSource(IngestToDb):
    def __init__(self) -> None:
        pass

    def ingest_data(self) -> None:
        print("Ingested to SQL source")
    