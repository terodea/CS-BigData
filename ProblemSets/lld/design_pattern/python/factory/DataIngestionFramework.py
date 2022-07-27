from StorageFactory import StorageFactory

class DataIngestionFramework:
    def __init__(self) -> None:
        pass

    def ingest(self, storage:str, source:str) -> None:
        storageFactory = StorageFactory()
        storageObject = storageFactory.get_storage_object(storage)
        storageObject.ingest_data_to_db(source)


if __name__ == "__main__":
    DIFramework = DataIngestionFramework()
    DIFramework.ingest("CLOUD", "NOSQL")
    DIFramework.ingest("CLOUD", "SQL")
    DIFramework.ingest("ONPREMISE", "DATALAKE")