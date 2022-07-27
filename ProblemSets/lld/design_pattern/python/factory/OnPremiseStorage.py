from IngestionService import IngestionService
from SqlSource import SqlSource
from DataLakeSource import DataLakeSource
from NoSqlSource import NoSqlSource
from IngestToDb import IngestToDb

class OnPremiseStorage(IngestionService):
    def __init__(self) -> None:
        super().__init__()

    def get_source_instance(self, source: str) -> IngestToDb:
        """
        """
        if(source == "NOSQL"):
            return NoSqlSource()
        elif(source == "SQL"):
            return SqlSource()
        elif(source == "DATALAKE"):
            return DataLakeSource()
        else:
            print("Unknown source")
