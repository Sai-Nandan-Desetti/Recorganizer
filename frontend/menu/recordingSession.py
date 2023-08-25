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
        - Eg: If you want to add information about the whereabouts of the patient:
            `
            p_place = get_text_input('Place')
            patient = Patient(p_id, p_name, p_place)
            `

    2. Get the details of the session.
        - If you need the kind of info where the user must select from a list of options,
          you can use `select_option()`.
        - The template is `select_option(<field_name>, <field_options>)`.
        - Eg: If you want to add a field for the type of video being recorded:
            `
            field_name = 'Video category'
            field_options = ['Surgery', 'Education', 'Testimonial']
            selected_category = select_option(field_name, field_options)
            session = Session(patient, department=selected_dept, category=selected_category)
            `
    """
    p_id = ui.get_text_input('Patient ID')
    p_name = ui.get_text_input('Patient Name')    
    patient = Patient(p_id, p_name)
        
    departments = ['Opthalmology', 'Urology', 'Cardiology']
    selected_dept = ui.select_option('Select Department', departments)
    session = Session(patient, department=selected_dept)    
    return session


def start_session(sessionService: SessionService, vlc_path: str) -> SessionService:
    """
    Uses the `SessionService` service class to start a `Session`
    """    
    try:
        sessionService.start(vlc_path)
        ui.success('VLC opened successfully!')
    except FileNotFoundError as fe:
        ui.error(str(fe) + '\nPlease check the path.')    


def end_session(sessionService: SessionService):
    """
    Uses `SessionService` to end a `Session`
    """
    sessionService.end()
