from bin.database import Database

from .bloem import Bloem

class Container:
    def __init__(self):
        self._bloemen = []

        for bloem in Database.lijst():
            self._bloemen.append(Bloem(bloem[0], bloem[1], bloem[2], bloem[3]))

        Bloem.fotoID = Database.fotoID()

    def lijst(self):
        self._bloemen = []

        for bloem in Database.lijst():
            self._bloemen.append(Bloem(bloem[0], bloem[1], bloem[2], bloem[3]))
        
        return self._bloemen
    
    def nieuw(self) -> Bloem:
        return Bloem()
    
    def update(self, oBloem:Bloem, naam:str, beschrijving:str, foto:str):
        if oBloem not in self._bloemen:
            self._bloemen.append(oBloem)
            
        oBloem.update(naam, beschrijving, foto)

    def verwijder(self, oBloem):
        if oBloem in self._bloemen:
            oBloem.verwijder()
            self._bloemen.remove(oBloem)