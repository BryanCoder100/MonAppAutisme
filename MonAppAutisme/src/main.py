# src/main.py
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

# importe tes classes d'écran
from app.ui.screens.home import HomeScreen
from app.ui.screens.puzzle import PuzzleScreen

class AutismeApp(App):
    def build(self):
        # on charge automatiquement tous les *.kv du dossier screens
        Builder.load_file("src/app/ui/screens/home.kv")
        Builder.load_file("src/app/ui/screens/puzzle.kv")

        sm = ScreenManager()
        sm.add_widget(HomeScreen())
        sm.add_widget(PuzzleScreen())
        return sm

if __name__ == "__main__":
    AutismeApp().run()
