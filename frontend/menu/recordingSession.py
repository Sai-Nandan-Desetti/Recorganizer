"""
This module defines the interface between the frontend and the backend for recording a session.
"""

from frontend.utils import ui
from backend.entities import *
from backend.services.sessionService import SessionService


def create_recording_session() -> Session:
    """
    Creates a recording `Session` (for which a `Patient` is first created).

    1. Get the details of the patient.
        - By default, you need to provide ID and Name.
        - Any other details you want to add, here's where you need to define those attributes.
        - Display the relevant text prompt and collect the corresponding information.
        - Eg. If you want to add information about the whereabouts of the patient:
            
        .. code-block:: python
            
            p_place = get_text_input('Place')
            patient = Patient(p_id, p_name, p_place)            

    2. Get the details of the session.
        - If you need the kind of info where the user must select from a list of options,
          you can use `select_option()`.
        - The template is `select_option(<field_name>, <field_options>)`.
        - Eg. If you want to add a field for the type of video being recorded:
            
        .. code-block:: python

            field_name = 'Video category'
            field_options = ['Surgery', 'Education', 'Testimonial']
            selected_category = select_option(field_name, field_options)
            session = Session(patient, department=selected_dept, category=selected_category)
            
    """
    p_id = ui.get_text_input('Patient ID')
    p_name = ui.get_text_input('Patient Name')    
    patient = Patient(p_id, p_name)
        
    departments = ['Opthalmology', 'Urology', 'Cardiology']
    selected_dept = ui.select_option('Select Department', departments)
    session = Session(patient, department=selected_dept)    
    return session


def start_session(sessionService: SessionService, vlc_path: str):
    """
    Starts a `Session`

    :param sessionService: a `SessionService`
    :type sessionService: :class:`SessionService`
    :param vlc_path: path to the VLC player executable
    :type vlc_path: str
    """    
    try:
        sessionService.start(vlc_path)
        ui.success('VLC opened successfully!')
    except FileNotFoundError as fe:
        ui.error(str(fe) + '\nPlease check the path.')


def end_session(sessionService: SessionService):
    """
    Ends a `Session`

    :param sessionService: a `SessionService`
    :type sessionService: :class:`SessionService`
    """
    try:
        n = sessionService.end()
        if n > 0:
            ui.success(f'Successfully organized {n} files from {sessionService.get_source_folder()}')
        else:
            ui.error(f'No files found in {sessionService.get_source_folder()}')
    except Exception as ex:
        ui.error('Error in moving the files\n' + str(ex))
