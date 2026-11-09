import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None
        #MENU A TENDINA
        self._dd_biblioteche = None
        self._dd_genere = None

        #LIST VIEW
        self._list_view= None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO
        # MENU A TENDINA
        self._dd_biblioteche= ft.Dropdown(label="Biblioteca", on_select=self.controller.handler_dd_biblioteche)
        #POPOLO DD
        self.controller.popolo_dd_biblioteche()

        self._dd_genere = ft.Dropdown(label="Genere", on_select=self.controller.handler_dd_genere)
        # POPOLO DD
        self.controller.popolo_dd_genere()


        

        # Sezione 3: Libri
        # TODO
        btn_libri = ft.Button(content="Libri", on_click=self.controller.handler_libri)
        self._list_view= ft.ListView(expand=True)

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # TODO
            ft.Row([self._dd_biblioteche,self._dd_genere], alignment= ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3: Libri
            ft.Row([btn_libri], alignment= ft.MainAxisAlignment.CENTER),
            self._list_view
            # TODO
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
