from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        return self._libro_dao.read_libri(biblioteca, genere)

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        # TODO
        lista_generi = []
        for libro in self._libro_dao.read_libri(None,None):
            genere=libro.genere
            if genere  not in lista_generi:
               lista_generi.append(genere)
        return lista_generi


    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        # TODO
        return self._biblioteca_dao.read_bibblioteca()

