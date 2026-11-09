from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        self._cnx=DBConnect.get_connection()

    def read_bibblioteca(self):
        query="""SELECT id, nome, indirizzo
                 FROM biblioteca"""
        cursor=self._cnx.cursor()
        cursor.execute(query)

        lista_biblioteche=[]
        for row in cursor:
            biblioteca=Biblioteca(*row)
            lista_biblioteche.append(biblioteca)
        return lista_biblioteche





    # TODO
