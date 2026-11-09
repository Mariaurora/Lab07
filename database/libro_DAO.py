from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        self._cnx=DBConnect.get_connection()

    def read_libri(self, nome , genere):
        query="""SELECT libro.id, titolo ,autore, genere ,anno_pubblicazione ,id_biblioteca
                 FROM libro , biblioteca
                 WHERE biblioteca.nome=COALESCE(%s, biblioteca.nome) AND libro.id_biblioteca = biblioteca.id
                 AND  libro.genere = COALESCE(%s, libro.genere)"""
        cursor=self._cnx.cursor()
        cursor.execute(query,(nome , genere ,))

        lista_libri=[]
        for row in cursor:
          libro=Libro(*row)
          lista_libri.append(libro)

        return lista_libri



