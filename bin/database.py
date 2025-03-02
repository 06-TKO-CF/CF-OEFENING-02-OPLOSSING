import sqlite3

class Database:
    @staticmethod
    def verbind():
        '''
        deze methode staat in voor het tot stand brengen
        van een verbinding met cursor met de database

        enkel voor intern gebruik
        '''
        dbVerbinding = sqlite3.connect('data/bloem.sqlite3')
        dbCursor = dbVerbinding.cursor()

        return dbVerbinding, dbCursor

    @staticmethod
    def naam(bloemID:int=0, naam:str='') -> bool:
        dbVerbinding, dbCursor = Database.verbind()
        
        dbSql = '''
            SELECT COUNT(1)
            FROM bloem
            WHERE bloemID <> ?
                AND naam = ?
        '''
        
        dbResultaat = dbCursor.execute(dbSql, (bloemID, naam))
        dbAantal = dbResultaat.fetchone()[0]

        return  dbAantal < 1
    
    @staticmethod
    def lijst(zoek:str='') -> list:
        zoek = zoek.strip().upper()
        dbVerbinding, dbCursor = Database.verbind()

        dbSql = '''
            SELECT * FROM bloem 
            ORDER BY naam
        '''
        dbResultaat = dbCursor.execute(dbSql)

        return [list(dbRij) for dbRij in dbResultaat.fetchall()]
    
    @staticmethod
    def update(bloemID:int, naam:str, beschrijving:str, foto:str) -> None:
        dbVerbinding, dbCursor = Database.verbind()
        
        try:
            if bloemID == 0:
                dbSql = '''
                    INSERT INTO bloem(naam, beschrijving, foto)
                    VALUES (?, ?, ?)
                '''
                
                dbCursor.execute(dbSql, (naam, beschrijving, foto))
                
                dbVerbinding.commit()
                
                return dbCursor.lastrowid
            else:
                dbSql = '''
                    UPDATE bloem
                        SET naam = ?,
                            beschrijving = ?,
                            foto = ?
                    WHERE bloemID = ?
                '''
                dbCursor.execute(dbSql, (naam, beschrijving, foto, bloemID))
                dbVerbinding.commit()
                
                return bloemID

        except Exception as ex:
            raise Exception(f'FOUT UPDATE: {ex}')
        
    @staticmethod
    def verwijder(bloemID:int) -> None:
        dbVerbinding, dbCursor = Database.verbind()

        try:
            dbSql = '''
                DELETE FROM bloem
                WHERE bloemID = ?
            '''
            dbCursor.execute(dbSql, (bloemID,))

            dbVerbinding.commit()
        except Exception as ex:
            raise Exception(f'FOUT VERWIJDER: {ex}')
        
    @staticmethod
    def fotoID():
        dbVerbinding, dbCursor = Database.verbind()

        try:
            dbSql = '''
                SELECT foto
                FROM bloem
                ORDER BY foto DESC
                LIMIT 0,1
            '''
            
            dbResultaat = dbCursor.execute(dbSql)

            try:
                dbRij = dbResultaat.fetchone()
                dbFotoID = int(dbRij[0].split('.')[0].split('_')[1])
                
                return dbFotoID
            except:
                return 0
        except Exception as ex:
            pass