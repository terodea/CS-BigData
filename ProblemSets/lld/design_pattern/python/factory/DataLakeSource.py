from IngestToDb import IngestToDb

class DataLakeSource(IngestToDb):
    def __init__(self) -> None:
        pass

    def ingest_data(self) -> None:
        print("Ingested data to DataLake.")
