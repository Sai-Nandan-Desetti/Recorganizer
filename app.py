from frontend.utils import ui
from frontend.menu import *


class App:
    """
    The Recorganizer :class:`App`
    """
    def __init__(self):
        self._name = 'Recorganizer'
        self._menu = ['Record Session', 'About']
        
    
    def run(self, vlc_path: str):
        """
        The method that runs the app. The app is designed to be menu-driven. But there are only two options: Record Session and About.            

        :param vlc_path: path to the VLC executable; the path must have forward slashes
        :type vlc_path: str
        """
        ui.set_title(self._name)        
        menu_option = ui.select_menu_option('Menu', self._menu)
        
        if menu_option == 'Record Session':
            session = create_recording_session()
            sessionService = SessionService(session)
            if ui.click('Start Session'):
                start_session(sessionService, vlc_path)
            if ui.click('End Session'):
                end_session(sessionService)
        
        elif menu_option == 'About':
            show_about_page()


# Run the app
if __name__ == "__main__":    
    app = App()
    # Enter the path to your VLC player here
    # Remember to keep forward slashes
    vlc_path = 'D:/Apps/VLC/vlc.exe'
    app.run(vlc_path)
