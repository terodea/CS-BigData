from abc import ABC, abstractmethod, ABCMeta


class IngestToDb(ABC):
    def __init__(self) -> None:
        pass

    def ingest_data(self):
        pass
