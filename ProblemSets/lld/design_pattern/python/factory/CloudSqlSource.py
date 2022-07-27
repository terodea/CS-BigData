from abc import abstractmethod
import IngestToDb
class CloudSqlSource(IngestToDb.IngestToDb):
    def __init__(self) -> None:
        pass

    def ingest_data(self) -> None:
        print("Cloud: Ingested to SQL source")
    