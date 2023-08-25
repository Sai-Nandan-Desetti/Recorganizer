"""
The main file that runs the Recorganizer app.
"""

from frontend.utils import ui
from frontend.menu import *


class App:
    """
    The Recorganizer App
    """
    def __init__(self):
        self._name = 'Recorganizer'
        self._menu = ['Record Session', 'About']
        
    
    def run(self, vlc_path: str):
        """
        The function that runs the app.

        - This is a menu-driven app. But the menu has only two options:
            - Record Session
            - About
        - So, you can either record a session or read about the app.
            - There's nothing much to read about; so, please go and record something!
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
