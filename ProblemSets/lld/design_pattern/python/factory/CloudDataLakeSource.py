from IngestToDb import IngestToDb

class CloudDataLakeSource(IngestToDb):
    def __init__(self) -> None:
        pass

    def ingest_data(self) -> None:
        print("CLOUD: Ingested data to DataLake.")
