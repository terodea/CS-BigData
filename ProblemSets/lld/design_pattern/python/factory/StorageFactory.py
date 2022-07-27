from CloudStorage import CloudStorage
from OnPremiseStorage import OnPremiseStorage

class StorageFactory:
    def __init__(self) -> None:
        pass
        
    def get_storage_object(self, source:str) -> None:
        if(source == "CLOUD"):
            return CloudStorage()
        elif(source == "ONPREMISE"):
            return OnPremiseStorage()
        else:
            print("Unknown source")
            return None