from IngestToDb import IngestToDb


class CloudNoSqlSource(IngestToDb):
    def __init__(self) -> None:
        pass
    
    def ingest_data(self) -> None:
        print("CLOUD: Ingested to NoSQL Source.")