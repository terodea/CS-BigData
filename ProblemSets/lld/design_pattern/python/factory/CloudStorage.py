from IngestionService import IngestionService
from IngestToDb import IngestToDb
from CloudNoSqlSource import CloudNoSqlSource
from CloudSqlSource import CloudSqlSource
from CloudDataLakeSource import CloudDataLakeSource
class CloudStorage(IngestionService):
    def __init__(self) -> None:
        pass

    def get_source_instance(self, source: str) -> IngestToDb:
        """
        """
        if(source == "NOSQL"):
            return CloudNoSqlSource()
        elif(source == "SQL"):
            return CloudSqlSource()
        elif(source == "DATALAKE"):
            return CloudDataLakeSource()
        else:
            print("Unknown source")