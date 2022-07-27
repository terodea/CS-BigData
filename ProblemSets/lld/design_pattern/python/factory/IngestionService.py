from abc import ABC, abstractmethod
from typing import AnyStr
class IngestionService(ABC):
    """
    An abstract factory implementation.
    """
    def __init__(self) -> None:
        pass

    def ingest_data_to_db(self, source: str) -> None:
        sourceObject = self.get_source_instance(source)
        sourceObject.ingest_data()
    
    @abstractmethod
    def get_source_instance(self, source):
        pass