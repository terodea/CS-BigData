from IngestToDb import IngestToDb


class NoSqlSource(IngestToDb):
    def __init__(self) -> None:
        pass
    
    def ingest_data(self) -> None:
        print("Ingested to NoSQL Source.")