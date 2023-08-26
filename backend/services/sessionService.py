from backend.entities.session import Session
from backend.services.fileService import *
import subprocess


class SessionService:
    """
    :class: `SessionService` - A service class to handle a `Session`
    
    :param session: a `Session`
    :type session: :class:`Session`
    :param base_path: path to the source folder where the recorded snippets are stored during the session; defaults to './Recordings'
    :type base_path: str             
    """
    def __init__(self, session: Session, base_path: str='./Recordings'):
        self.session = session
        self.base_path = base_path


    def get_source_folder(self) -> str:
        return self.base_path

    
    def start(self, vlc_path: str):
        """
        Starts the VLC media player.
        
        :param vlc_path: path to the VLC executable
        :type vlc_path: str
        """        
        subprocess.Popen(vlc_path)     


    def set_destination_path(self) -> str:
        """
        Sets the destination folder for the recordings. You have to define your desired order of the directories in this method.

        :return: path to the destination folder
        :rtype: str
        """
        sub_dirs = [str(self.session.department), str(self.session.patient.id), str(self.session.date)]
        destination = construct_path(self.base_path, sub_dirs)
        return destination
    
        
    def end(self) -> int:
        """
        Organizes the recordings as desired in the intended destination.

        :return: the number of files successfully organized
        :rtype: int
        """
        src, dest = self.base_path, self.set_destination_path()
        return organize_recorded_files(src, dest)
