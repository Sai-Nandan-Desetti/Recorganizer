from datetime import datetime
from backend.entities.patient import Patient

class Session:
    """
    A `Session` is defined by 
    - A `Patient`
    - Date of the session
    - (More attributes (eg: the department examining the patient) can be added if necessary.)
    """
    def __init__(self, patient: Patient, **kwargs):
        self.patient = patient
        self.__dict__.update(kwargs) # add attributes to class based on kwargs
        self.date = datetime.now().strftime("%Y%m%d")
    
    def __repr__(self):
        return f'Session(' + ', '.join([f'{key} = {value}' for key, value in self.__dict__.items()]) + ')'   



"""
A test run that first creates a `Patient` (using ID and Name) 
and then a `Session` using today's date.
"""
if __name__ == '__main__':
    patient = Patient('AX314', 'ABC')
    session = Session(patient)
    print(repr(session))
