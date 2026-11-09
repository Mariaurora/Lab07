import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popolo_dd_biblioteche(self):
        self._view._dd_biblioteche.options.append(ft.DropdownOption(key=None , text="NESSUN FILTRO"))
        for biblioteca in self._model.get_biblioteche():
            self._view._dd_biblioteche.options.append(ft.DropdownOption(key=f"{biblioteca.nome}", text=f"{biblioteca}"))


    def popolo_dd_genere(self):
        self._view._dd_genere.options.append(ft.DropdownOption(key=None , text="NESSUN FILTRO"))
        for genere in self._model.get_generi():
            self._view._dd_genere.options.append(ft.DropdownOption(key=f"{genere}" , text=f"{genere}"))


    # CALLBACKS DROPDOWN
    # TODO

    def handler_dd_biblioteche(self,e):
        #FLET QUANDO key= None prende il valore di text
        if self._view._dd_biblioteche.value == "NESSUN FILTRO":
            self.biblioteca_selezionata= None
        else:
         self.biblioteca_selezionata = self._view._dd_biblioteche.value
        print(self.biblioteca_selezionata)

    def handler_dd_genere(self,e):
        if self._view._dd_genere.value == "NESSUN FILTRO":
            self.genere_selezionato= None
        else:
         self.genere_selezionato = self._view._dd_genere.value
        print(self.genere_selezionato)



    # AZIONE: MOSTRA LIBRI
    # TODO
    def handler_libri(self,e):
        self._view._list_view.controls.clear()
        for libro in self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato):
            self._view._list_view.controls.append(ft.Text(str(libro)))

        if self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)==[]:
            self._view.show_alert('Nessun libro corrisponde ai criteri di ricerca')

