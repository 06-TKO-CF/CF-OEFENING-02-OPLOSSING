from bin.database import Database
from os.path import exists, isfile
from os import remove

class Bloem:
    fotoID = None

    def __init__(self, bloemID:int=0, naam:str='', beschrijving:str='', foto:str='') -> None:
        self._bloemID = bloemID
        self._naam = naam
        self._beschrijving = beschrijving
        self._foto = foto

    @property
    def bloemID(self):
        return self._bloemID

    @property
    def naam(self):
        return self._naam

    @property
    def beschrijving(self):
        return self._beschrijving

    @beschrijving.setter
    def beschrijving(self, beschrijving):
        self._beschrijving = beschrijving.strip()

    @property
    def foto(self):
        return self._foto

    @foto.setter
    def foto(self, foto:str) -> None:
        self._foto = foto
        
    def update(self, naam:str, beschrijving:str, foto:str) -> None:
        naam = naam.strip().upper()
        if len(naam) > 1:
            if Database.naam(bloemID=self._bloemID, naam=naam):
                self._bloemID = Database.update(bloemID=self._bloemID, naam=naam, beschrijving=beschrijving, foto=foto)
            else:
                raise Exception('DATABASE: een bloem met deze naam bestaat reeds')
        else:
            raise Exception('DATABASE: naam is een verlicht veld')
        
    def verwijder(self):
        try:
            if exists(self._foto) and isfile(self._foto):
                remove(self._foto)
        except:
            pass
        Database.verwijder(self._bloemID)
        
    def __str__(self):
        return f'{self._naam}'
    
def padFotoNieuw(self, bestandExt:str):
    Bloem.fotoID += 1
    return f'afbeelding/foto_{Bloem.fotoID}{bestandExt}'