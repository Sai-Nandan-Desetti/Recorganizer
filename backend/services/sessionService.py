from backend.entities.session import Session
from backend.services.fileService import *
import subprocess


class SessionService:
    """
    A service class to handle a `Session`
    - It needs the `base_path` of the video recordings.
        - If no path is provided, it's assumed that there's a folder named `Recordings` 
        in the `Recorganizer` folder.        
    """
    def __init__(self, session: Session, base_path: str='./Recordings'):
        self.session = session        
        self.base_path = base_path


    def start(self, vlc_path: str):
        """
        Opens the VLC app for recording.
        - This is equivalent to typing in the shell:
        `start <vlc_path>`
        """        
        subprocess.Popen(vlc_path)     


    def set_destination_path(self):
        """
        Sets the destination folder for the recordings.
        - Here's where you have to define the order of the directories along the path.
        """
        sub_dirs = [str(self.session.department), str(self.session.patient.id), str(self.session.date)]
        destination = construct_path(self.base_path, sub_dirs)
        return destination
    
        
    def end(self):
        """
        Transfers the recordings from the `base_path` to the intended destination.           
        """
        src, dest = self.base_path, self.set_destination_path()
        organize_recorded_files(src, dest)               
