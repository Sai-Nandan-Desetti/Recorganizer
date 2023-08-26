class Patient:
    """
    :class: `Patient` defines a patient.
        
    :param id: the patient's ID
    :type id: str
    :param name: the patient's name
    :type name: str

    - More attributes can be added if necessary.
    - Example:
        - A test run that creates and displays two patients:
            1. Patient with only ID and Name
            2. Patient with ID, Name, and Place.
    
    .. code-block:: python

        if __name__ == '__main__':
            patient = Patient('AX314', 'ABC')
            print(repr(patient))
            patient = Patient('GF342', 'POW', place='X-122')
            print(repr(patient))
    """

    def __init__(self, id: str, name: str, **kwargs):
        self.id = id
        self.name = name
        self.__dict__.update(kwargs) # add attributes to class based on kwargs

    def __repr__(self) -> str:
        """
        A string representation for the :class: `Patient`
        """
        return 'Patient(' + ', '.join([f'{key} = {value}' for key, value in self.__dict__.items()]) + ')'        



"""
A test run that creates and displays two patients:
1. Patient with only ID and Name
2. Patient with ID, Name, and Place.
"""
if __name__ == '__main__':
    patient = Patient('AX314', 'ABC')
    print(repr(patient))
    patient = Patient('GF342', 'POW', place='X-122')
    print(repr(patient))
